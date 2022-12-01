import os
import sys
import joblib
from etotWriter import EtotWriter



def write_specific():
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
    # 1. 特殊设置选择 `恒电势计算` 时，才会输入 sys.argv[2], sys.argv[3]
    # 2. 特殊设置选择 `恒电势计算` 时，才会输入 sys.argv[2]
    etot_writer.write_specific()
    etot_writer.dump_to_json()
    
    
    
    
    #joblib.dump(etot_writer, etot_writer_path)


if __name__ == "__main__":
    write_specific()