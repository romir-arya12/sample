import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv 

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()
#fig=ff.create_distplot([data],["math score"],show_hist=False)
#fig.show()
mean=statistics.mean(data)
stdev=statistics.stdev(data)
print(mean)
print(stdev)
def randomSetOfMean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
mean_list=[]
for i in range(0,1000):
    SetOfMean=randomSetOfMean(100)
    mean_list.append(SetOfMean)
stdev=statistics.stdev(mean_list)
mean=statistics.mean(mean_list)
print("this is the standared devation")
print(stdev)
print(mean)
fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="mean"))
fig.show()
first_std_deviation_start, first_std_deviation_end = mean-stdev, mean+stdev
second_std_deviation_start, second_std_deviation_end = mean-(2*stdev), mean+(2*stdev)
third_std_deviation_start, third_std_deviation_end = mean-(3*stdev), mean+(3*stdev)

df=pd.read_csv("data1.csv")
data=df["Math_score"].tolist()
meanofsample1=statistics.mean(data)
fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meanofsample1,meanofsample1],y=[0,0.17],mode="lines",name="meanofsample"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="stdev1"))
fig.show()

df=pd.read_csv("data2.csv")
data=df["Math_score"].tolist()
meanofsample2=statistics.mean(data)
fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meanofsample2,meanofsample2],y=[0,0.17],mode="lines",name="meanofsample"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="stdev1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="stdev2"))
fig.show()

df=pd.read_csv("data3.csv")
data=df["Math_score"].tolist()
meanofsample3=statistics.mean(data)
fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meanofsample3,meanofsample3],y=[0,0.17],mode="lines",name="meanofsample"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="stdev1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="stdev2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="stdev3"))
fig.show()

z_score=(meanofsample3-mean)/stdev
print(z_score)
x_score=(meanofsample2-mean)/stdev
print(x_score)
y_score=(meanofsample1-mean)/stdev
print(y_score)