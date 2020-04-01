import os
f = open('start_render.bat', 'w')

path_list = ['',                                           # 0
             'my_manim_projects\\',                        # 1
             'my_manim_projects\\my_projects\\',           # 2
             'my_manim_projects\\test\\',                  # 3
             'manim_sandbox\\utils\\',                     # 4
             'my_manim_projects\\my_utils\\',              # 5
             ]

py_file_name = path_list[5] + 'test_3D.py'
classname = 'Play_rubic_order3'

pl = '-pl'
pm = '-pm'
high = '--high_quality'

str01 = 'python -m manim ' + py_file_name + ' ' + classname + ' ' + pm # high # + ' -p'
f.write(str01)
f.close()
os.system('start_render.bat')
