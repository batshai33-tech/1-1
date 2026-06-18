menu = {
    "삼각김밥": 2000,
    "컵라면": 3000,
    "두바이 쫀득 아이스크림":12000,
    "의성마늘핫바":2500,
    "크림빵":1500
    }

money = 0
cart_money = 0
cart_items = []
def add_menu():
    global money
    global cart_money
    global cart_items
    print(f"소유중인 돈 : {money}")
    for name, money1 in menu.items():
        print(f"음식명 : {name} | 금액 : {money1}")

    while True:
        ans = input()

        if ans == "":
            break

        if ans not in menu.keys():
            print("없는 상품")
            continue

        menu_name = ""
        count = 0
        money2 = 0
        while ans != menu_name:
            if ans != list(menu.keys())[count]:
                count += 1
                continue
            else:
                menu_name = list(menu.keys())[count]
                money2 = list(menu.values())[count]
                break
        cart_money += money2
        cart_items.append(menu_name)
        print(f"{menu_name}을 추가했고 현재 : {cart_money}원이 카트 내에 있습니다.\n현재 잔액은 {money}원 입니다.")

def list_menu():
    if not cart_items:
        print("쇼핑 카트에 아무것도 없습니다.")
    else:
        for i in menu.keys():
            count1 = 0
            for j in cart_items:
                if i == j:
                    count1 += 1
            print(f"{i}는 {count1}개 있습니다.")

def delete_menu():
    global cart_money
    global cart_items
    for i in menu.keys():
        count1 = 0
        for j in cart_items:
            if i == j:
                count1 += 1
        print(f"{i}는 {count1}개 있습니다.")
    while True:
        print("삭제할 상품 입력 (종료는 엔터)")
        ans = input()
        if ans == "":
            break
        elif ans not in cart_items:
            print("없는 상품입니다.")
            continue
        else:
            cart_items.remove(ans)
            cart_money -= menu[ans]
            print(f"현재 바뀐 돈:{cart_money}원")




def main():
    global money
    global cart_money
    global cart_items
    print("편의점에 오신것을 환영합니다")
    while True:
       
        money = input("가지고 계신 돈을 입력해주세여:")
        try:
            money = int(money)
            break
        except ValueError:
            print("돈은 숫자형입니다!!!")

    print("안녕하세요~ 경소마고 편의점입니다~")
    while True:
        succese = False
        
        print("""1. 장바구니에 넣기
2. 장바구니 목록 보기
3. 장바구니에서 빼기
E. 종료는 엔터키""")

        ans = input()
        if ans in ["1", "장바구니에 넣기"]:
            add_menu()
        elif ans in ["2"]:
            list_menu()
        elif ans in ["3"]:
            delete_menu()
        elif ans == "":
            if money < cart_money:
                print("예산을 초과하여 구매하였습니다 조금 빼주세요ㅠㅠ")
            else:
                succese = True
        else:
            print("잘못된 입력") 
            continue

        if succese and cart_money >= 10000:
            print("축하드립니다! 10000원이상 구매했음으로 10% 할인입니다!")
            cart_money = cart_money * 0.9 
            print(f"당신이 구매한 총 메뉴들{cart_items}")
            print(f"총 가격!{cart_money}")
            print(f"남은잔액{money - cart_money}")
            print("감사합니다! 다음에 또 오세요!!")
            break
        elif succese:
            print(f"당신이 구매한 총 메뉴들{cart_items}")
            print(f"총 가격!{cart_money}")
            print(f"남은잔액{money - cart_money}")
            print("감사합니다! 다음에 또 오세요!!")
            break

if __name__ == "__main__":
    main()