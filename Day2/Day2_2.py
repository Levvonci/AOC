def Verifica_Report(report):
    Livelli = list(map(int, report.split()))
    n = len(Livelli)
    
    
    def Verifica_Livello(Livelli):
        crescente = all(1 <= Livelli[i+1] - Livelli[i] <= 3 
                         for i in range(len(Livelli) - 1))
        decrescente = all(1 <= Livelli[i] - Livelli[i+1] <= 3 
                         for i in range(len(Livelli) - 1))
        return crescente or decrescente
    
    if Verifica_Livello(Livelli):
        return True
    for i in range(n):
        NuovoLivello = Livelli[:i] + Livelli[i+1:]
        if Verifica_Livello(NuovoLivello):
            return True
    
    return False

def Conta_Report(reports):
    return sum(Verifica_Report(report) 
               for report in reports)

def Leggi(input):
    with open(input, 'r') as file:
        reports = file.readlines()
    return [report.strip() 
            for report in reports]

input = 'Day2/input.txt'
reports = Leggi(input)
print(Conta_Report(reports))
