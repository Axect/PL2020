use crate::engine::command::{Command, Target};
use crate::job::character::Character;

pub fn exec<T: Character, S: Character>(cmd: &Command, own: &mut T, enemy: &mut S) {
    for (target, op) in cmd {
        let mut prop = match target {
            Target { player: Own,  prop } => {
                own.get_mut_prop(prop)
            },
            Target { player: Enemy, prop } => {
                enemy.get_mut_prop(prop)
            }
        };
    }
}