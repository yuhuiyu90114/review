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
good =[ d for d in data if 'good' in d]
print(len(good))
bad1= [ d for d in data if 'bad' in d]
print(len(bad1))
bad2 = ['bad' in d for d in data ]

