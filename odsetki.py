import json
import datetime
import os
import sys
from datetime import datetime
from datetime import date



def delete_percent(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line.replace('%', ''))
delete_percent('lombard.txt')

# case_number = windxxx[i][0]
# name = windxxx[i][1]
# date = windxxx[i][2]
# amount = windxxx[i][3]
# telephone = windxxx[i][4]


def interest(windxxx, lombard, nalezne):
    with open(windxxx, 'r') as f:
        windxxx = json.load(f)
    with open(lombard, 'r') as f:
        lombard = f.readlines()
        for i in range(len(lombard)):
            lombard[i] = lombard[i].split()
            lombard[i][0] = datetime.strptime(lombard[i][0], '%Y-%m-%d')
            lombard[i][1] = float(lombard[i][1])
    with open(nalezne, 'w') as f:
        nalezne = []
        for i in range(len(windxxx)):
            if windxxx[i][0] == '' or windxxx[i][1] == '' or windxxx[i][2] == '' or windxxx[i][3] == '' or windxxx[i][4] == '':
                continue
            else:
                if windxxx[i][0] == windxxx[i-1][0]:
                    if windxxx[i][2] > windxxx[i-1][2]:
                        windxxx[i] == windxxx[i-1]
                windxxx[i][2] = datetime.strptime(windxxx[i][2], '%Y-%m-%d')
                windxxx[i][3] = float(windxxx[i][3])
                dzis = datetime.today().strftime('%Y-%m-%d')
                dzis =  datetime.strptime(dzis,'%Y-%m-%d')
                wybrana_stopa = 0
                liczba_dni = 10000000000000
                for j in range(len(lombard)): 
                    mindni = (windxxx[i][2] - lombard[j][0]).days
                    if mindni < liczba_dni and mindni > 0:
                        liczba_dni = mindni
                        index = j
                
                naleznosc = round(lombard[index][1]/(365*100)*windxxx[i][3]*(dzis - windxxx[i][2]).days, 2)
                nalezne.append([windxxx[i][0], windxxx[i][1],windxxx[i][2].strftime('%Y-%m-%d'), windxxx[i][3], naleznosc])        
        json.dump(nalezne, f)

interest('wind030.json', 'lombard.txt', 'nalezne.json')
  