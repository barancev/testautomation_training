import pexpect


def test_interactive_command_line():
    p = pexpect.spawn("telnet localhost 4555")
    p.expect("Login id:")
    p.sendline("root")
    p.expect("Password:")
    p.sendline("root")
    p.expect("Welcome root. HELP for a list of commands")
    p.sendline("listusers")
    p.expect("Existing accounts (\d+)")
    assert int(p.match.group(1)) == 3
    p.sendline("quit")
    p.expect(pexpect.EOF)
