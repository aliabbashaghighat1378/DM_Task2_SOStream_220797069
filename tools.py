from math import sqrt
import numpy as np

#this function actually compute the distance of two point or a point and centroid of a cluster in order to find the
#winner cluster(the cluster which is more near to the point) or winner neighbor and where ever it is needed
def distance(v1, v2):
    return np.sqrt(((v1 - v2) ** 2).sum())


#this use in merging cluster that a and b are centroids of two clusters and the weights are population of that cluster
#which will have influence on the place of centroid of the merged cluster
def weightedMean(a, b, wieghtA, wieghtB):
    return ((wieghtA * a + wieghtB * b)/(wieghtA + wieghtB))


#this function actully compare the distance between centroid of all clusters and the new point in order to find winner cluster
def minDist(vt, micro_clusters):
    micro_cluster_min_dist = float('inf')
    min_micro_cluster = None
    for micro_cluster in micro_clusters:
        dist_to_micro_cluster = distance(vt, micro_cluster.centroid)
        if dist_to_micro_cluster <= micro_cluster_min_dist:
            micro_cluster_min_dist = dist_to_micro_cluster
            min_micro_cluster = micro_cluster
    
    return min_micro_cluster
