import sys
import config

sys.path.insert(0, config.appPath())
from project import app as application
