import os
f = open('start_render.bat', 'w')

path_list = ['',                                           # 0
             'my_manim_projects\\',                        # 1
             'my_manim_projects\\my_projects\\',           # 2
             'my_manim_projects\\test\\',                  # 3
             'manim_sandbox\\utils\\',                     # 4
             'my_manim_projects\\my_utils\\',              # 5
             'my_manim_projects\\my_projects\\manim_code_by_manim\\',            # 6
             'manim_sandbox\\videos\\HomeworkVol05\\',                           # 7
             'others\\',                                   # 8
             'my_manim_projects\\my_projects\\fractal\\',            # 9
             'manim_sandbox\\utils\\mobjects\\',                     # 10
             ]

py_file_name = path_list[3] + 'Text_test.py'
classname = 'Test_02'

pl = '-pl'
pm = '-pm'
high = '--high_quality'
uhd = '-uhd'

str01 = 'python -m manim ' + py_file_name + ' ' + classname + ' ' + uhd # high + ' -s'# + ' -t'
f.write(str01)
f.close()
os.system('start_render.bat')
