import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        temperature = []
        iceCream = []

        for x in df:
            temperature.append(float(x["Temperature"]))
            iceCream.append(float(x["\tIce-cream Sales(₹)"]))
            print(iceCream)
    
    return {"x" : temperature, "y" : iceCream}

def findCorrelation(dataSource):
    print(dataSource)
    corrEf = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Corrleation between temperature and ice crem sales is ", corrEf[0,1])

def plotFigure(data_path):
    fig = px.scatter(data_path, x = "Temperature", y = "\tIce-cream Sales(₹)")
    fig.show()

def setUp():
    data_path = "TempIce.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setUp()