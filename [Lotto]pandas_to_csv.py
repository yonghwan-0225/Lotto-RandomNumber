import pandas as pd
import random

Game_Count = int(input("몇 게임을 진행하시겠습니까?"))
LottoNumList = []

for i in range(0, Game_Count):
    while True:
        data = random.sample(range(1,46), 6)
        SumNumber = 0
        for i in data:
            SumNumber += i
        if 100 <= SumNumber <= 170:
            print(data)
            LottoNumList.append(data)
            break
        df = pd.DataFrame(LottoNumList)
        df.to_csv('lotto_pd.csv')
