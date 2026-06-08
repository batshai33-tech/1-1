const unit = {
    0:'0입니다',
    name:"현재",
    attack : function(weapon) {
        return `${weapon}으로 공격한다`;
    }
}

console.log(unit.attack("주먹"));
console.log(unit.attack("선생님"));

console.log(unit.name);
console.log(unit['name'])
// console.log(unit.0)