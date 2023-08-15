import pickle
from Practice import Test

with open('confidencial.pkl', 'rb') as file:
    myvar = pickle.load(file)
    print(myvar.data)