from sys import argv
import messages
from time import time

# Recebe um horário em hh:mm e retorna o valor em minutos após às 00:00
def hhmm_to_minutes(time: str):
    hh, mm = time.split(':')
    return int(hh)*60 + int(mm)

# Recebe o caminho para um arquivo txt com formato:
# Cada linha é composta por:<horario_de_entrada> <horario_de_saida>
class MinimumPlatforms:
    def __init__(self, file='./tests/test_0.txt'):
        self.arrivals = []
        self.departures = []
        self.n = 0

        with open(file) as file:
            buses_schedules = file.readlines()

            for bus_schedule in buses_schedules:
                arrival_hhmm, departure_hhmm = bus_schedule.split()

                arrival = hhmm_to_minutes(arrival_hhmm)
                departure = hhmm_to_minutes(departure_hhmm)

                self.arrivals.append(arrival)
                self.departures.append(departure)
                self.n+=1

        

    def solve(self):
        arrivals = sorted(self.arrivals)
        departures = sorted(self.departures)
        platforms = 0
        i, j = 0, 0

        while(i < self.n and j < self.n):
            if (arrivals[i] <= departures[j]):
                platforms+=1
                i+=1
            else:
                platforms-=1
                j+=1
        
        return platforms

    def __str__(self):
        start = time()
        solution = self.solve()
        duration = time() - start
        duration = round(duration, 4)
        n = len(self.arrivals)
        inputs = [(self.arrivals[i], self.departures[i]) for i in range(n)]
        inputs_str = ''
        for inp in inputs:
            inputs_str += f'{inp}\n'
        
        return messages.show_results(inputs_str, solution, duration)



# EXECUÇÃO
if __name__ == '__main__':
    args = len(argv[1:])
    

    if (args == 1):
        if argv[1] == '-a' or argv[1] == '--all':
            messages.show_solution_title()
            for i in range(6):
                mp = MinimumPlatforms(f'./tests/test_{i}.txt')
                print(mp)
            
        elif argv[1] == '-h' or argv[1] == '--help':
            messages.show_help()
    
        else:
            try:
                FILE_PATH = argv[1]
                mp = MinimumPlatforms(FILE_PATH)
                print(mp)
                
            except FileNotFoundError:
                print('Erro: Arquivo não encontrado.')

            except:
                print('Formatação de arquivo inválida. Para mais informações, use --help ou -h.')

    elif (args == 0):
        mp = MinimumPlatforms()
        print(mp)
    else:
        messages.show_exced_arguments_error(args)


