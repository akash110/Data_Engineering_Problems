import pandas as pd
from mpi4py import MPI
import math as m
def split(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
df = pd.read_csv('C:/Users/akash/OneDrive/Desktop/geosales.csv')
loc_num = len(df["total_profit"]) /size
i=m.ceil(loc_num)
data = df["total_profit"].tolist()
list1=list(split(data, i))
if rank == 0:
    data1=list1
else:
    data1=None
data1=comm.scatter(data1, root=0)
loc_sum = 0
count=0
for i in range(0,len(data1)):
   loc_sum =loc_sum + data1[i]
   count=count+1
avg=loc_sum/count
final_res=comm.gather(avg,root=0)
if rank ==0:
    fin=0
    for i in range(0,size):
        fin =fin+ final_res[i]
    final_avg = fin /size
    print("Final average:")
    print(final_avg)