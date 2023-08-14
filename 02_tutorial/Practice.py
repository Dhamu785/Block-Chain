import hashlib

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



h = hashlib.sha256()
i = 0
h.update(str(i).encode("utf-8"))
while int(h.hexdigest(),16) > 2**(256-10):
    i += 1
    h = hashlib.sha256()
    h.update(str(i).encode("utf-8"))

print(i)
print(h.hexdigest())
print(int(h.hexdigest(), 16))

print("{} {}".format("data","123"))