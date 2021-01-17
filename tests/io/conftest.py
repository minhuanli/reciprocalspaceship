import pytest
from os.path import dirname, abspath, join

@pytest.fixture
def IOtest_hkl():
    """
    Path to Precognition .hkl file for I/O testing
    """
    datapath = join(abspath(dirname(__file__)), "../data/precognition")
    return  join(datapath, "hewl.hkl")

@pytest.fixture
def IOtest_ii():
    """
    Path to Precognition .ii file for I/O testing
    """
    datapath = join(abspath(dirname(__file__)), "../data/precognition")
    return  join(datapath, "e074a_off1_001.mccd.ii")

@pytest.fixture
def IOtest_mtz():
    """
    Path to MTZ file for I/O testing
    """
    datapath = join(abspath(dirname(__file__)), "../data/fmodel")
    return join(datapath, "9LYZ.mtz")
