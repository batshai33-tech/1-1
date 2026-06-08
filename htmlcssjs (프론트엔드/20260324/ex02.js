const num = 5;
// 넘이 5이면 25를 출력
// 넘 이 10이면 101을 출력
// 넘이 15이면 201을 출력

switch (num) {
    case 5:
        console.log('25');
        break; 
    case 10:
        console.log('101');
        break;
    case 15:
        console.log('201');
        break;
    default:
        console.log('잘못된 숫자입니다 5, 10, 15 중 하나를 입력하세요');
        break;
}