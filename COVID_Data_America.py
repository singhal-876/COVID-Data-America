import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Fun():
    print(":)")
    print("#1. For checking the data.")
    print("#2. Reading complete file without index.")
    print("===================")
    print("Topic - Data Visualization")
    print(" ")
    print("#3. Line Chart")
    print("    Press 1 to print the data for COVID cases as per cities.")
    print("    Press 2 to print the data for Age<30 cases as per cities.")
    print("    Press 3 to print the data for Age>30 cases as per cities.")
    print("    Press 4 to print the data for Deaths cases as per cities.")
    print("    Press 5 to print All data.")
    print(" ")
    print("#4. Bar Graph")
    print("    Press 1 to print the data for COVID cases as per cities.")
    print("    Press 2 to print the data for Age<30 cases as per cities.")
    print("    Press 3 to print the data for Age>30 cases as per cities.")
    print("    Press 4 to print the data for Deaths cases as per cities.")
    print("    Press 5 to print the data in form of stack bar chart")
    print("    Press 6 to print the data in form of multi bar chart")
    print(" ")
    print("#5. Scatter Chart")
    print(" ")
    print("#6. For Exit")
    print("===============")


def Read_CSV():
    print("The Data")
    df=pd.read_csv('COVID_Data_America.csv')
    print(df)

def No_Index():
    print("Reading the file without index")
    df=pd.read_csv('COVID_Data_America.csv', index_col=0)
    print(df)


#FOR LINE CHART:)

def line_plot():
    df=pd.read_csv('COVID_Data_America.csv')
    df['cities'] = ['NY','ST','LA','CF','BY','DN','FL','AZ','PX','SD','CA','MN','SF','HT']
    cities=df["cities"]
    COVID=df["COVID"]
    Under_30=df["Age<30"]
    Above_30=df["Age>30"]
    Deaths=df["Deaths"]
    plt.xlabel("cities")

    
    YC = int(input("Enter the number representing your preferred line chart from the above choices: "))
    
    if YC == 1:
        plt.ylabel("COVID Cases")
        plt.title("cities Wise COVID Cases")
        plt.plot(cities, COVID, color='b')
        plt.show()
    elif YC == 2:
        plt.ylabel("Age<30 Cases")
        plt.title("cities Wise Age<30 Cases")
        plt.plot(cities, Under_30, color='g')
        plt.show()
    elif YC == 3:
        plt.ylabel("Age>30 Cases")
        plt.title("cities Wise Age>30 Cases")
        plt.plot(cities, Above_30, color='r')
        plt.show()
    elif YC == 4:
        plt.ylabel("Deaths Cases")
        plt.title("cities Wise Deaths Cases")
        plt.plot(cities, Deaths, color='c')
        plt.show()
    elif YC == 5:
        plt.ylabel("Number of cases")
        plt.plot(cities, COVID, color='b', label = "cities Wise COVID Cases")
        plt.plot(cities, Under_30, color='g', label = "cities Wise Age<30 Cases")
        plt.plot(cities, Above_30, color='r', label = "cities Wise Age>30 Cases")
        plt.plot(cities, Deaths, color='c', label = "cities Wise Deaths Cases")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")
        

#FOR BAR GRAPH:)

def bar_plot():
    df = pd.read_csv('COVID_Data_America.csv')
    df['cities'] = ['NY','ST','LA','CF','BY','DN','FL','AZ','PX','SD','CA','MN','SF','HT']
    cities = df["cities"]
    COVID = df["COVID"]
    Under_30 = df["Age<30"]
    Above_30 = df["Age>30"]
    Deaths = df["Deaths"]
    plt.xlabel("cities")


    YC = int(input("Enter the number representing your preferred bar graph from the above choices:"))
    
    if YC == 1:
        plt.ylabel("COVID Cases")
        plt.title("cities Wise COVID Cases")
        plt.bar(cities, COVID, color='b', width = 0.5)
        plt.show()
    elif YC == 2:
        plt.ylabel("Age<30 Cases")
        plt.title("cities Wise Age<30 Cases")
        plt.bar(cities, Under_30, color='g', width = 0.5)
        plt.show()
    elif YC == 3:
        plt.ylabel("Age>30 Cases")
        plt.title("cities Wise Age>30 Cases")
        plt.bar(cities, Above_30, color='r', width = 0.5)
        plt.show()
    elif YC == 4:
        plt.ylabel("Deaths Cases")
        plt.title("cities Wise Deaths Cases")
        plt.bar(cities, Deaths, color='c', width = 0.5)
        plt.show()
    elif YC == 5:
        plt.bar(cities, COVID, color='b', width = 0.5, label = "cities Wise COVID Cases")
        plt.bar(cities, Under_30, color='g', width = 0.5, label = "cities Wise Age<30 Cases")
        plt.bar(cities, Above_30, color='r', width = 0.5, label = "cities Wise Age>30 Cases")
        plt.bar(cities, Deaths, color='c',width = 0.5, label = "cities Wise Deaths Cases")
        plt.legend()
        plt.show()
    elif YC == 6:
        D=np.arange(len(cities))
        width=0.25
        plt.bar(D,COVID, width, color='b', label = "cities Wise COVID Cases")
        plt.bar(D+0.25, Under_30, width, color='g', label = "cities Wise Age<30 Cases")
        plt.bar(D+0.50, Above_30, width, color='r', label = "cities Wise Age>30 Cases")
        plt.bar(D+0.75, Deaths ,width, color='c', label = "cities Wise Deaths Cases")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")
        
def scatter_chart():
    df=pd.read_csv('COVID_Data_America.csv')
    df['cities'] = ['NY','ST','LA','CF','BY','DN','FL','AZ','PX','SD','CA','MN','SF','HT']
    cities = df["cities"]
    COVID = df["COVID"]
    Under_30 = df["Age<30"]
    Above_30 = df["Age>30"]
    Deaths = df["Deaths"]
    
    SC=plt.gca()
    SC=plt.scatter(cities, COVID, color="b", label="cities Wise COVID Cases")
    SC=plt.scatter(cities, Under_30, color="g", label="cities Wise Age<30 Cases")
    SC=plt.scatter(cities, Above_30, color="r", label="cities Wise Age>30 Cases")
    SC=plt.scatter(cities, Deaths, color="c", label="cities Wise Deaths Cases")
    
    plt.xlabel("cities")
    plt.title("Complete Scatter Chart")
    plt.legend()
    plt.show()
    
Fun()
YC = int(input("Enter Your Choice: "))

while YC == 1 or 2 or 3 or 4 or 5 or 6:

    if YC == 1:
        Read_CSV()
        break
    elif YC == 2:
        No_Index()
        break
    elif YC == 3:
        line_plot()
        break
    elif YC == 4:
        bar_plot()
        break
    elif YC == 5:
        scatter_chart()
        break
    elif YC == 6:
        print("Thank You for using...")
        break
    else:
        print("Enter valid input")
        break
