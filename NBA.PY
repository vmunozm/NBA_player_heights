import json
import requests
from requests.models import Response
import pandas as pd

def NBA_PLAYERS():
    response = requests.get("https://mach-eight.uc.r.appspot.com/")
    json_object=json.loads(str((response.text)))

    List_1=json_object['values']
    data=pd.DataFrame(List_1)
    data_list=data.values.tolist()
    Players_up=[]

    def data_selection(Number):
    
        for i in range(0,len(data_list)):
            if int(data_list[i][1])>Number:
                Players_up.append(data_list[i][0]+' '+ data_list[i][3])    
            else:
                b=0

    def element_found(list):
        if len(list) == 0:
            print ("Match no Found")
        else: 
            print("Players Names are: ", list)

    while True:
        try:
            User_number=int(input("Enter the value by which you want to search : "))
        except ValueError:
            print("you should type an integer number")
            continue
        if User_number < 0:
            print("you should type a positive integer number")
            continue
        else:
            data_selection(User_number)
            element_found(Players_up)
            break
NBA_PLAYERS()




