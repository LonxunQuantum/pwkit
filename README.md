# PWkit
<font size="20">Toolkits for PWmat (http://www.pwmat.com/pwmat-introduce).</font>

## Supplementation
1. PWkit 手册: http://doc.lonxun.com/PWkit/PWkit.html
2. PWmat 常见任务计算方法: http://www.pwmat.com/Tutorials

# 1. 安装说明
## 1.0. 安装提示
1. 如果你进行 `1.1 安装步骤` 部分时，没有找到 `pwkit_env.tar.gz` 文件，你可以通过如下方式下载：  
    - intel版本：https://www.jianguoyun.com/p/DfhQFx8Q_qS-CxifgfwEIAA，提取码为 `lxkt`
    - arm版本：https://pan.baidu.com/s/1LPve8gaZK1LPUTthlmmcXw?pwd=lxkt，提取码为 `lxkt`
2. `pwkit_env.tar.gz` 中包含一个 Python 解释器，解释器内置Python库 `MaterSDK`

## 1.1. 安装步骤
```shell
# Step 1. 解压文件
$ cd pwkit
$ mkdir pwkit_env
$ tar -zxvf pwkit_env.tar.gz -C pwkit_env

# Step 2. 设置环境变量
$ export PWKIT_ROOT=<your_path>/pwkit
$ export PATH=<your_path>/pwkit/bin:$PATH

# Step 3. 设置`Python解释器`的路径 -- 修改 PYTHON_PATH
$ vim pwkit.cfg
#PYTHON_PATH = <your_path>/pwkit/pwkit_env/bin/python3
```

## 1.2. 卸载
```bash
$ rm -rf /share/app/pwkit
$ rm -rf $HOME/.local/pwkit
```


# 2. 使用方法 (On MCloud)
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