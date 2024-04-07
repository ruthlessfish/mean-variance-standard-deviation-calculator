import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    # set up response format
    calculations = {
        'mean': [[],[]],
        'variance': [[],[]],
        'standard deviation': [[],[]],
        'max': [[],[]],
        'min': [[],[]],
        'sum': [[],[]]
    }

    # convert list to a 3x3 Numpy array
    matrix = np.array(list).reshape(3,3)

    # calculate values for axis1
    for arr in np.hsplit(matrix, 3):
        calculations['mean'][0].append(arr.mean())
        calculations['variance'][0].append(arr.var())
        calculations['standard deviation'][0].append(arr.std())
        calculations['max'][0].append(arr.max())
        calculations['min'][0].append(arr.min())
        calculations['sum'][0].append(arr.sum())

    # calculate values for axis2
    for arr in np.vsplit(matrix, 3):
        calculations['mean'][1].append(arr.mean())
        calculations['variance'][1].append(arr.var())
        calculations['standard deviation'][1].append(arr.std())
        calculations['max'][1].append(arr.max())
        calculations['min'][1].append(arr.min())
        calculations['sum'][1].append(arr.sum())

    # calculate values for the flattened array
    calculations['mean'].append(matrix.flatten().mean())
    calculations['variance'].append(matrix.flatten().var())
    calculations['standard deviation'].append(matrix.flatten().std())
    calculations['max'].append(matrix.flatten().max())
    calculations['min'].append(matrix.flatten().min())
    calculations['sum'].append(matrix.flatten().sum())

    return calculations