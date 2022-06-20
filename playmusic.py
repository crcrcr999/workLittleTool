import Play_mp3
import datetime
import random
import time

### 定义文件名获取函数
def data_needed(filePath):
    import os        #引入os
    file_name = list()        #新建列表
    for i in os.listdir(filePath):        #获取filePath路径下所有文件名
    	if i.endswith(".mp3"):
        	data_collect = ''.join(i)        #文件名字符串格式
        	file_name.append(data_collect)        #将文件名作为列表元素填入
    return(file_name)        #返回列表

isworktime = lambda x,y: True if (x>=y[0] and x<y[1]) else False
upan="/media/cr/MUSIC/"
workrange=[13,19]
while True:
	nowhour = datetime.datetime.now().hour
	nowminute=datetime.datetime.now().minute
	if isworktime(nowhour,workrange):
	#if nowminute<23:
		musiclist=data_needed(upan)
		randomint=random.randint(0,len(musiclist))
		speakpath = upan+musiclist[randomint]
		Play_mp3.play(speakpath)
		time.sleep(1)
	else:
		time.sleep(60)
	
