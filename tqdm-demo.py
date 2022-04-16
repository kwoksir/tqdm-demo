import re
from tqdm import trange
import time
nameList = ["Chan Tai Man", "Lee Lap Man","Cheung Kwok Keung","Li Ho Yan"]
R = []
for x in trange(len(nameList)):
    R.append(re.sub(r'[a-z]','*', nameList[x]))
    time.sleep(0.5)
print(R)
