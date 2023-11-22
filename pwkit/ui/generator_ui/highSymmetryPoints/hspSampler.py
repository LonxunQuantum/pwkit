import os
import sys
import subprocess
from typing import Union, Tuple
from matersdk.io.publicLayer.structure import DStructure
from matersdk.calculation.kpath.kpathSampler import KpathSampler

from ...ui_template import UITemplate, OPTTemplate
from ....variable import *


class HspSampler(OPTTemplate):
    def run(self):
        current_path:str = os.getcwd()
        
        ### Step 1.1. 读取结构文件名
        print("输入atom.config格式的文件名 (default: atom.config)")
        file_name = input("------------>>\n")
        if (file_name == ""):
            file_name = "atom.config"
        file_path = os.path.join(current_path, file_name)
        structure = DStructure.from_file(
                file_format="pwmat",
                file_path=file_path
        )
        
        ### Step 1.2. 读取材料的维度
        print("输入材料的维度 (2: 二维材料; 3: 三维材料):")
        dimension = input("------------>>\n")
        dimension = int(dimension)
        
        
        ### Step 1.3. 读取能带两点之间的密度（单位 2pi/埃）
        print("输入每条KPATH上的取点密度 (单位: 2*PI/Angstrom): ")
        density = input("------------>>\n")
        density = float(density)
        
        ### Step 2. Run
        kpath_sampler = KpathSampler(
                structure=structure,
                dimension=dimension,
                symprec=0.1,
                angle_tolerance=5,
                atol=1e-5
        )
        
        ### Step 2.1. Output HIGH_SYMMETRY_POINTS
        kpath_sampler.output_HIGHK_file()
        
        ### Step 2.2. Output gen.kpt
        kpath_sampler.output_gen_kpt(density=density)
        