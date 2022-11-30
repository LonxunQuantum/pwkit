# pwkit
Toolkits for pwmat

# 1. Installation
# 1.0. 需要准备的文件
1. `pwkit_env.tar.gz`: pwkit 的环境
2. `pwkit.tar.gz`: pwkit 软件包
3. `pflow.tar.gz`: pflow package 的软件包

## 1.1. Python 的 conda 环境配置
```shell
### Part I. 到新服务器下解压
# 1. 将 `pwkit_env` 环境解压到 `pwkit_env` 文件夹下
$ mkdir -p pwkit_env
$ tar -xzf pwkit_env.tar.gz -C pwkit_env
# 2. 激活 `pwkit_env` 环境
$ source pwkit_env/bin/activate
# 3. 安装 pflow 环境
(pwkit_env) $ cd pflow; pip install -e .
# 4. Run Python from in the environment
# (pwkit_env) $ python
```


## 1.2. pwkit 环境变量设置
```shell
# Step 1. 设置环境变量
(pwkit_env) $ export PWKIT_ROOT=/data/home/liuhanyu/hyliu/code/pwkit
(pwkit_env) $ export PATH=/data/home/liuhanyu/hyliu/code/pwkit/bin:$PATH
# Step 2. 找到 pwkit_env 环境的解释器的路径
(pwkit_env) $ old_python_path=`head -n 1 $PWKIT_ROOT/menu/gmenu/gmenu_cn.py`
(pwkit_env) $ new_python_path='#!'`python -c "import sys;print(sys.executable)"`
# Step 3. 设置 python 解释器的路径
# /data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
# 自动安装了 pymatgen, click, prettytable, joblib, linecache, conda-pack
$ find . -name "*.py" | xargs sed -i "s:${old_python_path}:${new_python_path}:g"
```


## 1.3. 卸载
```bash
rm -rf /share/app/pwkit
rm -rf $HOME/.local/pwkit
```



# 2. 使用方法
```shell
# 加载环境
$ module load pwkit/1.0
$ source /share/app/anaconda3/etc/profile.d/conda.sh
$ conda activate pwkit

# 调用 pwkit
$ pwkit
 _ ____      ___ __ ___   __ _| |_
| '_ \ \ /\ / / '_ ` _ \ / _` | __|  website: http://www.lonxun.com
| |_) \ V  V /| | | | | | (_| | |_   v1.0.0
| .__/ \_/\_/ |_| |_| |_|\__,_|\__|  pwmat kit Usage: pwkit -h
|_|

# 退出环境
$ conda deactivate
```