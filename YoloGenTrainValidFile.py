import os

# save in parent folder of ./data
save_path=os.getcwd()+'/'
scan = save_path+"data/"

def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail
l = []
for jpg in os.listdir(scan):
    if not jpg.endswith(".jpg"):
    	continue
    jpg=scan+jpg
    print('.jpg',jpg)
    txt=replace_last(jpg,".jpg",".txt")

    if not os.path.exists(txt):
    	print('annotation do not exist',txt)
    	continue
    print('train set found:',txt,jpg)
    l.append(jpg)

train=open('train.txt','w+')
valid=open('valid.txt','w+')
i=0
for jpg in l:
	if i%50==0:
		valid.write(jpg+'\n')
	else:
		train.write(jpg+'\n')
	i+=1
train.close()
valid.close()

