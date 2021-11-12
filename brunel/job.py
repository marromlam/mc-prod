from Configurables import Brunel
from GaudiConf import IOHelper


IOHelper('ROOT').inputFiles([ "$input_file" ], clear=True)
Brunel().DatasetName = "$output_file".replace('.dst','')
Brunel().DataType = "$year"
Brunel().InputType = 'DIGI'
Brunel().WithMC = True   # use the MC truth information in the digi file
