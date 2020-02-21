pub fn damage_calc(dam: usize, def: usize) -> usize {
    if dam > def { dam - def } else { 0 }
}