import hashlib
import time
inp = input()
now = time.time()
x = 0
target = '00000'+'f'*(256//4 - 5)
curr = inp+str(x)
result = hashlib.sha256(curr.encode()).hexdigest()
while result[:5]!='00000':
    i+=1
    curr = inp+str(x)
    result = hashlib.sha256(curr.encode()).hexdigest()
print('x = ',x)
print('hash of string ',curr," = ",result)
print('time taken = ',time.time()-now)