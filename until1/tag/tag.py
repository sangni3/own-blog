import requests
import time

iddr = "http://127.0.0.1:8000/index/"

ret = requests.get(iddr)  # 打开
print(ret)
for a in range(100):
    start_time = time.time()
    ret = requests.get(iddr)  # 刷新
    end_time = time.time()
    print("runtime=", (end_time - start_time) * 1000)
    print(ret)
