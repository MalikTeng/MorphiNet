"""
    read the array of vertices from template/verts-control_mesh.txt and faces from template/faces-control_mesh.txt and create a control mesh,
    convert the polygonal mesh to a triangular mesh using triangulation and save the mesh as a control_mesh_v1.obj file
"""
import numpy as np
import trimesh
from trimesh import load_mesh

verts = np.loadtxt('template/verts-control_mesh.txt').astype(np.float32)
faces = np.loadtxt('template/faces-control_mesh.txt').astype(np.int64) - 1

faces = np.concatenate(
    [faces[:, [0, 1, 2]], faces[:, [2, 3, 0]]],
    axis=0
)

control_mesh = trimesh.Trimesh(vertices=verts, faces=faces)
control_mesh.export('template/control_mesh_v1.obj')

# load the updated control mesh resulting from the triangulation and connecting dots in Blender
control_mesh = load_mesh('template/control_mesh_v2.obj')
