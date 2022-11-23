#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import os
import joblib
from etotWriter import EtotWriter



def write_scf():
    '''
    Description
    -----------
        1. 向 `etot.input` 写入 `特殊设置`
    
    Example
    -------
    #特殊设置

    '''
    try: 
        etot_writer_path = os.path.join(os.getcwd(), "etot_writer.pkl")
        etot_writer = joblib.load(etot_writer_path)
    except:
        print("Error!!! check your input.")
    etot_writer.write_specific()
    joblib.dump(etot_writer, etot_writer_path)


if __name__ == "__main__":
    write_scf()