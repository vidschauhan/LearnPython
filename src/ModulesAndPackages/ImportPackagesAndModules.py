# Created by vidit.singh at 04-03-2022
# To access the packages right click on package directory -> Mark Directory as Source Root
# Make sure your package and sub packages have __init__.py file.
import src
from src.mainpackage.subpackage import SubScript

print(SubScript.my_sub_script())

from src.mainpackage import MainScript

print(src.mainpackage.MainScript.get_main_script())
