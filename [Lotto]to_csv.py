import random
import csv

def LottoPick():
    LottoNumList = []
    for i in range(int(input("몇 게임을 진행하시겠습니까?"))):
        while True:
            LottoNumber = sorted(random.sample(range(1,46), 6))
            SumNumber = 0
            for i in LottoNumber:
                SumNumber += i
            if 100 <= SumNumber <= 170:
                print(LottoNumber)
                LottoNumList.append(LottoNumber)
                break
    with open('lotto.csv', 'w', newline='') as csvfile:
        LottoCsvWriter = csv.writer(csvfile, delimiter='\n')
        LottoCsvWriter.writerow(LottoNumList)

LottoPick()
