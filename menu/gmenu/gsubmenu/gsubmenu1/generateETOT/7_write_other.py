import os
import joblib
from etotWriter import EtotWriter



def write_other():
    '''
    Description
    -----------
        1. 向 `etot.input` 写入 `其他设置`
    
    Example
    -------
    ### 其他设置
    #COULOMB = 13 XX 偶极矩修正
    #CHARGE_DECOMP = T
    #NUM_BAND = XX
    #SYMM_PREC = 1E-5
    '''
    try: 
        etot_writer_path = os.path.join(os.getcwd(), "etot_writer.pkl")
        etot_writer = joblib.load(etot_writer_path)
    except:
        print("Error!!! check your input.")
    etot_writer.write_other()


if __name__ == "__main__":
    write_other()