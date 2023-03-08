import os
import sys
import joblib


def write_scf():
    '''
    Description
    -----------
        1. 向 `etot.input` 写入 `电子自洽设置`
    
    Example
    -------
    #电子自洽设置
    Ecut = 50
    MP_N123 = 12 12 1 0 0 0 0
    SCF_ITER0_1 = 6 4 3 0.0 0.025 1
    SCF_ITER0_2 = 94 4 3 1.0 0.025 1
    
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
    etot_writer.write_scf(density=density)


if __name__ == "__main__":
    write_scf()