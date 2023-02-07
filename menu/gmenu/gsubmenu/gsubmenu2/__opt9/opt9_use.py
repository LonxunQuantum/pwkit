import os 


def optc():
    '''
    Description
    -----------
        1. 将波函数转化到实空间
        2. 将波函数转化到实空间，然后用 VESTA 可以查看
        3. 使用 convert_realwg.x OUT.REAL.RHOWF_SP01 得到 xsf 格式文件可以用 VESTA 进行查看
    '''
    # e.g. OUT.REAL.RHOWF_SP01
    out_real_name = input(" 请输入波函数的文件名\n------------>>\n")
    os.system("convert_realwg.x {0}".format(out_real_name))


if __name__ == "__main__":
    optc()
