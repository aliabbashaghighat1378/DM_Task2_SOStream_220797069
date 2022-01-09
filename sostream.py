from tools import minDist, distance
from findNeighbors import find_neighbors
from updateCluster import updateCluster
from findOverlap import find_overlap
from mergeClusters import merge_clusters
from newCluster import newCluster


class SOStream:

    #makes the object from SOStream class by initilizing its most important and primary parametrs like mergethershold and minPts
    #that works in finding winner neighbor and initilize some other parameters
    def __init__(self, alpha = 0.15, minPts = 9, merge_threshold = 28000):
        self.alpha = alpha
        self.minPts = minPts
        self.M = [[]]
        self.merge_threshold = merge_threshold


    #the most important function which gets the parametrs of init and the stream of date and call all the other fumctions
    #like dist, findOverlap , update Cluster ,findneighbor and ... in order to set a point to a cluster and then update
    #that clusrers parameter(like centroid radius and..) and then check if merging or deletion must be happend
    def process(self, vt):
        winner_micro_cluster = minDist(vt, self.M[-1])
        new_M = self.M[-1].copy()
        if len(new_M) >= self.minPts:
            winner_neighborhood = find_neighbors.find_neighbors(winner_micro_cluster, self.minPts, new_M)
            if distance(vt, winner_micro_cluster.centroid) < winner_micro_cluster.radius:
                updateCluster.updateCluster(winner_micro_cluster, vt, self.alpha, winner_neighborhood)
            else:
                new_M.append(newCluster.newCluster(vt))
            overlap = find_overlap.find_overlap(winner_micro_cluster, winner_neighborhood)
            if len(overlap) > 0:
                merged_cluster, deleted_clusters = merge_clusters.merge_clusters(winner_micro_cluster, overlap, self.merge_threshold)
                for deleted_cluster in deleted_clusters:
                    new_M.remove(deleted_cluster)
                if merged_cluster is not None:
                    new_M.append(merged_cluster)
        else:
            new_M.append(newCluster.newCluster(vt))
        self.M.append(new_M)
    pass
