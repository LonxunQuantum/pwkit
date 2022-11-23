# pwkit
kits for pwmat

### 安装
```shell
$ tar -zxvf pwkit.tar.gz -C /share/app
$ cp /share/app/pwkit/env/pwkit /share/app/modulefiles
```

### 使用
## 1. Now 
```bash
# Step 1. 设置环境变量
$ export PWKIT_ROOT=/data/home/liuhanyu/hyliu/code/pwkit
$ export SG15_DIR_PATH=/share/psp/NCPP-SG15-PBE
$ export PD04_DIR_PATH=/share/psp/NCPP-PD04-PBE

# Step 2. 设置 python 解释器的路径
$ find . -name "*.py" | xargs grep "#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3"
$ find . -name "*.py" | xargs sed -i 's:#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3:#!<your_python_path>:g'
```

## 2. In future
```bash
$ module load pwkit
$ which pwkit
```

### 卸载
```bash
rm -rf /share/app/pwkit
rm -rf $HOME/.local/pwkit
```