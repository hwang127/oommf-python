import mesh

def test_Mesh():
    a = mesh.Mesh(10, 20, 30, 1, 2, 3)
    assert a.mesh_info() == (10, 20, 30, 1, 2, 3)

