extern crate peroxide;
use peroxide::*;

fn main() {
    let d = dual(9, 6);
    d.sin().ln().powi(2).print();
}
