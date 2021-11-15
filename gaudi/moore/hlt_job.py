from GaudiConf import IOExtension
from Configurables import Moore


IOExtension().inputFiles([ "$input_file" ], clear=True)
Moore().outputFile = "$output_file"

