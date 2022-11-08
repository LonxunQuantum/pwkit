#!/bin/bash
msubmenu3::opt1() {
  cat <<EOF
This module is the interface between PWmat and RINGS (Rigorous Investigation of Networks Generated using Simulations).
RINGS is a scientific code developed in Fortran90/MPI to analyze the results of molecular dynamics simulations.
Using the R.I.N.G.S. code you can compute: Radia distribution functions; Simulated neutron and X-rays structure factors;
Mean Square Displacement; Bond angles and dihedral angles distribution; Bond properties;
Structural environments distribution; Voids distribution; Very detailed ring statistics analysis;
Various inputs files for 3D visualization using OpenDX.（分子动力学数据分析软件，可以分析键长键角等非常多信息）
EOF

exit 0
}
