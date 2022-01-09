from tools import distance, weightedMean
from micro_cluster import MicroCluster

#this part of code will use the out put of findOverlap function in order to check if the winner cluster and its wiiner neighbor
#can satisfy the merge thereshold so if they can we will merge them together
#and also we add two counter by the name of counting_mergedClusters  & count_deletedClusters in order to count the number of deleted
#and merged cluster in the procedure of clustering which was wanted in the task
class merge_clusters :
    counting_mergedClusters =0
    count_deletedClusters =0
    def merge_clusters(win_micro_cluster, overlaping_micro_clusters, merge_threshold):
        merged_cluster = None
        deleted_clusters = list()
        for micro_cluster in overlaping_micro_clusters:
            if distance(micro_cluster.centroid, win_micro_cluster.centroid) < merge_threshold:
                if len(deleted_clusters) == 0:
                    deleted_clusters.append(win_micro_cluster)
                    merged_cluster = MicroCluster(win_micro_cluster.centroid,
                                                  number_points=win_micro_cluster.number_points,
                                                  radius=win_micro_cluster.radius)
                MicroCluster.count_Final_Clusters -=1
                merge_clusters.counting_mergedClusters +=1
                merged_cluster = merge_clusters.merge(micro_cluster, merged_cluster)
                deleted_clusters.append(micro_cluster)
                merge_clusters.count_deletedClusters += 1
                MicroCluster.count_Final_Clusters -= 1
        return merged_cluster, deleted_clusters


    #after detecting that the two clusters are fit enough to have merge here we make the new cluster and set its parametrs
    #like centroid radius and ...
    def merge(cluster_a, cluster_b):
        new_cluster_centroid = weightedMean(cluster_a.centroid, cluster_b.centroid, cluster_a.number_points, cluster_b.number_points)
        new_cluster_radius = distance(cluster_a.centroid, cluster_b.centroid) + max(cluster_a.radius, cluster_b.radius)
        new_cluster = MicroCluster(centroid=new_cluster_centroid,
                                   number_points=cluster_a.number_points + cluster_b.number_points,
                                   radius=new_cluster_radius)
        return new_cluster
