#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import os
import joblib
from etotWriter import EtotWriter


def write_task():
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
    etot_writer.write_task()
    
    etot_writer_path = os.path.join(os.getcwd(), "etot_writer.pkl")
    if os.path.exists(etot_writer_path):
        os.remove(etot_writer_path)
    joblib.dump(etot_writer, etot_writer_path)


if __name__ == "__main__":
    write_task()