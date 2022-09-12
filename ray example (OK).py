import ray
import time

ray.init()

@ray.remote
def test():
    for i in range(0,10):
        print(1)
        time.sleep(2)

@ray.remote
def test2():
    for i in range(0,10):
        print(2)
        time.sleep(2)

ray.get([test.remote(), test2.remote()])
ray.close()