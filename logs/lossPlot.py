file1 = open('yolact_plus_resnet50_generated_dwg.log', 'r')
Lines = file1.readlines()
import matplotlib
import matplotlib.pyplot as plt
import json
# Strips the newline character
counter = 0;
b = [];
m = [];
c = [];
s = [];
t = [];
x = [];
valX = [];
valCounter = 0;
bAll = [];
b50 = [];
b55 = [];
b60 = [];
b65 = [];
b70 = [];
b75 = [];
b80 = [];
b85 = [];
b90 = [];
b95 = [];

mAll = [];
m50 = [];
m55 = [];
m60 = [];
m65 = [];
m70 = [];
m75 = [];
m80 = [];
m85 = [];
m90 = [];
m95 = [];
for line in Lines:
    if("loss" in json.loads(line.strip())['data']):
      b.append(json.loads(line.strip())['data']['loss']['B']);
      m.append(json.loads(line.strip())['data']['loss']['M']);
      c.append(json.loads(line.strip())['data']['loss']['C']);
      s.append(json.loads(line.strip())['data']['loss']['S']);
      t.append(json.loads(line.strip())['data']['loss']['T']);
      counter = counter + 1;
      x.append(counter);
    elif('elapsed' in json.loads(line.strip())['data']):
      bAll.append(json.loads(line.strip())['data']['box']['all']);
      b50.append(json.loads(line.strip())['data']['box']['50']);
      b55.append(json.loads(line.strip())['data']['box']['55']);
      b60.append(json.loads(line.strip())['data']['box']['60']);
      b65.append(json.loads(line.strip())['data']['box']['65']);
      b70.append(json.loads(line.strip())['data']['box']['70']);
      b75.append(json.loads(line.strip())['data']['box']['75']);
      b80.append(json.loads(line.strip())['data']['box']['80']);
      b85.append(json.loads(line.strip())['data']['box']['85']);
      b90.append(json.loads(line.strip())['data']['box']['90']);
      b95.append(json.loads(line.strip())['data']['box']['95']);
      
      mAll.append(json.loads(line.strip())['data']['mask']['all']);
      m50.append(json.loads(line.strip())['data']['mask']['50']);
      m55.append(json.loads(line.strip())['data']['mask']['55']);
      m60.append(json.loads(line.strip())['data']['mask']['60']);
      m65.append(json.loads(line.strip())['data']['mask']['65']);
      m70.append(json.loads(line.strip())['data']['mask']['70']);
      m75.append(json.loads(line.strip())['data']['mask']['75']);
      m80.append(json.loads(line.strip())['data']['mask']['80']);
      m85.append(json.loads(line.strip())['data']['mask']['85']);
      m90.append(json.loads(line.strip())['data']['mask']['90']);
      m95.append(json.loads(line.strip())['data']['mask']['95']);
      valCounter = valCounter + 1;
      valX.append(valCounter);
      
plt.suptitle('Bounding Box Loss')
plt.plot(x, b)
plt.figure()
plt.suptitle('Mask Loss')
plt.plot(x, m)
plt.figure()
plt.suptitle('C Loss')
plt.plot(x, c)
plt.figure()  
plt.suptitle('S Loss')
plt.plot(x, s)
plt.figure()  
plt.suptitle('T Loss')
plt.plot(x, t)
plt.figure()  

plt.suptitle('Box All')
plt.plot(valX, bAll)
plt.figure()

plt.suptitle('Box 50')
plt.plot(valX, b50)
plt.figure()

plt.suptitle('Box 55')
plt.plot(valX, b55)
plt.figure()

plt.suptitle('Box 60')
plt.plot(valX, b60)
plt.figure()

plt.suptitle('Box 65')
plt.plot(valX, b65)
plt.figure()

plt.suptitle('Box 70')
plt.plot(valX, b70)
plt.figure()

plt.suptitle('Box 75')
plt.plot(valX, b75)
plt.figure()

plt.suptitle('Box 80')
plt.plot(valX, b80)
plt.figure()

plt.suptitle('Box 85')
plt.plot(valX, b85)
plt.figure()

plt.suptitle('Box 90')
plt.plot(valX, b90)
plt.figure()

plt.suptitle('Box 95')
plt.plot(valX, b95)
plt.figure()

plt.suptitle('Mask All')
plt.plot(valX, mAll)
plt.figure()

plt.suptitle('Mask 50')
plt.plot(valX, m50)
plt.figure()

plt.suptitle('Mask 55')
plt.plot(valX, m55)
plt.figure()

plt.suptitle('Mask 60')
plt.plot(valX, m60)
plt.figure()

plt.suptitle('Mask 65')
plt.plot(valX, m65)
plt.figure()

plt.suptitle('Mask 70')
plt.plot(valX, m70)
plt.figure()

plt.suptitle('Mask 75')
plt.plot(valX, m75)
plt.figure()

plt.suptitle('Mask 80')
plt.plot(valX, m80)
plt.figure()

plt.suptitle('Mask 85')
plt.plot(valX, m85)
plt.figure()

plt.suptitle('Mask 90')
plt.plot(valX, m90)
plt.figure()

plt.suptitle('Mask 95')
plt.plot(valX, m95)


plt.show()
