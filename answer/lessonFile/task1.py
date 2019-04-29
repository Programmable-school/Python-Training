"""
課題 ファイルの入出力
"""

import os, subprocess


dir_path =  os.path.dirname(os.path.abspath(__file__))
dir1 = dir_path + '/Dir'
dir2 = dir1 + '/Child'
dir1_file1 = dir1 + '/file.py'
dir2_file1 = dir2 + '/__init__.py'
dir2_file2 = dir2 + '/file.py'

os.makedirs(dir1, exist_ok=True)
os.makedirs(dir2, exist_ok=True)

f1 = open(dir1_file1, 'w')
f1.write('print(\'Hello world\')')

f2 = open(dir2_file1, 'w')
f2.write('# none')

f3 = open(dir2_file2, 'w')
f3.write('print(\'Hello world\')')

f1.close
f2.close
f3.close

# 実行
subprocess.run(['tree', dir_path])
