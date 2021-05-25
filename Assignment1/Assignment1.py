import hashlib
import time
inp = input()
start = time.time()
x = 1
target = '00000'+'f'*(256//4 - 5)
curr = inp+str(x)
result = hashlib.sha256(curr.encode()).hexdigest()
while result[:5]!='00000':
    x+=1
    curr = inp+str(x)
    result = hashlib.sha256(curr.encode()).hexdigest()
print('x = ',x)
print('hash of string ',curr," = ",result)
print('time taken = ',time.time()-start)
