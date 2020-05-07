import pandas as pd 
import numpy as np 
import csv
import plotly.express as px
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
    df = pd.read_csv(temp, sep=";")
    # fig = px.line(df, x="Datum", y="Lufttemperatur", title='Temperature over time')
    # fig.show()
    df = df.set_index("Datum")
    z = df.index.get_loc("2020-01-10")
    print(z.start)

def interval_temp(temp):
    #exempel på datum: 2020-12-28
    df = pd.read_csv(temp, sep=";")
    df = df.set_index("Datum")
    interval1 = input("Enter the first date: ")
    interval2 = input ("Enter the second date: ")
    df = df.loc[interval1:interval2, :]
    df = df.reset_index()
    fig = px.line(df, x="Datum", y="Lufttemperatur", title='Temperature over time')
    fig.show()


def interval_hour(temp, hours):
    #Gör om valt värde till ett index som sedan adderas med antal timmar eller hours, som user väljer själv. Dessa görs sedan om igen till ett värde utifrån indexet och man får en ny range.
    df = pd.read_csv(temp, sep=";") #df = dataframe
    df1 = df.set_index("Datum")
    interval1 = input("Enter the first date: ") # 2020-01-10 
    slice_start = int(df1.index.get_loc(interval1).start) #2020-01-10 = i(285) 285, 310 == slice_start = int(285)
    df1 = df1.iloc[slice_start:(slice_start + hours), :] #om du ger interger värde så får du fram ett värde på det indexet. ":" = interval. Till 285 + 48
    df1 = df1.reset_index()
    new_df = pd.DataFrame(df1["Lufttemperatur"])
    fig = px.line(new_df, x = new_df.index, y="Lufttemperatur", title="Interval between " + interval1 + " to " + str(df.iloc[(slice_start+hours)][0]) , labels={"index":"Hours"})
    fig.show()


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


# temperature("temp1.csv")
# interval_temp("temp.csv")
interval_hour("temp.csv", 48)


#### blabla = index ????
#### search blabla == index
#### index + 48 == intervall på 48h
