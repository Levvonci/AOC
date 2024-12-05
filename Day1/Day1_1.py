import pandas as pd
 
df = pd.read_csv('Day1\df.txt', sep = '\s+', header=None)


colonna1 = df[0].tolist()  
colonna2 = df[1].tolist()  

colonna1.sort()
colonna2.sort()

acc = 0

for i in range(len(colonna1)):
    acc += abs(colonna1[i] - colonna2[i])

print(acc)
    
