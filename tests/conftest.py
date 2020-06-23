import pytest
from os import listdir
from os.path import dirname, abspath, join
import numpy as np
import pandas as pd
import re
import reciprocalspaceship as rs
import gemmi

@pytest.fixture
def dataset_hkl():
    """
    Build DataSet for testing containing only Miller indices
    """
    hmin, hmax = -5, 5
    H = np.mgrid[hmin:hmax+1:2,hmin:hmax+1:2,hmin:hmax+1:2].reshape((3, -1)).T
    dataset = rs.DataSet({"H": H[:, 0], "K": H[:, 1], "L": H[:, 2]})
    dataset.set_index(["H", "K", "L"], inplace=True)
    return dataset

def load_dataset(datapath, as_gemmi=False):
    """
    Load dataset at given datapath. Datapath is expected to be a list of
    directories to follow.
    """
    inFN = abspath(join(dirname(__file__), *datapath))
    if as_gemmi:
        return gemmi.read_mtz_file(inFN)
    else:
        return rs.read_mtz(inFN)
    
@pytest.fixture
def data_hewl():
    """
    Load HEWL diffraction data from APS 24-ID-C
    """
    datapath = ["data", "algorithms", "HEWL_SSAD_24IDC.mtz"]
    return load_dataset(datapath)

@pytest.fixture
def data_gemmi():
    """
    Load HEWL diffraction data from APS 24-ID-C as gemmi.Mtz
    """
    datapath = ["data", "fmodel", "9LYZ.mtz"]
    return load_dataset(datapath, as_gemmi=True)

@pytest.fixture
def data_fmodel():
    """
    Load fmodel results for 9LYZ.mtz
    """
    datapath = ["data", "fmodel", "9LYZ.mtz"]
    return load_dataset(datapath)
    
def get_mtz_by_spacegroup():
    """
    Get absolute paths to MTZ files generated by phenix.fmodel for 
    testing crystallographic symmetry operations.
    """
    datadir = abspath(join(dirname(__file__) + '/data/fmodel/'))
    files = [join(datadir, i) for i in listdir(datadir) if re.match(r'.*(?<!_p1).mtz$', i)]
    return files


@pytest.fixture(params=get_mtz_by_spacegroup())
def mtz_by_spacegroup(request):
    """Yields paths to MTZ files for each crystallographic spacegroup"""
    return request.param

@pytest.fixture(params=[
    rs.HKLIndexDtype,                        # H
    rs.IntensityDtype,                       # J
    rs.StructureFactorAmplitudeDtype,        # F
    rs.AnomalousDifferenceDtype,             # D
    rs.StandardDeviationDtype,               # Q
    rs.StructureFactorAmplitudeFriedelDtype, # G
    rs.StandardDeviationSFFriedelDtype,      # L
    rs.IntensityFriedelDtype,                # K
    rs.StandardDeviationIFriedelDtype,       # M
    rs.ScaledStructureFactorAmplitudeDtype,  # E
    rs.PhaseDtype,                           # P
    rs.WeightDtype,                          # W
    rs.HendricksonLattmanDtype,              # A
    rs.BatchDtype,                           # B
    rs.M_IsymDtype,                          # Y
    rs.MTZIntDtype,                          # I
    rs.MTZRealDtype                          # R
])
def dtype_all(request):
    """Yields MTZ dtypes"""
    return request.param()
