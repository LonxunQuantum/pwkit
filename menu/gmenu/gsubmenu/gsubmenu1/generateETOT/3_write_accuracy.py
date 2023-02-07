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
        
    sys.argv
    --------
        1. sys.argv[1]: KMesh 的 density -- 用于填写 MP_N123
    '''
    try:
        etot_writer_path = os.path.join(os.getcwd(), "etot_writer.pkl")
        etot_writer = joblib.load(etot_writer_path)
    except:
        print("Error!!! check your input.")
        
        
    # 1. 任务类型为 nonscf 时，若按照高对称点确定KPoints，$density_in_2pi 是空的
    try:
        density = float( sys.argv[1] )
    except IndexError:  # IndexError: 有些任务比如NS，不需要填写density_in_2pi, 
                        # 因此不会向Python脚本传入参数，因此sys.argv[1]会引发错误
        density = False
    etot_writer.write_accuracy(density=density)


if __name__ == "__main__":
    write_accuracy()