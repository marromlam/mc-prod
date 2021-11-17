from GaudiConf import IOExtension
from Configurables import DaVinci

IOExtension().inputFiles([ "$input_file" ], clear=True)
# DaVinci().EvtMax = 1 # Number of events
# DaVinci().TupleFile = "$output_file"
# DaVinci().DatasetName = "$output_file".replace('.dst','')
# DaVinci().HistogramFile = "$output_file".replace('.dst','_histograms.root')
# DaVinci().outputFile = "$output_file".replace('.root','')
# DaVinci().ProductionType = 'Stripping'
DaVinci().Simulation = True
DaVinci().DataType = "$year"
# IOExtension().outStream("$output_file")
