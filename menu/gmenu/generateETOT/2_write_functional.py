#!/data/home/liuhanyu/anaconda3/envs/pwkit_env/bin/python
import os
import sys
import joblib
from etotWriter import EtotWriter


def write_functional():
    '''
    Description
    -----------
        1. 向 `etot.input` 写入 `泛函设置`
        2. 载入 `etot_writer` 对象后，再写入
    
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
    etot_writer.write_functional(functional_name=sys.argv[1])
    joblib.dump(etot_writer, etot_writer_path)


if __name__ == "__main__":
    write_functional()