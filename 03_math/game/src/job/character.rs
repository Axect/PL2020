use engine::command::Command;

pub trait Character {
    fn attack(&self, enemy: &Self) -> Command;
    fn defense(&self, enemy: &Self) -> Command;
    
}