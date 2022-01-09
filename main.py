import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from fadingAll import fading_all
from micro_cluster import MicroCluster
from mergeClusters import merge_clusters

from sostream import SOStream
import pathlib
import csv
#import time
#import datetime
#manipulating time
from time import process_time
t1_start = process_time()

#manipulating the place that the file of data set is in our computer first way
home = pathlib.Path.home() / "DOC" / "Dataset_1 .csv"
home2 = pathlib.Path.home() / "DOC" / "Dataset_2 .csv"

DataSet1 = []
with home.open(mode="r", encoding="utf-8") as file:
  reader = csv.reader(file)
  #print(reader)
  for row in reader:
      #print(row)
      DataSet1.append(row)
#print(type(DataSet1),DataSet1)
DataSet1 = np.array(DataSet1)

#second way of reading data set to a numpyarray
data_df1 = pd.read_csv('Dataset_1 .csv')
data_df2 = pd.read_csv('Dataset_2 .csv')
#data_df2 = pd.DataFrame(DataSet1)
#print(data_df1.values)
#print(data_df2)
#print(DataSet1)

#we can run the clustering by second data set but it takes lot of time if we want to cluster second data set is as easy as write
#data_df2 in place of data_df1 in below lines or uncomment its section in some lines below


#making object out of sos tream
sostream_clustering = SOStream(alpha = 0, minPts = 3, merge_threshold = 47000)
# using fade_all is optional and unnecessary

#ax = plt.axes(projection="3d")

#this loop call the sos tream for each data(we can assume stream of data) and for each of that make a plot both 3d & 2d  but when you see
#this code maybe some of that be commented beacus of timing and some ram limits
for r in data_df1.values:
    #print(r)
    sostream_clustering.process(r)
    # 3d plotting
    plt.figure()
    ax = plt.axes(projection="3d")
    a = np.array([c.centroid for c in sostream_clustering.M[-1]])
    ax.scatter3D(a[:, 0], a[:, 1], a[:, 2], color="green")
    plt.show()
    # 2d plotting
    #plt.figure()
    #data_df1.plot.scatter(x=0, y=1)
    #a = np.array([c.centroid for c in sostream_clustering.M[-1]])
    #plt.scatter(a[:, 0], a[:, 1], color='blue')
    #plt.show()
#plt.show()


#for r in data_df2.values:
    #print(r)
    #sostream_clustering.process(r)
    # 3d plotting
    #plt.figure()
    #ax = plt.axes(projection="3d")
    #a = np.array([c.centroid for c in sostream_clustering.M[-1]])
    #ax.scatter3D(a[:, 0], a[:, 1], a[:, 2], color="green")
    #plt.show()
    # 2d plotting
    #plt.figure()
    #data_df1.plot.scatter(x=0, y=1)
    #a = np.array([c.centroid for c in sostream_clustering.M[-1]])
    #plt.scatter(a[:, 0], a[:, 1], color='blue')
    #plt.show()
#plt.show()

#for t in DataSet1:
#    sostream_clustering.process(t)

#ax = plt.axes(projection="3d")
#a = np.array([c.centroid for c in sostream_clustering.M[-1]])
#ax.scatter3D(a[:,0],a[:,1],a[:,2], color="green")
#plt.show()

#3d plotting after all the clustering but i dont know why it doesnt work in 3d with complete accuracy as it works in 2d
#fig = plt.figure()
#ax = plt.axes(projection="3d")
#ax = fig.add_subplot(projection='3d')
#a = np.array([c.centroid for c in sostream_clustering.M[-1]])
#ax.scatter3D(a[:,0],a[:,1],a[:,2], color ="green")
#plt.show()


#2d plotting
plt.figure()
data_df1.plot.scatter(x=0,y=1)
a = np.array([c.centroid for c in sostream_clustering.M[-1]])
plt.scatter(a[:,0], a[:,1], color='blue')
plt.show()



t3_stop = process_time()

AllTime = (t3_stop - t1_start)

#printing bunch of answers
print('total time for runing the algorithm :',AllTime)
print('number of total clusters at the end :' ,MicroCluster.count_Final_Clusters)
#print('number of faded clusters :',fading_all.count_fadedClusters)  ## using fade_all is optional and unnecessary ###
print('number of deleted clusters :',merge_clusters.count_deletedClusters)
print('number of merged clusters :',merge_clusters.counting_mergedClusters)
