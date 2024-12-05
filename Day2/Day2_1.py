def report_safe(report):
    livelli = list(map(int, report.split()))

    for i in range(1, len(livelli)):
        differenza = abs(livelli[i] - livelli[i - 1])
        if differenza < 1 or differenza > 3:
            return False;
    
    crescente = all(livelli[i] < livelli[i + 1]
                    for i in range(len(livelli) - 1))
    decrescente = all(livelli[i] > livelli[i + 1]
                    for i in range(len(livelli) - 1))
    
    return crescente or decrescente

def conta_safe(input):
    count = 0
    with open(input, 'r') as file:
        for linea in file:
            report = linea.strip()
            if report_safe(report):
                count += 1
    return count    

def safe_rimozione(report):
    livelli = list(map(int, report.split()))
    for i in range(len(livelli)):
        report2 = livelli[:i] + livelli[i + 1:]
        if conta_safe(report2):
            return True
    return False  

input = "C:\\Users\\Administrator\\Documents\\Vs\\AOC\\Day2\\input.txt"
Risultato = conta_safe(input) 
print(Risultato)
