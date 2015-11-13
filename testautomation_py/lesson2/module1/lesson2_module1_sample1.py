import javabridge


def test_java_bridge():
    javabridge.start_vm(run_headless=True)
    try:
        print(javabridge.run_script('java.lang.String.format("Hello, %s!", name);', dict(name='world')))
    finally:
        javabridge.kill_vm()