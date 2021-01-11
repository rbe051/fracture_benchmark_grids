import porepy.io.gridWriter as ioWriter
import os

import case2.data as problem_data


def export_grid(path, mesh_id=1):
    case_folder = "case2/"
    mesh_sizes = ["mesh500.geo", "mesh4k.geo", "mesh32k.geo"]

    file_geo = case_folder  + mesh_sizes[mesh_id]

    gb = problem_data.import_grid(file_geo, 1e-8)
    gb = ioWriter.mergeGridsOfEqualDim(gb)

    ioWriter.dumpGridBucketToFile(gb, os.path.join(path, "benchmark3d_2.txt"))
