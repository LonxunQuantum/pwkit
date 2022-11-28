# pwkit
kits for pwmat

### 安装
```shell
$ tar -zxvf pwkit.tar.gz -C /share/app
$ cp /share/app/pwkit/env/pwkit /share/app/modulefiles
```

### 使用 (Before)
## 1. Now 
```bash
# Step 1. 设置 python 解释器的路径
$ find . -name "*.py" | xargs grep "#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3"
$ find . -name "*.py" | xargs sed -i 's:#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3:#!<your_python_path>:g'

# Step 2. 设置环境变量
$ export PWKIT_ROOT=/data/home/liuhanyu/hyliu/code/pwkit
$ cp $PWKIT_ROOT/pwkit.cfg ~/.pwkit.cfg
$ source ~/.pwkit.cfg
```

## 2. In future
```bash
$ module load pwkit
$ which pwkit
```

## 3. 卸载
```bash
rm -rf /share/app/pwkit
rm -rf $HOME/.local/pwkit
```



# 1. Installation
## 1.1. Python 环境打包与安装
```shell
### Part I. 打包 pwkit 的conda环境
$ conda pack -n pwkit -o pwkit.tar.gz --ignore-editable-packages

### Part II. 到新服务器下解压
# Unpack environment into directory `pwkit`
$ mkdir -p pwkit
$ tar -xzf pwkit.tar.gz -C pwkit

## Way 1.
# Use Python without activating or fixing the prefixes. Most Python
# libraries will work fine, but things that require prefix cleanups
# will fail.
$ ./pwkit/bin/python

## Way 2. The most common way
# Activate the environment. This adds `my_env/bin` to your path
$ source my_env/bin/activate
# Run Python from in the environment
(my_env) $ python

## Way 3.
# Cleanup prefixes from in the active environment.
# Note that this command can also be run without activating the environment
# as long as some version of Python is already installed on the machine.
(my_env) $ conda-unpack
```

## 1.2. pwkit 环境变量设置
```shell
# Step 1. 设置环境变量
$ export PWKIT_ROOT=/data/home/liuhanyu/hyliu/code/pwkit
$ cp $PWKIT_ROOT/pwkit.cfg ~/.local/pwkit
$ source ~/.local/pwkit

# Step 2. 设置 python 解释器的路径
$ find . -name "*.py" | xargs grep "#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3"
$ find . -name "*.py" | xargs sed -i 's:#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3:#!<your_python_path>:g'
```

## 1.3. 卸载
```bash
rm -rf /share/app/pwkit
rm -rf $HOME/.local/pwkit
```