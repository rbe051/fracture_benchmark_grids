import os
import porepy.io.gridWriter as ioWriter

import case4.data as problem_data

def export_grid(path):
    gb, domain = problem_data.create_grid(False, False)

    gb = ioWriter.mergeGridsOfEqualDim(gb)
    ioWriter.dumpGridBucketToFile(gb, os.path.join(path, "benchmark3d_4.txt"))
