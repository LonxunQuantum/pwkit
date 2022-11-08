#!/bin/bash
msubmenuh::opt1() {
  cat <<EOF
This module is used to introduce how to use charge patching method to simulate large systems (atoms > 10000). Charge patching method is based on the assumption that the charge density around an atom is mainly determined by its local environment. In this approach, on first do a direct density functional theory (DFT) calculation for some small systems and decompose their charge density into charge motifs assigned to each atom. The total charge density of the large system of interest is then constructed by reassembling the charge motifs, and is used to generate the DFT hamiltonian. It has been shown the CPM gives almost identical results as direct ab initio calculations.（使用CPM方法计算大体系，比如量子点、磨角石墨烯）
EOF

exit 0
}
