import sys
import warnings
from pflow.io.publicLayer.structure import DStructure
from pflow.calculation.kpath.kpathSampler import KpathSampler


warnings.filterwarnings("ignore")


class HighSymmetryPointsGenerator(object):
    def __init__(self,
                atom_config_path:str,
                symprec:float=0.1,
                angle_torlerance:float=5,
                atol:float=1e-5, 
                ):
        structure = DStructure.from_file(
                            file_path=atom_config_path,
                            file_format="pwmat",
                            coords_are_cartesian=False,
                            )
        self.kpath_sampler = KpathSampler(
                            structure=structure,
                            symprec=symprec,
                            angle_tolerance=angle_torlerance,
                            atol=atol,
                            )
    
    
    def output_gen_kpt_and_HIGHK(self,
                                density:float=0.01):
        # Output HIGHK
        self.kpath_sampler.output_HIGHK_file()
        # output gen.kpt
        self.kpath_sampler.output_gen_kpt(density=density)



if __name__ == "__main__":
    high_symmetry_points_generator = HighSymmetryPointsGenerator(
                                        atom_config_path=sys.argv[1],
                                        symprec=0.1,
                                        angle_torlerance=5,
                                        atol=1e-5,
                                        )
    # sys.argv[2] 定义 KPATH 各个路段的取点密度
    high_symmetry_points_generator.output_gen_kpt_and_HIGHK(
                                        density=float(sys.argv[2]),
                                        )