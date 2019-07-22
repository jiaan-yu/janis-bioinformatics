from abc import abstractmethod, ABC
from typing import List

from janis_bioinformatics.data_types import Vcf, CompressedVcf
from janis_bioinformatics.tools import BioinformaticsTool
from janis_core import ToolOutput, ToolInput, Boolean, Int, File
from janis_core import Stdout
from janis_core import ToolMetadata


class BGZipBase(BioinformaticsTool, ABC):
    @staticmethod
    def tool_provider():
        return "htslib"

    @staticmethod
    def tool():
        return "bgzip"

    @staticmethod
    def base_command():
        return "bgzip"

    def inputs(self) -> List[ToolInput]:
        return [
            ToolInput("file", Vcf(), position=100, doc="File to bgzip compress"),
            *self.additional_args,
        ]

    def outputs(self) -> List[ToolOutput]:
        return [
            ToolOutput(
                "out",
                Stdout(CompressedVcf(), stdoutname="$(inputs.file.basename + '.gz')"),
            )
        ]

    def friendly_name(self):
        return "BGZip"

    def metadata(self):
        from datetime import date

        return ToolMetadata(
            creator="Michael Franklin",
            maintainer="Michael Franklin",
            maintainerEmail="michael.franklin@petermac.org",
            dateCreated=date(2018, 12, 24),
            dateUpdated=date(2019, 1, 24),
            institution="HTSLib",
            doi=None,
            citation=None,  # "",
            keywords=["htslib", "bgzip", "compression"],
            documentationUrl="http://www.htslib.org/doc/bgzip.html",
            documentation="""bgzip – Block compression/decompression utility

Bgzip compresses files in a similar manner to, and compatible with, gzip(1). The file is compressed 
into a series of small (less than 64K) 'BGZF' blocks. This allows indexes to be built against the 
compressed file and used to retrieve portions of the data without having to decompress the entire file.

If no files are specified on the command line, bgzip will compress (or decompress if the -d option is used) 
standard input to standard output. If a file is specified, it will be compressed (or decompressed with -d). 
If the -c option is used, the result will be written to standard output, otherwise when compressing bgzip 
will write to a new file with a .gz suffix and remove the original. When decompressing the input file must 
have a .gz suffix, which will be removed to make the output name. 
Again after decompression completes the input file will be removed.""".strip(),
        )

    @staticmethod
    @abstractmethod
    def docker():
        raise Exception(
            "An error likely occurred when resolving the method order for docker for the tabix classes "
            "or you're trying to execute the docker method of the base class (ie, don't do that). "
            "The method order resolution must preference BwaBase subclasses, "
            "and the subclass must contain a definition for docker."
        )

    additional_args = [
        ToolInput(
            "offset",
            Int(optional=True),
            prefix="--offset",
            doc="b: Decompress to standard output from virtual file position "
            "(0-based uncompressed offset). Implies -c and -d.",
        ),
        ToolInput(
            "stdout",
            Boolean(optional=True),
            default=True,
            prefix="--stdout",
            doc="c: Write to standard output, keep original files unchanged.",
        ),
        ToolInput(
            "decompress",
            Boolean(optional=True),
            prefix="--decompress",
            doc="d: Decompress.",
        ),
        ToolInput(
            "force",
            Boolean(optional=True),
            prefix="--force",
            doc="f: Overwrite files without asking.",
        ),
        ToolInput(
            "help",
            Boolean(optional=True),
            prefix="--help",
            doc="h: Displays a help message.",
        ),
        ToolInput(
            "index",
            Boolean(optional=True),
            prefix="--index",
            doc="i: Create a BGZF index while compressing. Unless the -I option is used, "
            "this will have the name of the compressed file with .gzi appended to it.",
        ),
        ToolInput(
            "indexName",
            File(optional=True),
            prefix="--index-name",
            doc="-I: Index file name.",
        ),
        ToolInput(
            "compress",
            Int(optional=True),
            prefix="--compress",
            doc="l: Compression level to use when compressing. From 0 to 9, or -1 "
            "for the default level set by the compression library. [-1]",
        ),
        ToolInput(
            "reindex",
            Boolean(optional=True),
            prefix="--reindex",
            doc="r: Rebuild the index on an existing compressed file.",
        ),
        ToolInput(
            "rebgzip",
            Boolean(optional=True),
            prefix="--rebgzip",
            doc="g: Try to use an existing index to create a compressed file with matching block offsets. "
            "Note that this assumes that the same compression library and level are in use "
            "as when making the original file. Don't use it unless you know what you're doing.",
        ),
        ToolInput(
            "size",
            Int(optional=True),
            prefix="--size",
            doc="s: Decompress INT bytes (uncompressed size) to standard output. Implies -c.",
        ),
        ToolInput(
            "threads",
            Int(optional=True),
            prefix="--threads",
            doc="@: Number of threads to use [1].",
        ),
    ]
