class MicroCluster:
    count_Final_Clusters = 0

    #the class which make each cluster as a object and have three parametrs centroid and population of cluster
    #and its radius and also we added a counter by name of count_Final_Clusters  which will be ++ if any cluster is maid and will
    #be -- if any merge or deletion happen(-- happens in fadinAll and mergeClusters )
    def __init__(self, centroid, number_points = 1, radius = 0):
        self.number_points = number_points
        self.radius = radius
        self.centroid = centroid
        MicroCluster.count_Final_Clusters += 1

    pass