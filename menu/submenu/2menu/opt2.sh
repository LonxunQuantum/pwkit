#!/bin/bash
submenu::2opt2() {
  # disorder
  cat <<EOF
This module is used to introduce how to use disorder code to generate irreducible site-occupancy
configurations file for PWmat. disorder is an open source software designed for generating
irreducible site-occupancy configurations (i.e., symmetrically inequivalent disordered crystal structures),
which can be used for disordered doping, including substitution doping and vacancy doping.
The disorder code works for arbitrary parent cells with any supercell expansion matrix,
and for any number of atomic types with arbitrary stoichiometry. Most important,
a linear scale of run time with the number of irreducible configurations is achieved,
which is the best possible scaling for this type of problem.（不可约无序掺杂构型产生程序）
EOF

exit 0
}
