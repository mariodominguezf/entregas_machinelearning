# entregas_machinelearning

A python class for a tensor calculator usying PyTorch.

# Overview.
This Python file porvides some utilities needed to perform basic tensor operation uding PyToroch.
With it, you cancreate tensors filled with zeros, ones or random values, and calcuations duch as addition and multiplication of those tensors.

# Installation (Requirements).
It is highly important to install Pytorch using pip:
    pip install torch

# Usage.
This code can be used as following:

  from tensor_calculator import TensorCalculator

  calculator = TensorCalculator()

  zero_tensor = calculator.tensor_zeros(2,3)
  ones_tensor = calculator.tensor_ones(2,3)
  random_tensor = calculator.tensor_random(2,3)
  sum_tensor = calculator.tensor_zum(2,3)
  multiplication_tensor = calculator.tensor_multiplication(2,3)

Inside the brackets is the two dimensions of the tensors.
