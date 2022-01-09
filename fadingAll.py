from micro_cluster import MicroCluster

#this fading job will remove some not very important clusters(which dont have enough members) but it is not necessary to be used
# as it says in the paper
class fading_all:
    count_fadedClusters =0
    def fadingAll(M, t_current, var_lambda, fadeThreshold):
        M_copy = M.copy()
        for microcluster in M_copy:
            t = t_current - microcluster['t']
            fading = microcluster.number_points*2**(-var_lambda*t)
            if fading < fadeThreshold:
                fading_all.count_fadedClusters +=1
                MicroCluster.count_Final_Clusters = MicroCluster.count_Final_Clusters - 1
                M.remove(microcluster)
