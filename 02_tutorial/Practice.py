import hashlib
import pickle

# h = hashlib.sha256()
# h.update("2629".encode("utf-8"))
# h.digest()
# print(h.hexdigest())
# print(int(h.hexdigest(), 16))


# IT CUMALIATE THE HEXA VALUES
# h = hashlib.sha256()
# i = 0
# h.update(str(i).encode("utf-8"))
# while int(h.hexdigest(),16) > 2**(256-10):
#     i += 1
#     h.update(str(i).encode("utf-8"))
#     print(i)

# print(h.hexdigest())



# h = hashlib.sha256()
# i = 0
# h.update(str(i).encode("utf-8"))
# while int(h.hexdigest(),16) > 2**(256-10):
#     i += 1
#     h = hashlib.sha256()
#     h.update(str(i).encode("utf-8"))

# print(i)
# print(h.hexdigest())
# print(int(h.hexdigest(), 16))

# print("{} {}".format("data","123"))

# STORE THE HASH CLASS DATA IN A FILE
class Test:
    def __init__(self, data, time) -> None:
        self.data = data
        self.time = time

    def dha(self):
        print("Fun 2")

# d = Test("Confidencial1","5 'O clk")
# with open("confidencial.pkl", "wb") as f:
#     pickle.dump(d, f)