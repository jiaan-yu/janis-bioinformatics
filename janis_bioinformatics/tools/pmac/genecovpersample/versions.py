from janis_bioinformatics.tools.pmac.genecovpersample.base import (
    GeneCoveragePerSampleBase,
)
from janis_bioinformatics.tools.pmac.versions import (
    PeterMacUtils_0_0_7,
    PeterMacUtils_dev,
)


class GeneCoveragePerSample_0_0_7(GeneCoveragePerSampleBase, PeterMacUtils_0_0_7):
    pass


class GeneCoveragePerSample_dev(GeneCoveragePerSampleBase, PeterMacUtils_dev):
    pass


GeneCoveragePerSampleLatest = GeneCoveragePerSample_0_0_7
# GeneCoveragePerSampleLatest = GeneCoveragePerSample_dev