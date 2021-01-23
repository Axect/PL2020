#[macro_use]
extern crate cached;

use cached::SizedCache;

fn main() {
    let a = c(100, 60);
    println!("{}", a);

    //let b = c_raw(200, 60);
    //println!("{}", b);
}

cached!{
    C: SizedCache<(usize, usize), usize> = SizedCache::with_size(100);
    fn c(n: usize, r: usize) -> usize = {
        if n == r || r == 0 {
            return 1;
        } else {
            return c(n-1, r-1) + c(n-1, r);
        }
    }
}

fn c_raw(n: usize, r: usize) -> usize {
    if n == r || r == 0 {
        return 1;
    } else {
        return c_raw(n-1, r-1) + c_raw(n-1, r);
    }
}
