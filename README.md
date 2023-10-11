# Xiaoyin_Links_Manager

## 用途

方便快捷地管理订阅链接。

## 使用方法

1.  安装依赖
   
```shell
pip3 install -r requirements.txt
```

2.  后台运行

```
nohup python3 main.py &
```

3.   结束运行

```
ps aux | grep python3
```

找到`python3 main.py`当行，复制当行的pid，此处假设为`<pid>`

```
kill -9 <pid>
```
