# workLittleTool
上班用的一些小工具

安装依赖:
```
pip install -r requirements.txt 
```

doors.py
树莓派收到门铃自动相应门禁

```
$ git clone https://github.com/crcrcr999/AnswerTheFuckingDoor.git # Cloning project repository
$ cd AnswerTheFuckingDoor # Enter to project directory
$ python3 -m venv my_venv # If not created, creating virtualenv
$ source ./my_venv/bin/activate # Activating virtualenv
(my_env)$ pip3 install -r ./requirements.txt # Installing dependencies
(my_env)$ deactivate # When you want to leave virtual environment
```

生成依赖命令:
```
pipreqs . --encoding=utf8 --force
```
playmusic.py
上班自动播放u盘歌曲

需要执行	
```
sudo apt install python3-gst-1.0
```