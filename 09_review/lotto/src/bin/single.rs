extern crate lotto;
use lotto::*;

fn main() {
    let n = 10_000_000usize;
    let (answer, bonus) = gen_lotto_bonus();

    let data = lotto_sample(n);
    let result = count(&data, &answer, bonus);
    println!("{}", result);
    calc(n, &result);
}
