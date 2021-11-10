from GaudiConf import IOExtension
from Configurables import L0App


IOExtension().inputFiles([ "$input_file" ], clear=True)
L0App().outputFile = "$output_file"

