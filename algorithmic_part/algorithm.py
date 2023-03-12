def check_relation(net, first, second):
    friends = _make_friends_dict(net)
    return _breadth_first_search(friends, first, second)


def _make_friends_dict(net):
    """function for making friends graph"""

    friends = {}

    for connection in net:
        friend1, friend2 = connection
        if friend1 not in friends:
            friends[friend1] = set()
        if friend2 not in friends:
            friends[friend2] = set()
        friends[friend1].add(friend2)
        friends[friend2].add(friend1)

    return friends


def _breadth_first_search(friends, first, second):
    """breadth first search algorithm"""

    queue = [first]
    visited = set()
    while queue:
        user = queue.pop(0)
        if user == second:
            return True
        visited.add(user)
        for friend in friends[user]:
            if friend not in visited:
                queue.append(friend)

    return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
