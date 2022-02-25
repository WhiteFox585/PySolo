import sys, os
import tempfile
import venv
import subprocess
import shutil


tmp = tempfile.gettempdir()  #literally tmp directory, can be custom
os.makedirs(tmp, exist_ok=True)
tempdir = tempfile.mkdtemp(dir=tmp)
venv.create(tempdir, with_pip=True)
subprocess.run(f"{tempdir}/bin/pip3 install pyfiglet", shell=True)

if len(sys.argv) == 1:
    subprocess.run(f"{tempdir}/bin/python3 -m figdate", shell=True)
elif len(sys.argv) == 2:
    subprocess.run(f"{tempdir}/bin/python3 -m figdate \"{sys.argv[1]}\"", shell=True)
elif len(sys.argv) == 3:
    subprocess.run(f"{tempdir}/bin/python3 -m figdate \"{sys.argv[1]}\" \"{sys.argv[2]}\"", shell=True)
else:
    print("ERROR! Wrong arguments count.")

shutil.rmtree(tempdir)  # deletes only subdirectory of this directory


