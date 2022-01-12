##################################
#
# RUN WITH THE FOLLOWING COMMAND: python3 Excecuter.py
##############

import PyInstaller.__main__
import os
    
folder  =  '/Users/davidhuijser/Documents/Freelance Work/Elaine - March 2021/Test/TestPyInstaller'
    
#PyInstaller.__main__.run([  
 #    'name-%s%' % 'myfile',
  #   '--onefile',
  #   '--windowed',
   #  os.path.join(folder, 'GUI.py'), """your script and path to the script"""                                        
  #   ])


PyInstaller.__main__.run([
    'Simple_GUI.py',
    '--onefile',
    '--windowed'
])
