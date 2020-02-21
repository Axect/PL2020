use crate::job::character::{Status, Character};
use crate::engine::command::{Target, Operation, Command};
use crate::engine::command::TargetPlayer::{Enemy, EnemyTemp, Own};
use crate::engine::command::TargetProp::{HP, ATK, DEF};
use crate::engine::command::Operation::{Minus, Plus};

#[derive(Debug, Copy, Clone)]
pub struct Warrior {
    pub stat: Status,
    pub exp: usize,
}

impl Default for Warrior {
    fn default() -> Self {
        Warrior { 
            stat: Status {
                hp: 10,
                mp: 0,
                atk: 3,
                def: 2,
                cri: 3,
                dex: 3,
            },
            exp: 0,
        }
    }
}

impl Character for Warrior {
    fn attack(&self, enemy: &Self) -> Command {
        let mut cmd: Command = Vec::new();
        cmd.push((Target::new(Enemy, HP), Minus(self.stat.atk)));
        cmd
    }

    fn defense(&self, enemy: &Self) -> Vec<(Target, Operation)> {
        let mut cmd: Command = Vec::new();
        cmd.push((Target::new(EnemyTemp(1), ATK), Minus(self.stat.def)));
        cmd
    }

    fn special_attack(&self, enemy: &Self) -> Vec<(Target, Operation)> {
        let mut cmd: Command = Vec::new();
        cmd.push((Target::new(Enemy, DEF), Minus(1)));
        cmd
    }

    fn special_defense(&self, enemy: &Self) -> Vec<(Target, Operation)> {
        let mut cmd: Command = Vec::new();
        cmd.push((Target::new(Own, DEF), Plus(1)));
        cmd
    }

    fn is_dead(&self) -> bool {
        self.stat.hp <= 0
    }
}