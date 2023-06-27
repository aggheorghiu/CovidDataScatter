import matplotlib.pyplot as plt
from io import StringIO
from csv import DictReader
from requests import get

def create_scatter_plot(num_rows):
    data = {'Cases': [], 'Population over 75 years': []}
    for i, row in enumerate(constructItLines()):
        if i >= num_rows:
            break
        data['Cases'].append(int(row['confirmados_1']))
        data['Population over 75 years'].append(int(row['population_85_mais']))
    median = find_median(data)
    print(median)
    plt.scatter(data['Cases'], data['Population over 75 years'])
    plt.xlabel('Number of confirmed cases')
    plt.ylabel('Population over 75 years')
    plt.title('COVID-19 cases vs population over 75 years')
    plt.show()



def create_bar_chart(num_rows):
    data = {'concelho': [], 'Cases': []}
    for i, row in enumerate(constructItLines()):
        if i >= num_rows:
            break
        data['concelho'].append(int(row['concelho']))
        data['Cases'].append(int(row['confirmados_1']))
    # median = find_median(data)
    # print(median)
    plt.bar(data['concelho'], data['Cases'])

    plt.show()

def constructItLines():
    url = "https://raw.githubusercontent.com/dssg-pt/covid19pt-data/master/data_concelhos_new.csv"
    req = get(url, stream=True)
    buffer = StringIO(req.text)
    return DictReader(buffer, delimiter=",")


def find_median(data):
    cases = data['Cases']
    n = len(cases)
    # Insert sort
    sorted_cases = []
    for i in range(n):
        sorted_cases.append(cases[i])
        j = i
        while j > 0 and cases[j] < sorted_cases[j - 1]:
            sorted_cases[j], sorted_cases[j - 1] = sorted_cases[j - 1], sorted_cases[j]
            j -= 1
        sorted_cases.insert(j, cases[i])
    # Find the median value
    if n % 2 == 0:
        median = (sorted_cases[n // 2] + sorted_cases[n // 2 - 1]) / 2
    else:
        median = sorted_cases[n // 2]
    return median


