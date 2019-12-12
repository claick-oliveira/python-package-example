import python_package.package as package


def test_main():
    msg = package.main()
    right_msg = 'Python package example!'
    assert msg == right_msg, 'This is a dummy test!'
