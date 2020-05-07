import pandas as pd 
import numpy as np 
import csv

def readfiles():

    list_temperatur = []
    with open('temp.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            list_temperatur.append(row)
    print(list_temperatur)

    list_sol = []
    with open('solskenstid.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            list_sol.append(row)
    print(list_sol)

    list_neder = []
    with open('nederbörd.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            list_neder.append(row)
    print(list_neder)


    return list_neder,list_sol,list_temperatur

def temperature(list_temperatur):

    years = mdates.YearLocator()   # every year
    months = mdates.MonthLocator()  # every month
    years_fmt = mdates.DateFormatter('%Y')

    # Load a numpy structured array from yahoo csv data with fields date, open,
    # close, volume, adj_close from the mpl-data/example directory.  This array
    # stores the date as an np.datetime64 with a day unit ('D') in the 'date'
    # column.
    with cbook.get_sample_data('temp.csv') as datafile:
        data = np.load(datafile)['price_data']

    fig, ax = plt.subplots()
    ax.plot('date', 'adj_close', data=data)

    # format the ticks
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(years_fmt)
    ax.xaxis.set_minor_locator(months)

    # round to nearest years.
    datemin = np.datetime64(data['date'][0], 'Y')
    datemax = np.datetime64(data['date'][-1], 'Y') + np.timedelta64(1, 'Y')
    ax.set_xlim(datemin, datemax)

    # format the coords message box
    ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax.format_ydata = lambda x: '$%1.2f' % x  # format the price.
    ax.grid(True)

    # rotates and right aligns the x


def sunshine(list_sol):



def rain(list_neder):





def main():
    readfiles()=list_neder,list_sol,list_temperatur
    answer = ""
    while answer != "5":
        str(input("what do you want to do?"))
        print("1. Show temperature graph")
        print("2. Show sunshine graph")
        print("3. Show rain graph")

        if answer == "1":
            temperature(list_temperatur)
        if answer == "2":
            temperature(list_temperatur)
        if answer == "3":
            temperature(list_temperatur)

main()


print("hello")


sdfghfd