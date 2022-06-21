import datetime
import random
import time
import worktime
import os
import playsound


def play(filename):
    try:
        playsound.playsound(filename)
    except Exception as ide:
        print(f'Error: {ide}')

### 定义文件名获取函数
def data_needed(filePath):
    import os        #引入os
    file_name = list()        #新建列表
    for i in os.listdir(filePath):        #获取filePath路径下所有文件名
    	if i.endswith(".mp3"):
        	data_collect = ''.join(i)        #文件名字符串格式
        	file_name.append(data_collect)        #将文件名作为列表元素填入
    return(file_name)        #返回列表

#isworktime = lambda x,y: True if (x>=y[0] and x<y[1]) else False
upanPath="/media/cr/MUSIC/"
endMusicPath="end/范圣琦 - 回家 (萨克斯独奏).mp3"
playEndMusic=False
#workrange=[13,20]
while True:
	#nowhour = datetime.datetime.now().hour
	#nowminute=datetime.datetime.now().minute
	if os.path.exists(upanPath):
		if worktime.timecalendar():
		#if nowminute<23:
			playEndMusic=False
			musiclist=data_needed(upanPath)
			randomint=random.randint(0,len(musiclist))
			speakpath = upanPath+musiclist[randomint]
			play(speakpath)
			time.sleep(1)
	else:
		if playEndMusic==False:
			play(upanPath+endMusicPath)
			playEndMusic=True
		time.sleep(60)
	
