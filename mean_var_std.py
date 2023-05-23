import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
  arr = np.array(list).reshape(3,3)
  #mean along all axis
  mean_col = np.mean(arr,axis = 0).tolist()
  mean_row = np.mean(arr, axis = 1).tolist()
  mean_flat = np.mean(arr).tolist()
  meanlis = [mean_col,mean_row,mean_flat]
  #variance along all axis
  var_col = np.var(arr, axis = 0).tolist()
  var_row = np.var(arr, axis = 1).tolist()
  var_flat = np.var(arr).tolist()
  varlis = [var_col,var_row,var_flat]
  #standard deviations along all axis
  std_col = np.std(arr,axis=0).tolist()
  std_row = np.std(arr,axis=1).tolist()
  std_flat = np.std(arr).tolist()
  stdlis = [std_col,std_row,std_flat]
  #max along all axis
  max_col = np.max(arr,axis=0).tolist()
  max_row = np.max(arr,axis=1).tolist()
  max_flat = np.max(arr).tolist()
  maxlis = [max_col,max_row,max_flat]
  #min along all axis
  min_col = np.min(arr,axis=0).tolist()
  min_row = np.min(arr,axis=1).tolist()
  min_flat = np.min(arr).tolist()
  minlis = [min_col,min_row,min_flat]
  #sum along all axis
  sum_col = np.sum(arr,axis=0).tolist()
  sum_row = np.sum(arr,axis=1).tolist()
  sum_flat = np.sum(arr).tolist()
  sumlis = [sum_col,sum_row,sum_flat]
  #return dictionary with calculation lists
  calculations = {'mean': meanlis, 'variance': varlis, 'standard deviation': stdlis, 'max': maxlis, 'min': minlis, 'sum': sumlis}
  
  return calculations