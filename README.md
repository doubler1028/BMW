import random

money_me = 100
money_enemy = 100

while money_me > 0 and money_enemy > 0:
    print("\n===== 새로운 라운드 시작 =====")
    
    my_card = random.randint(1, 10)
    enemy_card = random.randint(1, 10)
    
    print(f"당신의 카드: {my_card}")
    
    # 베팅 시작
    bet = int(input("베팅 금액을 입력하세요 (0 = 체크): "))

    # 내가 베팅하면 상대의 반응 (랜덤)
    if bet > 0:
        # 상대가 콜 또는 다이 결정
        enemy_action = random.choice(["call", "fold"])
        print(f"상대 행동: {enemy_action}")

        if enemy_action == "fold":
            print("상대가 다이했습니다! 당신 승리!")
            money_me += bet
            money_enemy -= bet
            continue
        else:
            print("상대가 콜했습니다!")
    
    else:
        print("당신은 체크했습니다.")
        enemy_action = random.choice(["check", "bet"])

        if enemy_action == "bet":
            enemy_bet = random.randint(5, 20)
            print(f"상대가 {enemy_bet} 을(를) 베팅했습니다.")
            choice = input("콜 하려면 c, 다이하려면 f 입력: ")

            if choice == "f":
                print("당신이 다이했습니다!")
                money_me -= enemy_bet
                money_enemy += enemy_bet
                continue
            else:
                bet = enemy_bet
                print("콜했습니다!")

        else:
            print("상대도 체크했습니다.")
            bet = 0

    # 결과 공개
    print(f"당신 카드: {my_card} | 상대 카드: {enemy_card}")

    if my_card > enemy_card:
        print("당신이 승리했습니다!")
        money_me += bet
        money_enemy -= bet
    elif my_card < enemy_card:
        print("상대가 승리했습니다!")
        money_me -= bet
        money_enemy += bet
    else:
        print("무승부 (베팅 금액 변동 없음).")

    print(f"현재 소지금 → 나: {money_me} | 상대: {money_enemy}")

print("\n===== 게임 종료 =====")
if money_me > money_enemy:
    print("최종 승리!")
else:
    print("패배했습니다...")

