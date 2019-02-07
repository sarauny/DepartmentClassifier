from multiprocessing import Pool, cpu_count
import pandas as pd


# define traverse to unlist the lists in a list
def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o


def process_Pandas_data(func, df, stemDeptKeys=None, num_processes=None, index=0):
    ''' Apply a function separately to each sub-dataframe, in parallel.'''
    
    # If num_processes is not specified, default to #machine-cores
    if num_processes==None:
        num_processes = cpu_count()
    
    # 'with' context manager takes care of pool.close() and pool.join() for us
    with Pool(num_processes) as pool:
        
        # calculate the chunk size as an integer
        chunk_size = int(df.shape[0]/num_processes)
        chunks = [df.iloc[df.index[i:i + chunk_size]] for i in range(0, df.shape[0], chunk_size)]
        
        # pool.map returns results as a list
        results_list = pool.map(func, chunks)
        
        # return list of processed columns, concatenated together as a new dataframe
        return pd.concat(results_list)