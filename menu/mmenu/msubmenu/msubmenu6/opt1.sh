#!/bin/bash
msubmenu6::opt1() {
  cat <<EOF
This module is the interface between PWmat and Phonopy. Phonopy is an open source package for
phonon calculations at harmonic and quasi-harmonic levels. It can be used to calculate phonon
band structures, phonon DOS and partial DOS, phonon thermal properties, etc.
The most important thing is that this module can calculate the phonon of the defect
system and the phonon modes of subsystem.（算声子谱，缺陷声子谱，部分原子声子谱）
EOF

exit 0
}
