import os
# save in parent folder of ./data

l = []
scan = "data/"
for jpg in os.listdir(scan):
    if not jpg.endswith(".jpg"):
    	continue
    l.append(jpg)
    print('Append JPG ',jpg)

train=open('jpg.list','w+')
i=0
for jpg in l:
	train.write(os.getcwd()+'/'+jpg+'\n')
train.close()

