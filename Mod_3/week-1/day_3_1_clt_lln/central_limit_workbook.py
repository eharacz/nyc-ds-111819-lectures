import numpy as np
import matplotlib as mp
import seaborn as sns
import pandas as pd
from statistics import mean

#1

x = np.random.binomial(100,.5, 1000)
print(x)

df = pd.DataFrame(x, columns=['number'])
print(df)
df.plot(kind='hist')

#2

def dice_roller(dice,attempts):
    list= []
    for attempt in range(attempts):
        d_count=0
        for d in range(dice):
            d_count=d_count+np.random.randint(1,7)
        list.append(d_count)
    return list

roll1=pd.DataFrame(dice_roller(2,100))
roll2=pd.DataFrame(dice_roller(3,100))
roll3=pd.DataFrame(dice_roller(4,100))

print(roll1)
print(roll2)
print(roll3)

roll1.plot(kind='hist')

roll2.plot(kind='hist')

roll3.plot(kind='hist')

def big_dice_roller(num_dice, samp_num):
    mean_list =[]
    for samp in range(samp_num):
        x = dice_roller(num_dice, 100)
        mean_list.append(mean(x))
    return mean_list

drollmean1=(big_dice_roller(2,100))
df1 =pd.DataFrame(drollmean1)

df1.plot(kind='hist')


drollmean2=(big_dice_roller(3,100))
df2 =pd.DataFrame(drollmean2)

df2.plot(kind='hist')

drollmean3=(big_dice_roller(4,100))
df3 =pd.DataFrame(drollmean3)

df3.plot(kind='hist')
