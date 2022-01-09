import numpy as np
import pandas as pd
import tools

#this is second alg of the paper which cooperate with findOverlap and then merge cluster. this code will finde the winner neighbor of
#the winner cluster (which satisfie minPts) in order to find overlap at next step and if every thing goes ok merge them together
class find_neighbors :
  def find_neighbors(win_microcluster, minPts, model_t):
    if len(model_t) >= minPts:
      win_dist = []
      for microcluster in model_t:
        win_dist.append(tools.distance(microcluster.centroid, win_microcluster.centroid))
      win_dist.sort()
      idx_microclusters = np.argsort(win_dist)

      k_dist = win_dist[minPts-1]
      win_microcluster.radius = k_dist
      win_nn = [model_t[idx] for idx in idx_microclusters[0:(minPts)]]
      return win_nn
    else:
      return []

