from itertools import product

import random 

print("誰に賭けますか？")

who = input()


print("いくら賭けますか？")

money = input()



Tp_num =[1,2,3,4,5,6,7,8,9,10,10,10,10]

JQK_list=["J","Q","K"]

Tp_mark = ["♣","♦","♥","♠"]

numA = 1

numJQK = 10

card_list = list(product(Tp_num,Tp_mark))


player_card = random.shuffle(card_list)

for i in range(2):
    player_card = []
    p_total = 0
p = []
#1人目
for i in range(0,2):
    player_card.append(card_list.pop(0))
    if player_card[i][0] == "A":
        p.append(numA)
    elif player_card[i][0] in JQK_list:
        p.append(numJQK)
    else:
        p.append(int(player_card[i][0]))
print(player_card)
print(p)
print(sum(p))
#2人目
for i in range(2):
    banker_card = []
b = []
for i in range(0,2):
    banker_card.append(card_list.pop(0))
    if banker_card[i][0] == "A":
        b.append(numA)
    elif banker_card[i][0] in JQK_list:
        b.append(numJQK)
    else:
        b.append(int(banker_card[i][0]))
print(banker_card)
print(b)
print(sum(b))


sump = str(sum(p))

sumb = str(sum(b))

player = sump[-1:]

banker = sumb[-1:]


if 8 <= int(player)<= 9 or 8 <= int(banker) <= 9:
    pass
elif 0<= int(player) <= 6:
    random.choice(player_card)
    player_card.append(card_list.pop(0))
    if player_card[2][0] == "A":
        p.append(numA)
    elif player_card[2][0] in JQK_list:
        p.append(numJQK)
    else:
        p.append(player_card[2][0])

    print(player_card)
    print(p)
    print(sum(p))
    
    if 0<= int(banker) < 3:
        random.choice(banker_card)
        banker_card.append(card_list.pop(0))
        if banker_card[2][0] == "A":
            b.append(numA)
        elif banker_card[2][0] in JQK_list:
            b.append(numJQK)
        else:
            b.append(banker_card[2][0])
    elif 0 <= int(player) < 8:
        random.choice(banker_card)
        banker_card.append(card_list.pop(0))
        if banker_card[2][0] == "A":
            b.append(numA)
        elif banker_card[2][0] in JQK_list:
            b.append(numJQK)
        else:
            b.append(banker_card[2][0])
    elif 1 <= int(player) < 8:
        random.choice(banker_card)
        banker_card.append(card_list.pop(0))
        if banker_card[2][0] == "A":
            b.append(numA)
        elif banker_card[2][0] in JQK_list:
            b.append(numJQK)
        else:
            b.append(banker_card[2][0])
    elif 3 <= int(player) < 8:
        random.choice(banker_card)
        banker_card.append(card_list.pop(0))
        if banker_card[2][0] == "A":
            b.append(numA)
        elif banker_card[2][0] in JQK_list:
            b.append(numJQK)
        else:
            b.append(banker_card[2][0])
    elif 6 <= int(player) <= 8:
     if len(p) == 2 and int(banker) <= 6:
        random.choice(banker_card)
        banker_card.append(card_list.pop(0))
        if banker_card[2][0] == "A":
              b.append(numA)
        elif banker_card[2][0] in JQK_list:
            b.append(numJQK)
        else:
            b.append(int(banker_card[1][0]))
    print(banker_card)
    print(b)
    print(sum(b))

sump = str(sum(p))

sumb = str(sum(b))

player = sump[-1:]

banker = sumb[-1:]



print("プレイヤー" + player)

print("バンカー" + banker )

if int(player) >= 8 and  int(banker)<= 8:
    if int(player) == 8 or 9:
        print("プレイヤーの勝ち")
        if who == "プレイヤー":
            print("おめでとう!あなたは" + str(int(money)*2) +"円の賞金を手に入れました。")
        elif who == "バンカー":
            print("残念！賞金は手に入れられませんでした。")
elif int(player) <= 8 and int(banker) >= 8:
    if int(banker) == 8 or 9:
            print("バンカーの勝ち")
            if who == "バンカー":
                print("おめでとう！あなたは" + str(int(money)*1.95) + "円の賞金を手に入れました。")
            elif who == "プレイヤー":
                print("残念！賞金は手に入れられませんでした。")
elif int(player) == int(banker):
    print("タイ")
    if who == "バンカー" and "プレイヤー":
         print("あなたは" + str(int(money)* 9) + "円の賞金を手に入れました。")
elif int(player) >= int(banker):
    print("あなたは" + str(int(money)*2) + "円の賞金を手に入れました。") 
elif int(banker)  >= int(player):
    print("あなたは" + str(int(money)*1.95) + "円の賞金を手に入れました。")
