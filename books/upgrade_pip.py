import os
import time


def upgrade_pip_all():
    default_back_input = ' --upgrade'
    default_forward_input = 'pip install '
    cmd_lines = []

    with open('requirements.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            cmd_lines.append(default_forward_input + line.strip('\n') + default_back_input)

    for cmd_line in cmd_lines:
        os.system(cmd_line)
        time.sleep(3.0)
        print(f'### {cmd_line} ...done! ###\n')


upgrade_pip_all()
