import os
import re

def generate_all_ui2py_and_all_qrc2py(path: str):
    files = os.listdir(path)
    ui_list = []
    ui_pattern = re.compile(r'.*\.ui')
    
    qrc_list = []
    qrc_pattern = re.compile(r'.*\.qrc')
    try:
        for item in files:
            if ui_pattern.match(item):
                ui_list.append(item)
            elif qrc_pattern.match(item):
                qrc_list.append(item)
        
        if ui2py:
            if ui_list == []:
                raise Exception(".ui files not found in current directory")
            
            for item in ui_list:
                filepath = os.path.join(path, item)
                file_name_without_ext = item.removesuffix('.ui')
                cmd = f'pyside6-uic "{filepath}" > "{path}{os.sep}{file_name_without_ext}.py"'
                os.popen(cmd)

        if qrc2py:
            if qrc_list == []:
                raise Exception(".qrc files not found in current directory")
            
            for item in qrc_list:
                filepath = os.path.join(path, item)
                file_name_without_ext = item.removesuffix('.qrc')
                cmd = f'pyside6-rcc "{filepath}" > "{path}{os.sep}{file_name_without_ext}_rc.py"'
                os.popen(cmd)

    except Exception as e:
        print(e)
    else:
        print('Convertation successful!')

if __name__ == '__main__':
    ui2py = True
    qrc2py = False
    path = os.path.dirname(os.path.abspath(__file__))
    generate_all_ui2py_and_all_qrc2py(path)