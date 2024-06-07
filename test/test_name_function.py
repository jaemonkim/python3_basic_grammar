from name_function import get_formatted_name
def test_first_last_name():
    """do names like janis joplin work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'