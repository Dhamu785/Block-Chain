from chain import Chain

c = Chain(22)
data = ['Confidencial1', 'Confidicial2', 'Confidicial3', 'Confidicial4', 'Confidicial5', 'Confidicial6']
for i in data:
    c.add_pool(i)
    c.mine()
    print(">>"*10)
    print(f"Previous Block hash: {c.blocks[-1].previous_hash.hexdigest()}")
    print(f"Current Block hash: {c.blocks[-1].hash.hexdigest()}")
    print(">>"*10)
    print()




