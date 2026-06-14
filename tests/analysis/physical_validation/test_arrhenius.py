import numpy as np

from src.analysis.physical_validation.arrhenius import fit_arrhenius, within_literature_band


def test_recovers_known_activation_energy():
    R = 8.314
    ea_true = 50_000.0
    t_k = np.linspace(298, 363, 12)
    k = np.exp(-ea_true / (R * t_k)) * 1e8
    fit = fit_arrhenius(t_k, k)
    assert abs(fit.ea_j_mol - ea_true) / ea_true < 0.05
    assert fit.r2 > 0.99


def test_band_check():
    assert within_literature_band(50_000) is True
    assert within_literature_band(500_000) is False
