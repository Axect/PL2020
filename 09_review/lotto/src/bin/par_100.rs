extern crate lotto;

use lotto::*;
use std::thread;
use std::sync::mpsc;

fn main() {
    let (tx, rx)= mpsc::sync_channel(100);

    let n = 10_000_000usize;
    let (answer, bonus) = gen_lotto_bonus();

    for _ in 0 .. 100 {
        let tx_sender = mpsc::SyncSender::clone(&tx);
        let ans = answer.clone();
        thread::spawn(move || {
            let data = lotto_sample(n / 100);
            let result = count(&data, &ans, bonus);
            tx_sender.send(result).unwrap();
        });
    }
    //let data = lotto_sample(n);
    //let result = count(&data, &answer, bonus);
    //let result = count_par(&data, &answer, bonus);
    
    let mut result = Winner::default();

    for (i, received) in rx.into_iter().enumerate() {
        result.mut_sum(&received);
        if i == 99 {
            break;
        }
    }
    println!("{}", result);
    calc(n, &result);
}
