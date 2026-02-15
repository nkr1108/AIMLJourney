import numpy as np
import torch

print(f"torch.__version__: {torch.__version__}") # check the version of PyTorch
print(f"CUDA available: {torch.cuda.is_available()}") # check if CUDA (GPU support) is available
print(f"Number of CUDA devices: {torch.cuda.device_count()}") # check the number of available CUDA devices (GPUs)
if torch.cuda.is_available():
    print(f"Name of the first CUDA device: {torch.cuda.get_device_name(0)}") # get the name of the first CUDA device (GPU)


print(f"MPS available: {torch.backends.mps.is_available()}")
print(f"MPS built: {torch.backends.mps.is_built()}")

# demo the use of torch.tensor, torch.zeros, torch.ones, torch.eye, torch.arange, torch.linspace, torch.rand, torch.randint, and torch.normal
print("######################################################################################################################################################")
print(f"#### demo the use of torch.tensor, torch.zeros, torch.ones, torch.eye, torch.arange, torch.linspace, torch.rand, torch.randint, and torch.normal ####")
print("######################################################################################################################################################")
print(f"\ntorch.tensor([1, 2, 3]) => \n {torch.tensor([1, 2, 3])}") # create a 1D tensor
print(f"\ntorch.tensor([[1, 2], [3, 4]]) => \n {torch.tensor([[1, 2], [3, 4]])}") # create a 2D tensor
print(f"\ntorch.zeros((2, 3)) => \n {torch.zeros((2, 3))}") # create a 2D tensor of zeros with shape (2, 3)
print(f"\ntorch.ones((4, 5)) => \n {torch.ones((4, 5))}") # create a 2D tensor of ones with shape (4, 5)
print(f"\ntorch.eye(3) => \n {torch.eye(3)}") # create a 2D tensor with ones on the diagonal and zeros elsewhere (identity matrix)
print(f"\ntorch.arange(0, 10, 2) => \n {torch.arange(0, 10, 2)}") # create a 1D tensor of evenly spaced values within a specified range (start, stop, step)
print(f"\ntorch.linspace(0, 1, 5) => \n {torch.linspace(0, 1, 5)}") # create a 1D tensor of evenly spaced values between a specified start and stop value (inclusive) with a specified number of samples
print(f"\ntorch.rand(3, 4) => \n {torch.rand(3, 4)}") # create a 2D tensor of random values between 0 and 1 with shape (3, 4)
print(f"\ntorch.randint(0, 10, size=(2, 3)) => \n {torch.randint(0, 10, size=(2, 3))}") # create a 2D tensor of random integers between a specified low (inclusive) and high (exclusive) value with a specified shape
print(f"\ntorch.normal(mean=0, std=1, size=(2, 3)) => \n {torch.normal(mean=0, std=1, size=(2, 3))}") # create a 2D tensor of random values drawn from a normal distribution with specified mean, standard deviation, and shape (size)


# demo creating tensors with numpy array and converting between numpy arrays and PyTorch tensors
print("######################################################################################################################################################")
print(f"#### demo creating tensors with numpy array and converting between numpy arrays and PyTorch tensors ####")
print("######################################################################################################################################################")
np_array = np.array([[1, 2], [3, 4]]) # create a 2D numpy array
torch_tensor = torch.from_numpy(np_array) # create a PyTorch tensor from the numpy array
print(f"\nNumpy array: \n{np_array}") # original numpy array
print(f"\nPyTorch tensor created from numpy array: \n{torch_tensor}") # PyTorch tensor created from the numpy array
print(f"\nType of the original numpy array: {type(np_array)}") # type of the original numpy array
print(f"\nType of the PyTorch tensor: {type(torch_tensor)}") # type of the PyTorch tensor
torch_tensor_back_to_numpy = torch_tensor.numpy() # convert the PyTorch tensor back to a numpy array
print(f"\nPyTorch tensor converted back to numpy array: \n{torch_tensor_back_to_numpy}") # numpy array converted back from the PyTorch tensor
print(f"\nType of the converted numpy array: {type(torch_tensor_back_to_numpy)}") # type of the converted numpy array

# using as_tensor to create a tensor from a numpy array (this will create a copy of the data)
torch_tensor_from_as_tensor = torch.as_tensor(np_array) # create a PyTorch tensor from the numpy array using as_tensor (this will create a copy of the data)
print(f"\nPyTorch tensor created from numpy array using as_tensor: \n{torch_tensor_from_as_tensor}") # PyTorch tensor created from the numpy array using as_tensor
print(f"\nType of the PyTorch tensor created using as_tensor: {type(torch_tensor_from_as_tensor)}") # type of the PyTorch tensor created using as_tensor

 # using torch.tensor to create a tensor from a numpy array (this will also create a copy of the data)
torch_tensor_from_torch_tensor = torch.tensor(np_array) # create a PyTorch tensor from the numpy array using torch.tensor (this will also create a copy of the data)
print(f"\nPyTorch tensor created from numpy array using torch.tensor: \n{torch_tensor_from_torch_tensor}") # PyTorch tensor created from the numpy array using torch.tensor
print(f"\nType of the PyTorch tensor created using torch.tensor: {type(torch_tensor_from_torch_tensor)}") # type of the PyTorch tensor created using torch.tensor

