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

impl Target {
    pub fn new(p: TargetPlayer, prop: TargetProp) -> Self {
        Target {
            player: p,
            prop
        }
    }
}

#[derive(Debug, Copy, Clone)]
pub enum Operation {
    Plus(usize),
    Minus(usize),
    Mult(usize),
    Div(usize),
    Swap(Target),
}

pub type Command = Vec<(Target, Operation)>;