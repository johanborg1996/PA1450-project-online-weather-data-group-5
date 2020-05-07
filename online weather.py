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



def sunshine(list_sol):
    "blabl"



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