from pandas.core.dtypes.dtypes import register_extension_dtype

from reciprocalspaceship.dtypes.base import MTZInt32Dtype, MTZIntegerArray


@register_extension_dtype
class HKLIndexDtype(MTZInt32Dtype):
    """Custom MTZ Dtype for Miller indices"""

    name = "HKL"
    mtztype = "H"

    def is_friedel_dtype(self):
        return False

    @classmethod
    def construct_array_type(cls):
        return HKLIndexArray


class HKLIndexArray(MTZIntegerArray):
    _dtype = HKLIndexDtype()
    pass
