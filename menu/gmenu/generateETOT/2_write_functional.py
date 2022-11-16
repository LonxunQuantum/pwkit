#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
from etotWriter import EtotWriter



def write_functional():
    '''
    Description
    -----------
        1. 向 `etot.input` 写入 `任务类型`
    
    Example
    -------
    1   4
    #基础设置
    JOB = SCF
    XCFUNCTIONAL = PBE
    ACCURACY = NORM
    CONVERGENCE = EASY
    PRECISION = AUTO
    '''
    etot_writer = EtotWriter()
    etot_writer.write_functional()


if __name__ == "__main__":
    write_functional()