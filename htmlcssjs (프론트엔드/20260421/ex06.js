const id ="아이디"
const pw ="비밀번호"

const person = {
    id,
    pw,
    name: "김범규",
    age: 17,
    phone: "010-3680-5216"
}

console.log(person);
for (const key in person) {
    const element = person[key];
    console.log(`key ${key} element ${element}`)
}