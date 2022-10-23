# remember to import your libraries!
import numpy as np
import pandas as pd


def get_random_matrix(num_rows, num_columns):
    matrix = np.random.rand(num_rows, num_columns)
    return matrix


def get_file_dimensions(file_name):
    iris_df = pd.read_csv(file_name, sep=',', header=None)
    return iris_df.shape


def write_matrix_to_file(num_rows, num_columns, file_name):
    matrix = np.random.rand(num_rows, num_columns)
    np.savetxt(file_name, matrix, delimiter=',')
    return None
