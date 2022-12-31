import numpy as np

def calculate(list):

    calculations = dict()
    #print(list, type(list), len(list))

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list)
    arr = arr.reshape((3,3))
    #print('the arr', arr, arr.shape)

    all_sum = (arr.sum()).tolist()
    ax0_sum = (arr.sum(axis=0)).tolist()
    ax1_sum = (arr.sum(axis=1)).tolist()
    #print('sums >> all, 0, 1 >>>', all_sum, ax0_sum, ax1_sum)

    ax0_mean = (arr.mean(axis=0)).tolist()
    ax1_mean = (arr.mean(axis=1)).tolist()
    all_mean = (arr.mean()).tolist()
    #print('mean ax0, ax1, all >>>', ax0_mean, ax1_mean, all_mean)

    ax0_var = (arr.var(axis=0)).tolist()
    ax1_var = (arr.var(axis=1)).tolist()
    all_var = (arr.var()).tolist()

    ax0_std = (arr.std(axis=0)).tolist()
    ax1_std = (arr.std(axis=1)).tolist()
    all_std = (arr.std()).tolist()

    ax0_max = (arr.max(axis=0)).tolist()
    ax1_max = (arr.max(axis=1)).tolist()
    all_max = (arr.max()).tolist()

    ax0_min = (arr.min(axis=0)).tolist()
    ax1_min = (arr.min(axis=1)).tolist()
    all_min = (arr.min()).tolist()

    calculations['mean'] = [ax0_mean, ax1_mean, all_mean]
    calculations['variance'] = [ax0_var, ax1_var, all_var]
    calculations['standard deviation'] = [ax0_std, ax1_std, all_std]
    calculations['max'] = [ax0_max, ax1_max, all_max]
    calculations['min'] = [ax0_min, ax1_min, all_min]
    calculations['sum'] = [ax0_sum, ax1_sum, all_sum]
    #print(calculations)

    return calculations