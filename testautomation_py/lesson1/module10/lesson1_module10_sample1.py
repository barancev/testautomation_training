import subprocess


def test_command_line_utility():
    p = subprocess.Popen(["ls", "~"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    res = p.stdout.read()
    print(res.decode())
