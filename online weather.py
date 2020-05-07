import pandas as pd 
import numpy as np 
import csv
import plotly.express as px

hallå
# def read_temp():

#     list_temperature = []
#     with open('temp.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             list_temperature.append(row)
#     print(list_temperature)
#     return list_temperature

# def read_sunshine():

#     list_sunshine = []
#     with open('solskenstid.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             list_sunshine.append(row)
#     print(list_sunshine)
#     return list_sunshine

# def read_rain():
#     list_rain = []
#     with open('nederbörd.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             list_rain.append(row)
#     print(list_rain)
#     return list_rain



    

def temperature(temp):

    # temp_data = []
    # for i in range(0,len(temp)):
    #     temp_data.append(temp[i][2])
    # temp_date = []
    # for i in range(0,len(temp)):
    #     temp_date.append(temp[i][0])
    df = pd.read_csv(temp, sep=";")
    fig = px.line(df, x="Datum", y="Lufttemperatur", title='Temperature over time')
    fig.show()
    print(df)


# def sunshine(list_sunshine):



# def rain(list_rain):





# def main():
#     readfiles()=list_rain,list_sunshine,list_temperature
#     answer = ""
#     while answer != "5":
#         str(input("what do you want to do?"))
#         print("1. Show temperature graph")
#         print("2. Show sunshine graph")
#         print("3. Show rain graph")

#         if answer == "1":
#             temperature(list_temperature)
#         if answer == "2":
#             temperature(list_temperature)
#         if answer == "3":
#             temperature(list_temperature)

# main()


# print("hello")


# sdfghfd
temperature("temp1.csv")
