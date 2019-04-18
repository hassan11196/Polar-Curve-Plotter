# -*- mode: python -*-

import sys
sys.setrecursionlimit(5000)
block_cipher = None

added_files = [
               ('C:\\Users\\Hassan\\Desktop\\Programs\\C++\\GUI\\qt\\practice\\python\\base1.ui', '.'),
               ('C:\\Users\\Hassan\\Desktop\\Programs\\C++\\GUI\\qt\\practice\\python\\if_chart02_64_201480.ico', '.')
              ]


a = Analysis(['PolarCurvePlotProject_v1.1.py'],
             pathex=['C:\\Users\\Hassan\\Desktop\\Programs\\C++\\GUI\\qt\\python\\PolarCurvePlotProject_v1.1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='PolarCurvePlotProject_v1.1',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='PolarCurvePlotProject_v1.1')
