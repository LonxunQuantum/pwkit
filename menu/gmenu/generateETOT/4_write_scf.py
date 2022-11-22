#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import os
import joblib
from etotWriter import EtotWriter



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
    '''
    try: 
        etot_writer_path = os.path.join(os.getcwd(), "etot_writer.pkl")
        etot_writer = joblib.load(etot_writer_path)
    except:
        print("Error!!! check your input.")
    etot_writer.write_scf()


if __name__ == "__main__":
    write_scf()