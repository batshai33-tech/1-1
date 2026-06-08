const express = require('express');
const app = express();
const fs = require('fs/promises');
const PORT = 3000;
const mysql = require('mysql2/promise');

// 미들웨어 설정: HTTP 요청의 본문(body)에 있는 JSON 데이터를 파싱하기 위함(파싱은 번역을 뜻함)

app.use(express.json());

// MySQL 커넥션 풀(Pool) 설정 (본인의 DB 정보로 변경 필요)

const pool = mysql.createPool({
host: 'localhost', //또는 127.0.0.1
user: 'root', // MySQL 사용자명
password: "1234", // MySQL 비밀번호
database: 'gbsw1-1', // 데이터베이스 이름
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

app.post('/adduser', (req, res) => {
        console.log("req.body");
        console.log(req.body);
        res.status(200).json({"msg":"success"});
    });



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

//실행
app.listen(PORT , () => {
    console.log(`서버가 http://localhost:${PORT} 에서 실행중입니다.`);
});