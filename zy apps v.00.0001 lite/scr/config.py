import os

class cfgDir:
    basedir = os.getcwd()
    uidir = os.path.join(basedir, "UI")
    srcdir = os.path.join(basedir, "scr")
    dbdir = os.path.join(basedir, "db")
    csvdir = os.path.join(basedir, "csv")

class cfgInfo:
    APP_NAME = "Zy App"
    APP_VERSION = "V.00.001"
    # ud = Under Development, us = Unstable, s = Stable" 
    APP_STATUS = "ud" 
