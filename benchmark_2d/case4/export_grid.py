import porepy as pp
import porepy.io.gridWriter as ioWriter
import os

def export_grid(path):
    mesh_kwargs = {"mesh_size_frac": 5, "mesh_size_min": 5}
    domain = {"xmin": 0, "xmax": 700, "ymin": 0, "ymax": 600}

    network = pp.fracs.fracture_importer.network_2d_from_csv("case4/network.csv", domain=domain)

    gb = network.mesh(mesh_kwargs)
    gb = ioWriter.mergeGridsOfEqualDim(gb)

    ioWriter.dumpGridBucketToFile(gb, os.path.join(path, "benchmark4.txt"))
