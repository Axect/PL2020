extern crate peroxide;
//extern crate rayon;

use peroxide::*;
use std::collections::HashSet;
use std::iter::FromIterator;
use std::fmt;

pub fn gen_lotto_bonus() -> (HashSet<usize>, usize) {
    let data: Vec<usize> = (1 .. 46).collect();
    let sample = data.sample(7);
    let bonus = sample[6];
    (HashSet::from_iter(sample[..6].to_vec()), bonus)
}

pub fn gen_lotto() -> HashSet<usize> {
    let data: Vec<usize> = (1 .. 46).collect();
    HashSet::from_iter(data.sample(6))
}

type Data = Vec<HashSet<usize>>;

pub fn lotto_sample(n: usize) -> Data {
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

impl Winner {
    pub fn mut_sum(&mut self, rhs: &Self) {
        self.one += rhs.one;
        self.two += rhs.two;
        self.thr += rhs.thr;
        self.fou += rhs.fou;
        self.fiv += rhs.fiv;
    }
}

impl fmt::Display for Winner {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        writeln!(f, "1등:{}\n2등:{}\n3등:{}\n4등:{}\n5등:{}", self.one, self.two, self.thr, self.fou, self.fiv)
    }
}

pub fn count(data: &Data, answer: &HashSet<usize>, bonus: usize) -> Winner {
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

pub fn count_elem(elem: &HashSet<usize>, answer: &HashSet<usize>) -> usize {
    elem.intersection(answer).count()
}

pub fn calc(n: usize, w: &Winner) {
    let mut total = n * 5000;
    total -= w.fou * 50000 + w.fiv * 5000;
    let one_total = total as f64 * 0.75;
    let two_total = total as f64 * 0.125;
    let thr_total = total as f64 * 0.125;

    match div_by_people(one_total, w.one) {
        Some(value) => println!("1등 당첨금은 {}입니다.", value),
        None => println!("1등은 없습니다.")
    }

    match div_by_people(two_total, w.two) {
        Some(value) => println!("2등 당첨금은 {}입니다.", value),
        None => println!("2등은 없습니다.")
    }

    match div_by_people(thr_total, w.thr) {
        Some(value) => println!("3등 당첨금은 {}입니다.", value),
        None => println!("3등은 없습니다.")
    }
}

fn div_by_people(total: f64, people: usize) -> Option<f64> {
    if people == 0 {
        None
    } else {
        Some(total / people as f64)
    }
}

//fn count_par(data: &Data, answer: &HashSet<usize>, bonus: usize) -> Winner {
//    let result = data.par_iter()
//        .map(|elem| {
//            let l = count_elem(elem, answer);
//            if l == 6 {
//                (1, 0, 0, 0, 0)
//            } else if l == 5 {
//                if elem.contains(&bonus) {
//                    (0, 1, 0, 0, 0)
//                } else {
//                    (0, 0, 1, 0, 0)
//                }
//            } else if l == 4 {
//                (0, 0, 0, 1, 0)
//            } else if l == 5 {
//                (0, 0, 0, 0, 1)
//            } else {
//                (0, 0, 0, 0, 0)
//            }
//        })
//        .reduce(|| (0,0,0,0,0), |a, b| (a.0+b.0, a.1+b.1, a.2+b.2, a.3+b.3, a.4+b.4));
//
//    Winner {
//        one: result.0,
//        two: result.1,
//        thr: result.2,
//        fou: result.3,
//        fiv: result.4
//    }
//}