# demo the difference between torch.tensor vs torch.Tensor
print("###" * 50)
print(f"#### demo the difference between torch.tensor vs torch.Tensor ####")
print("###" * 50)
torch_tensor_lowercase = torch.tensor([1, 2, 3]) # create a PyTorch tensor using torch.tensor (this will create a copy of the data)
torch_tensor_uppercase = torch.Tensor([1, 2, 3]) # create a PyTorch tensor using torch.Tensor (this will also create a copy of the data, but float tensor by default)
print(f"\nPyTorch tensor created using torch.tensor: \n{torch_tensor_lowercase}") # PyTorch tensor created using torch.tensor
print(f"\nPyTorch tensor created using torch.Tensor: \n{torch_tensor_uppercase}") # PyTorch tensor created using torch.Tensor
print(f"\nType of the PyTorch tensor created using torch.tensor: {type(torch_tensor_lowercase)}") # type of the PyTorch tensor created using torch.tensor
print(f"\nType of the PyTorch tensor created using torch.Tensor: {type(torch_tensor_uppercase)}") # type of the PyTorch tensor created using torch.Tensor
print(f"\nData type of the PyTorch tensor created using torch.tensor: {torch_tensor_lowercase.dtype}") # data type of the PyTorch tensor created using torch.tensor
print(f"\nData type of the PyTorch tensor created using torch.Tensor: {torch_tensor_uppercase.dtype}") # data type of the PyTorch tensor created using torch.Tensor

# create a empty tensor using torch.empty (this will create a tensor with uninitialized values)
print("######################################################################################################################################################")
print(f"#### create a empty tensor using torch.empty (this will create a tensor with uninitialized values) ####")
print("######################################################################################################################################################")
torch_empty_tensor = torch.empty((2, 3)) # create a 2D tensor with uninitialized values using torch.empty
print(f"\nPyTorch tensor created using torch.empty: \n{torch_empty_tensor}") # PyTorch tensor created using torch.empty
print(f"\nType of the PyTorch tensor created using torch.empty: {type(torch_empty_tensor)}") # type of the PyTorch tensor created using torch.empty
print(f"\nData type of the PyTorch tensor created using torch.empty: {torch_empty_tensor.dtype}") # data type of the PyTorch tensor created using torch.empty

# demo the use of dtype, shape, size, reshape, and astype
print("######################################################################################################################################################")
print(f"#### demo the use of dtype, shape, size, reshape, and astype ####")
print("######################################################################################################################################################")
torch_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32) # create a 2D tensor with specified data type
print(f"\nOriginal PyTorch tensor: \n{torch_tensor}") # original PyTorch tensor
print(f"\nData type of the original PyTorch tensor: {torch_tensor.dtype}") # data type of the original PyTorch tensor
print(f"\nShape of the original PyTorch tensor: {torch_tensor.shape}") # shape of the original PyTorch tensor
print(f"\nSize of the original PyTorch tensor: {torch_tensor.size()}") # size of the original PyTorch tensor
reshaped_torch_tensor = torch_tensor.reshape((3, 2)) # reshape the original tensor to a new shape
print(f"\nReshaped PyTorch tensor: \n{reshaped_torch_tensor}") # reshaped PyTorch tensor
print(f"\nShape of the reshaped PyTorch tensor: {reshaped_torch_tensor.shape}") # shape of the reshaped PyTorch tensor
int_torch_tensor = torch_tensor.to(torch.int32) # convert the original tensor to a different data type (int32)
print(f"\nPyTorch tensor converted to int32: \n{int_torch_tensor}") # PyTorch tensor converted to int32
print(f"\nData type of the converted PyTorch tensor: {int_torch_tensor.dtype}") # data type of the converted PyTorch tensor

# demo tensor operations
print("######################################################################################################################################################")
print(f"#### demo tensor operations ####")
print("######################################################################################################################################################")
torch_tensor1 = torch.tensor([[1, 2], [3, 4]]) # create the first 2D tensor
torch_tensor2 = torch.tensor([[5, 6], [7, 8]]) # create the second 2D tensor
print(f"\nFirst PyTorch tensor: \n{torch_tensor1}") # first PyTorch tensor
print(f"\nSecond PyTorch tensor: \n{torch_tensor2}") # second PyTorch tensor
sum_tensor = torch_tensor1 + torch_tensor2 # element-wise addition of the two tensors
print(f"\nElement-wise sum of the two tensors: \n{sum_tensor}") # element-wise sum of the two tensors
product_tensor = torch_tensor1 * torch_tensor2 # element-wise multiplication of the two tensors
print(f"\nElement-wise product of the two tensors: \n{product_tensor}") # element-wise product of the two tensors
matrix_product_tensor = torch.matmul(torch_tensor1, torch_tensor2) # matrix multiplication of the two tensors
print(f"\nMatrix product of the two tensors: \n{matrix_product_tensor}") # matrix product of the two tensors