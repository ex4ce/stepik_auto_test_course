f = '1_2'
s = '1'
w = '3'


def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f'expected \'{substring}\' to be substring of \'{full_string}\''


def wrong_test(full, sub):
    assert sub in full, f'expected \'{sub}\' to be substring of \'{full}\''


if __name__ == '__main__':
    test_substring(f, s)
    wrong_test(f, w)
    print('All test passed')
