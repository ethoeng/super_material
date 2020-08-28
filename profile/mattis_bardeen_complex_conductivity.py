#!/usr/bin/env python3

from cProfile import Profile

from numpy import linspace

from material.gap_energy import BCSGapEnergy
from material.conductivity import MattisBardeenComplexConductivity


def run():
    gap_energy = BCSGapEnergy(1.5e-3, 2.3)
    conductivity = MattisBardeenComplexConductivity(gap_energy, 2.4e7)

    frequencies = linspace(10e9, 1500e9, 400)

    with Profile() as profile:
        for frequency in frequencies:
            conductivity.evaluate(4.2, frequency)

    profile.print_stats()


if __name__ == "__main__":
    run()