const user = {
    id:"김범규",
    pw:"1234",
    name_1:"your face",
    age:20
}

// const { id, pw, name_1, age } = user;

//const id = user.id;
//const pw = user.pw;
//const name_1 = user.name_1;
//const age = user.age;

function aa({id, pw, name_1, age}){
    console.log(id);
    console.log(pw);
    console.log(name_1);
    console.log(age);
}

aa(user);