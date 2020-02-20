#[derive(Debug, Copy, Clone)]
pub enum TargetPlayer {
    Own,
    Enemy,
    OwnTemp(usize),
    EnemyTemp(usize),
}

#[derive(Debug, Copy, Clone)]
pub enum TargetProp {
    ATK,
    DEF,
    CRI,
    DEX,
    HP,
    MP,
}

#[derive(Debug, Copy, Clone)]
pub struct Target {
    player: TargetPlayer,
    prop: TargetProp,
}

#[derive(Debug, Copy, Clone)]
pub enum Operation {
    Plus(usize),
    Minus(usize),
    Mult(usize),
    Div(usize),
    Swap(Target),
}

#[derive(Debug, Copy, Clone)]
pub struct Command {
    target: Target,
    ops: Operation
}