import random

int_amount = 100
capital = 25000
rounds = 20
sim_no = 100000
gameover = 0
earning = 0

for j in range(sim_no):
    total = capital
    bet = int_amount
    #print("Processing Simulation #%d:"%j)
    for i in range(1,rounds+1):
        #print("Round %d:"% i)
        if bet > total:
            #print("BET HAS EXCEED THE TOTAL. GAME OVER.")
            gameover += 1
            total = 0
            break
        if random.random() <= 0.4861:
            total += bet
            #print("Won. Bet = %d, Total = %d"% (bet,total))
            bet = int_amount
        else:
            total -= bet
            #print("Lose. Bet = %d, Total = %d" % (bet, total))
            bet = bet * 2
    if (total - capital) > earning:
        earning = (total - capital)

print("Best earning: %d"% earning)
print("Gameover Count: %d"% gameover)
print("Fail prob: %f"%(gameover/sim_no))