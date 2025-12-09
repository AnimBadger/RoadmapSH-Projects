from start import handle_command

def test_exist_command_returns_false():
    assert handle_command('exit') is False

def test_non_exist_command_returns_true():
    assert handle_command('add') is True