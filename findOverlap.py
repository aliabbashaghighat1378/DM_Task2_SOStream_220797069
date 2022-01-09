import pandas as pd
import tools

#this part will detect(and compute) overlap between winner cluster and winner nighbor(which we find that by findNeighbor function)
#and will pass that to merge cluster inorder to merge them if they are close enough
class find_overlap :
  def find_overlap(win, win_nn):
    overlap = []
    for microcluster in win_nn:
      if win is not microcluster:
        if tools.distance(win.centroid, microcluster.centroid) - (win.radius + microcluster.radius) < 0 :
          overlap.append(microcluster)
    return overlap
