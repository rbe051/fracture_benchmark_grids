import numpy as np
import porepy as pp
import porepy.io.gridWriter as ioWriter
import os


def create_gb(file_name, mesh_size):
    domain = {"xmin": 0, "xmax": 1, "ymin": 0, "ymax": 1}
    network = pp.fracture_importer.network_2d_from_csv(file_name, domain=domain)
    mesh_kwargs = {"mesh_size_frac": mesh_size, "mesh_size_min": mesh_size / 20}
    return network.mesh(mesh_kwargs)

def export_grid(path):
    mesh_size = np.power(2., -4)
    file_name = "case1/network.csv"
    gb = create_gb(file_name, mesh_size)

    gb = ioWriter.mergeGridsOfEqualDim(gb)
    ioWriter.dumpGridBucketToFile(gb, os.path.join(path, "benchmark3.txt"))
