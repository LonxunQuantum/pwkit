import os
import sys
import joblib


def write_accuracy_and_scf():
    '''
    Description
    -----------
        1. 向 `etot.input` 写入 `收敛精度` 和 `电子自洽设置`
        
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
    etot_writer.write_scf(density=density)


if __name__ == "__main__":
    write_accuracy_and_scf()