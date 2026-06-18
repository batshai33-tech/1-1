//ex
const express = require('express');
const { watch } = require('fs');
const app = express();
const fs = require('fs/promises');
const PORT = 3000;
const mysql = require('mysql2/promise');
const nunjucks = require('nunjucks');
// const { nunjucks } = require('nunjucks/browser/nunjucks-slim');

// 미들웨어 설정: HTTP 요청의 본문(body)에 있는 JSON 데이터를 파싱하기 위함(파싱은 번역을 뜻함)

app.use(express.json());
app.use(express.urlencoded({extended : true}));

//넌적스 환경설정시작
nunjucks.configure('views',{
    express : app,
    watch : true,
});
app.set('view engine', 'html')
//넌적스 환경설적 끝

// MySQL 커넥션 풀(Pool) 설정 (본인의 DB 정보로 변경 필요)

const pool = mysql.createPool({
host: 'localhost', //또는 127.0.0.1 호스트(방장)
user: 'root', // MySQL 사용자명
password: "1234", // MySQL 비밀번호
database: 'aaa', // 데이터베이스 이름
port: "3306",
waitForConnections: true,
connectionLimit: 10,
queueLimit: 0
});

// 임시 데이터베이스 (메모리 배열)

let users = [
{ id: 1, name: '홍길동', email: 'hong@example.com' },
{ id: 2, name: '이순신', email: 'lee@example.com' }
];

//post --> insert 행넣기

//get -> req.query
//post 방식 -> req.body

app.use(express.urlencoded({extends:true}))
// from 태그 안에 들어오는 내용 파싱(번역) 하기위한 미들웨어

app.get("/", async function  (req, res){
    try{
        const [rows] = await pool.query("select * from users");
        res.render('main', {users: rows});
    }catch(e){
        console.log("e" + e);
        res.send("서버가 잘못됬어");
    }
})
app.post('/adduser', async (req, res) => {
        console.log("req.body");
        console.log(req.body);
        const {name,email} = req.body;
        try{
            await pool.query(`insert into users (name,email) values(?,?)`,[name,email])
            res.send("성공적으로 행 데이터를 넣었네? 너 받볻먿청이가 아니구나!?")
        }catch(e){
            console.log(e);
            res.send("error났어 뭐가 이상해");
        }
    })


    app.post('/deluser', async (req, res) => {
        res.send("delUser");
        console.log(req.body);
        const {id} = req.body;
        console.log(`id = ${id}`)
        try{
            await pool.query(`delete from users where id=?`,[id])
            res.send("내가 아끼던 데이터였는데 ㅠㅠㅠㅠㅠ그래도 잘 삭제했어")
        }catch(e){
           console.log(e);
            res.send("삭제 도중에 뭐가 잘못됬잖아!!!!!!!이 받볻멍청아");
        }
    })

    app.post('/upduser', async (req, res) => {
        res.send("updUser");
        console.log(req.body);
        const {id, name, email} = req.body;
        console.log(`id = ${id} name = ${name} email = ${email}`)
        try{
            await pool.query(`UPDATE users SET name=?,email=? Where id=?`,[name, email, id])
        }catch(e){
           console.log(e);
        }
    })



app.get("/", (req,res)=>{
    res.send("<div><h1>받볻멍청이 ㅋ</h1></div>");
});

app.get("/bb", (req,res)=>{
    console.log(__dirname);
    res.sendFile(__dirname+'/bb.html');
});


app.get("/aa", async (req,res)=>{
    try{
        const data = await fs.readFile('aa.html');
        res.send(data)
    }catch(e){
        console.log(e);
        res.send("<div><h1>이 받볻멍청아 aa 페이지에서 에러났잖아</h1></div>"+e);
    }
});


//get 
app.get("/users", async (req,res) => {
    //console.log("test 누가 요청 왔음");
    //console.log(req.url,req.ip);
    //res.json(users);
    try{
        const [rows,columns] = await pool.query("SELECT * FROM users");
        console.log(rows);
        res.json(rows);
    }catch(e){
        console.log(e);
        res.send("망했다요!!!");
    }
    
});

app.post("/deluser",async(req,res) => {
    try{

    req.body.id
     await pool.query('delete From users where id = ?',[id]);
     res.send("내가 아끼던 데이터였는데 ㅠㅠㅠㅠㅠ그래도 잘 삭제했어")
    }catch(e){
        console.log(e)
        res.send("삭제 도중에 뭐가 잘못됬잖아!!!!!!!이 받볻멍청아")
    }
    })
//실행
app.listen(PORT , () => {
    console.log(`서버가 http://localhost:${PORT} 에서 실행중입니다.`);
});