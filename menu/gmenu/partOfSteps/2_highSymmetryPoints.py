from pflow.io.publicLayer.structure import DStructure
from pflow.calculation.kpath.kpathSampler import KpathSampler


class HighSymmetryPointsGenerator(object):
    def __init__(self,
                atom_config_path:str,
                symprec:float=0.1,
                angle_tolerance:float=5,
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
                            angle_tolerance=angle_tolerance,
                            atol=atol,
                            )
    
    
    def output_gen_kpt_and_HIGHK(self,
                            density:float=0.01,
                            ):
        # Output HIGHK
        self.kpath_sampler.output_HIGHK()
        # Ouput gen.kpt
        self.kpath_sampler.output_gen_kpt(density=density)

if __name__ == "__main__":
    pass