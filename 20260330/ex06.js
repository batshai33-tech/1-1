function aa(pp){
    console.log(pp); //함수 펑션을 출력
    pp(); //함수 펑션안에 콘솔로그 cc를 출력
}

const bb = (ww) => {
    console.log(ww);
}
// function = =>

aa(function cc(){console.log('cc')});
bb(()=>{console.log('bb')});