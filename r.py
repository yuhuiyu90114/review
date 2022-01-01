data = []
sum_len = 0
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        count += 1
        data.append(line)
        if count % 10000 ==0:
            print(count)
print(len(data))
print(data[0])
print('---------------------')
print(data[1])
for d in data:
    sum_len += len(d)
print('平均留言長度是',sum_len/len(data))
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print(len(new))
print(new[0])
print(new[1])
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print(len(good))
print(good[0])
print(good[1])

