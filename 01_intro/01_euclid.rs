fn main() {
    println!("GCD: {}", gcd(78696, 19332));
}

fn gcd(x: usize, y: usize) -> usize {
    match x % y {
        0 => y,
        _ => gcd(y, x % y),
    }
}
