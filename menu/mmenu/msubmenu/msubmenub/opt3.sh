#!/bin/bash
msubmenub::opt3() {
  cat <<EOF
This module is used to introduce how to calculate charge trapping using DFT + Marcus theroy, including coupling constant between two states , reorganization energy and charge trapping rate calculations. When combined with charge patching method, this approach can be used to study large systems with tens of thousands of atoms. Charge transfer is an important process, describing one electron jumping from one localized state to another, which can happen between localized states (e.g., point defects), or extended state to localized state. It is a phonon assisted process, can be described by Landau-Zener transition, can also be calculated by Marcus theory, or multiphonon process.（如何计算电荷俘获）
EOF

exit 0
}
