extern crate peroxide;
use peroxide::*;
use std::collections::HashSet;
use std::iter::FromIterator;

fn main() {
    let n = 10_000_000usize;
    let (answer, bonus) = gen_lotto_bonus();
    let data = lotto_sample(n);
    let result = count(data, answer, bonus);
    println!("{:?}", result);

}

fn gen_lotto_bonus() -> (HashSet<usize>, usize) {
    let data: Vec<usize> = (1 .. 46).collect();
    let sample = data.sample(7);
    let bonus = sample[6];
    (HashSet::from_iter(sample[..6].to_vec()), bonus)
}

fn gen_lotto() -> HashSet<usize> {
    let data: Vec<usize> = (1 .. 46).collect();
    HashSet::from_iter(data.sample(6))
}

type Data = Vec<HashSet<usize>>;

fn lotto_sample(n: usize) -> Data {
    let mut result = vec![HashSet::<usize>::default(); n];
    for i in 0 .. n {
        result[i] = gen_lotto();
    }
    result
}

#[derive(Debug, Clone, Copy, Default)]
pub struct Winner {
    pub one: usize,
    pub two: usize,
    pub thr: usize,
    pub fou: usize,
    pub fiv: usize,
}

fn count(data: Data, answer: HashSet<usize>, bonus: usize) -> Winner {
    let mut winner = Winner::default();

    for elem in data {
        let insect = elem.intersection(&answer);
        let num = insect.count();

        if num == 6 {
            winner.one += 1;
        } else if num == 5 {
            if elem.contains(&bonus) {
                winner.two += 1;
            } else {
                winner.thr += 1;
            }
        } else if num == 4 {
            winner.fou += 1;
        } else if num == 3 {
            winner.fiv += 1;
        }
    }
    winner
}
