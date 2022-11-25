#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import os
import sys
import joblib
from etotWriter import EtotWriter



def write_accuracy():
    '''
    Description
    -----------
        1. 向 `etot.input` 写入 `收敛精度`
    
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
    try:
        etot_writer_path = os.path.join(os.getcwd(), "etot_writer.pkl")
        etot_writer = joblib.load(etot_writer_path)
    except:
        print("Error!!! check your input.")
    etot_writer.write_accuracy(density=float( sys.argv[1] ))


if __name__ == "__main__":
    write_accuracy()