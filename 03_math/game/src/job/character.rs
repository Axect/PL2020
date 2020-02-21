use crate::engine::command::{Command, TargetProp};

pub trait Character {
    fn attack(&self, enemy: &Self) -> Command;
    fn defense(&self, enemy: &Self) -> Command;
    fn special_attack(&self, enemy: &Self) -> Command;
    fn special_defense(&self, enemy: &Self) -> Command;
    fn receive_damage(&mut self, damage: usize);
    fn get_mut_prop(&mut self, prop: &TargetProp) -> &mut usize;
    fn is_dead(&self) -> bool;
}

#[derive(debug, Copy, Clone)]
pub struct Status {
    pub hp: usize,
    pub mp: usize,
    pub atk: usize,
    pub def: usize,
    pub cri: usize,
    pub dex: usize,
}