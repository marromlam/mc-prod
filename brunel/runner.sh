source /cvmfs/lhcb.cern.ch/lib/LbEnv
lb-set-platform x86_64-slc6-gcc49-opt

lb-run Brunel/${BRUNEL_VERSION} gaudirun.py ${APPCONFIGOPTS}/Brunel/DataType-${YEAR}.py \
                               ${APPCONFIGOPTS}/Brunel/MC-WithTruth.py \
                               ${APPCONFIGOPTS}/Brunel/SplitRawEventOutput.4.3.py \
                               ${APPCONFIGOPTS}/Persistency/Compression-ZLIB-1.py \
                               ${JOB_FILE} \
                               Tags.py

