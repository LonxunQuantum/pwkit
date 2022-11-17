#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import sys


class Warning(object):
    @staticmethod
    def kmesh_warning():
        print("+{0:-^58}+".format("Warm Tips"))
        print("\t* Accuracy Levels: Gamma-Only: 0;")
        print("\t                   Low:        0.06~0.04;")
        print("\t                   Medium:     0.04~0.03")
        print("\t                   Fine:       0.02~0.01")
        print("\t* 0.03~0.04 is Generally Precise Enough!")
        print("+{0:-^58}+".format("---------"))


if __name__ == "__main__":
    if sys.argv[1] == "kmesh_warning":
        Warning.kmesh_warning()