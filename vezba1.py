import os
def size_mb(file_path):
    x=os.path.getsize(file_path)
    return x/(1024*1024)

sizemb=size_mb('/home/irida/py_scripts/jupyteri_studenti_vezbe23/studenti_programiranje2/basic_part1/1VasPrviProgram.ipynb')
print(f"Velicina fajla je {sizemb:.2f} MB")