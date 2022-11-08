#!/bin/bash
msubmenue::opt2() {
  cat <<EOF
This module is used to introduce how to use PWmat to simulate Boltzman NAMD (Nonadiabatic Molecular Dynamics). NAMD simulation is a widely used approach to study carrier dynamic processes involving excited states, such as charge relaxation, recombination, and transport. In this Boltzman NAMD, we developed a new NAMD simulation method by modifying the conventional density matrix, it can incorporate the detailed balance and decoherence.（Boltzman NAMD 可以考虑退相干效应和细致平衡，PWmat自带的JOB=NAMD没有考虑退相干和细致平衡）
EOF

exit 0
}
