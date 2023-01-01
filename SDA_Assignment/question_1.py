import pandas as pd
from mpi4py import MPI
def my_region_units_sold(df):
    df1 = df[["region", "units_sold"]]
    print(df1.groupby(by=["region"]).sum())
def my_region_units_sold(df):
    df1 = df[["region", "units_sold"]]
    print(df1.groupby(by=["region"]).sum())
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
df=pd.read_csv('C:/Users/akash/OneDrive/Desktop/geosales.csv')
#(a) What is the total units_sold in each region across the entire data set ?
# Create the dictionary
Partitions_map = {'Australia and Oceania': 0, 'Europe': 1, 'Sub-Saharan Africa': 2,'Central America and the Caribbean':3,'Asia':4,'North America':5, 'Middle East and North Africa':6}
# Add a new column named 'Partition'
df['Partition'] = df['region'].map(Partitions_map)

for i in range(0,size):
    if rank%size == i:
        my_region_units_sold(df[df['Partition']% size==i])



