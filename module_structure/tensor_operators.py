""""
Mario Domínguez Ferrer.
Machine Learning, 4th BA.

TENSOR CALCULATOR.
"""


import torch # To generate tensors

__all__ = ['TensorCalculator']

class TensorCalculator:
    # Tensors' dimensions (two dimensions, x and y):
    def __init__(self):
        return None

    # All-Zeros tensor:
    def tensor_zeros(self, dim_x, dim_y):
        all_zeros = torch.zeros([dim_x, dim_y])
        return all_zeros

    # All-Ones tensor:
    def tensor_ones(self, dim_x, dim_y):
        all_ones = torch.ones([dim_x, dim_y])
        return all_ones

    # Tensor with random values:
    def tensor_random(self, dim_x, dim_y):
        randoms = torch.rand([dim_x, dim_y])
        return randoms

    # Sum of tensors
    def tensor_sum(self, dim_x, dim_y):
        a = torch.rand([dim_x, dim_y])
        b = torch.rand([dim_x, dim_y])
        return print(a, '\n', ' + ', '\n', b, '\n', '=', torch.add(a,b))

    # Multiplication of tensors:
    def tensor_multiplication(self, dim_x, dim_y):
        # Now we need to generate two tensors but with one condition: the number of rows of tensor c must be equal
        # to the number of columns of tensro d. So:
        c = torch.rand([dim_x, dim_y])
        d = torch.rand([dim_y, dim_x])
        return print(c, '\n', ' * ', '\n', d, '\n', '=', torch.matmul(c, d))

