#!/usr/bin/env python

from string import ascii_lowercase


def spin(programs, count):
    for x in range(count):
        programs.insert(0, programs.pop())


def exchange(programs, first, second):
    temp = programs[first]
    programs[first] = programs[second]
    programs[second] = temp


def partner(programs, first, second):
    ix_first = programs.index(first)
    ix_second = programs.index(second)
    programs[ix_first] = second
    programs[ix_second] = first


def dance(tokens, programs):
    for t in tokens:
        action = t[:1]
        if action is 's':
            count = int(t[1:])
            spin(programs, count)
        elif action is 'x':
            first, second = tuple(map(int, t[1:].split('/')))
            exchange(programs, first, second)
        elif action is 'p':
            first, second = tuple(filter(None, t[1:].split('/')))
            partner(programs, first, second)


def tokenize(intext):
    return intext.split(',')

if __name__ == '__main__':
    programs = [letter for letter in ascii_lowercase[:16]]
    with open('input.txt', 'r') as f:
        tokens = tokenize(f.read().strip())

    for _ in range(1000000000):
        dance(tokens, programs)

    print(''.join(programs))
