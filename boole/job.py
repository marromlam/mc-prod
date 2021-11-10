from Configurables import Boole
from GaudiConf import IOHelper


IOHelper('ROOT').inputFiles([ "$input_file" ])
Boole().DatasetName = '$output_file'.replace('.digi','')

