import porepy.io.gridWriter as ioWriter
import os

import case1.data as problem_data

def export_grid(path, cartesian=False):
    mesh_size = 0.025
    data = {"mesh_size": mesh_size}

    gb = problem_data.import_grid(data, cartesian)
    gb = ioWriter.mergeGridsOfEqualDim(gb)

    ioWriter.dumpGridBucketToFile(gb, os.path.join(path, "benchmark1.txt"))
