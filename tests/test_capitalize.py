from scr.capitalize import capitalize


def test_capitalizer():
    assert capitalize('') == ''
    assert capitalize('hello') == 'Hello'
