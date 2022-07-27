with open("practice.txt", "r") as f:
    lines = f.readlines()

with open("3043210_siuksles.txt", "r") as f:
    siuksles = f.readlines()

def remove_all_trash(sarasas, trashs):
    for trash in trashs:
        while trash in sarasas:
            lines.remove(trash)

            
remove_all_trash(lines, siuksles)
