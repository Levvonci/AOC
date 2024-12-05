import pandas as pd
 
df = pd.read_csv('Day1\df.txt', sep = '\s+', header=None)

colonna1 = df[0].tolist()  
colonna2 = df[1].tolist()  

colonna1.sort()
colonna2.sort()

sommaTot = 0

for item in (colonna1):
    Num_occorrenze = 0
    for i in range(len(colonna2)):
        if item == colonna2[i]:
            Num_occorrenze += 1
    sommaTot += item * Num_occorrenze

print(sommaTot)
        
        