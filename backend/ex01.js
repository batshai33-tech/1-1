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

app.get("/", async function (req, res) {

    try {

        const [rows] = await pool.query('select * from tb_snack');
        console.log(rows);
        res.render('snack_list',{snacks:rows});

    } catch (e) {
        res.send("오류로인해 황지한이 간식으로 나왔습니다" + e);
    }
})


app.listen(PORT , () => {
    console.log(`서버가 http://localhost:${PORT} 에서 실행중입니다.`);
});