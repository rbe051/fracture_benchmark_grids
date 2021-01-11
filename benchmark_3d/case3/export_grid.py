import porepy.io.gridWriter as ioWriter
import os

import case3.data as problem_data


def export_grid(path, mesh_id=0):
    case_folder = "case3/"
    mesh_sizes = ["mesh30k.geo", "mesh140k.geo", "mesh323k.geo", "mesh454k.geo"]

    file_geo = case_folder  + mesh_sizes[0]
    gb, domain = problem_data.create_grid(file_geo)
    gb = ioWriter.mergeGridsOfEqualDim(gb)
    ioWriter.dumpGridBucketToFile(gb, os.path.join(path, "benchmark3d_3.txt"))
