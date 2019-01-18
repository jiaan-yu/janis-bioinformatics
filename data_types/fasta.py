from Pipeline import File


class FastaFai(File):
    @staticmethod
    def name():
        return "FastaFai"

    @staticmethod
    def secondary_files():
        return [".fai"]


class Fasta(FastaFai):

    @staticmethod
    def name():
        return "Fasta"

    @staticmethod
    def secondary_files():
        return [".amb", ".ann", ".bwt", ".pac", ".sa", *super(Fasta).secondary_files()]


class FastaWithDict(Fasta):

    @staticmethod
    def name():
        return "FastaWithDict"

    @staticmethod
    def secondary_files():
        return [*Fasta.secondary_files(), "^.dict"]