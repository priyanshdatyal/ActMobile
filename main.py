from itertools import count
import json
from unittest import result

def getData():
    data = json.load(open("data/input_ios.json","r"))["sales"]
    for item in data:
        countries.add(item["country"])
        refined_data[item['country']+"_"+item["prod"]]=0
    setTotal(data,refined_data)

def setTotal(data,refined_data):
    for item in data:
        refined_data[item['country']+"_"+item["prod"]]=item["price"]+refined_data[item['country']+"_"+item["prod"]]
    

def getMaxCity():
    getData()
    result="Wrong Choice of product"
    print(countries)
    max=0
    for items in countries:
        if (  refined_data[items+"_"+product] > max):
            max=refined_data[items+"_"+product]
            result = items
    
    return result

        


if __name__ == "__main__" :
    data={}
    refined_data={}
    countries=set()
    product = input("Enter the product : ")
    print(getMaxCity())