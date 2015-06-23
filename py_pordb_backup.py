# usr bin python3
# -*- coding: utf-8 -*-

import sys
import os
import subprocess

DBNAME = "por"
verzeichnis = os.path.expanduser("~") +os.sep +"Dokumente"

subprocess.check_output(["/usr/bin/vacuumdb", "--analyze", "por"], universal_newlines=True)
subprocess.check_output(["pg_dump", DBNAME, "-f", os.path.join(verzeichnis, DBNAME + ".sql")], universal_newlines=True)