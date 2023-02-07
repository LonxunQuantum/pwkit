# PWkit
 _ ____      ___ __ ___   __ _| |_
| '_ \ \ /\ / / '_ ` _ \ / _` | __|  
| |_) \ V  V /| | | | | | (_| | |_   
| .__/ \_/\_/ |_| |_| |_|\__,_|\__|  
|_|


<font size="10">Toolkits for pwmat </font>

详情见 http://doc.lonxun.com/PWkit/PWkit.html


# 1. Installation
# 1.0. 需要准备的文件
1. `pwkit_env.tar.gz`: pwkit 的环境
2. `pwkit.tar.gz`: pwkit 软件包

## 1.1. Python 的 conda 环境配置
```shell
### Part I. 到新服务器下解压
# 1. 将 `pwkit_env` 环境解压到 `pwkit_env` 文件夹下
$ mkdir -p pwkit_env
$ tar -xzf pwkit_env.tar.gz -C pwkit
# 2. 激活 `pwkit_env` 环境
$ source pwkit/bin/activate
```

## 1.2. pwkit 环境变量设置
```shell
# Step 1. 设置环境变量
(pwkit) $ export PWKIT_ROOT=/data/home/liuhanyu/hyliu/code/pwkit
(pwkit) $ export PATH=/data/home/liuhanyu/hyliu/code/pwkit/bin:$PATH

# Step 2. 设置Conda环境 -- 修改 CONDA_PATH
(pwkit) $ vim pwkit.cfg 
```


## 1.3. 卸载
```bash
rm -rf /share/app/pwkit
rm -rf $HOME/.local/pwkit
```



# 2. 使用方法 (On MCloud2)
```shell
# 加载环境
$ module load pwkit/1.0

# 运行 pwkit
$ pwkit
 _ ____      ___ __ ___   __ _| |_
| '_ \ \ /\ / / '_ ` _ \ / _` | __|  website: http://www.lonxun.com
| |_) \ V  V /| | | | | | (_| | |_   v1.0.0
| .__/ \_/\_/ |_| |_| |_|\__,_|\__|  pwmat kit Usage: pwkit -h
|_|
```