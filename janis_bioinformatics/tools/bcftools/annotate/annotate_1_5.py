from bioinformatics.janis_bioinformatics.tools.bcftools.annotate.latest import BcfToolsAnnotateBase
from bioinformatics.janis_bioinformatics.tools.bcftools.bcftools_1_5 import BcfTools_1_5


class BcfToolsAnnotate_1_5(BcfTools_1_5, BcfToolsAnnotateBase):
    pass


if __name__ == "__main__":
    print(BcfToolsAnnotate_1_5().help())
