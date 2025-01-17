from pandas.core.dtypes.dtypes import register_extension_dtype

from reciprocalspaceship.dtypes.base import MTZFloat32Dtype, MTZFloatArray


@register_extension_dtype
class StructureFactorAmplitudeDtype(MTZFloat32Dtype):
    """Dtype for structure factor amplitude  data"""

    name = "SFAmplitude"
    mtztype = "F"

    def is_friedel_dtype(self):
        return False

    @classmethod
    def construct_array_type(cls):
        return StructureFactorAmplitudeArray


class StructureFactorAmplitudeArray(MTZFloatArray):
    """ExtensionArray for supporting StructureFactorAmplitudeDtype"""

    _dtype = StructureFactorAmplitudeDtype()
    pass


@register_extension_dtype
class FriedelStructureFactorAmplitudeDtype(MTZFloat32Dtype):
    """
    Dtype for structure factor amplitude data from Friedel pairs --
    F(+) or F(-)
    """

    name = "FriedelSFAmplitude"
    mtztype = "G"

    def is_friedel_dtype(self):
        return True

    @classmethod
    def construct_array_type(cls):
        return FriedelStructureFactorAmplitudeArray


class FriedelStructureFactorAmplitudeArray(MTZFloatArray):
    """ExtensionArray for supporting FriedelStructureFactorAmplitudeDtype"""

    _dtype = FriedelStructureFactorAmplitudeDtype()
    pass


@register_extension_dtype
class NormalizedStructureFactorAmplitudeDtype(MTZFloat32Dtype):
    """Dtype for normalized structure factor amplitude data"""

    name = "NormalizedSFAmplitude"
    mtztype = "E"

    def is_friedel_dtype(self):
        return False

    @classmethod
    def construct_array_type(cls):
        return NormalizedStructureFactorAmplitudeArray


class NormalizedStructureFactorAmplitudeArray(MTZFloatArray):
    """ExtensionArray for supporting NormalizedStructureFactorAmplitudeDtype"""

    _dtype = NormalizedStructureFactorAmplitudeDtype()
    pass
