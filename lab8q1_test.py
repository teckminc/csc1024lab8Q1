import builtins
import lab8q1
from io import StringIO
from sys import stderr 
import sys
import os.path

import importlib

oriOpen = builtins.open
def openfile(a, b):
    if b.upper() == "W":
        return oriOpen("testSubject.txt", "w")
    elif b.upper() == "R":
        return oriOpen("testSubject.txt", "r")
    elif b.upper() == "A":
        return oriOpen("testSubject.txt", "a")
    else:
        return oriOpen("testSubject.txt", "r")   

def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('1\nNET3204 Distributed System\n')
    monkeypatch.setattr("builtins.open", openfile)
    monkeypatch.setattr('sys.stdin', number_inputs)
    lab8q1.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert os.path.exists("testSubject.txt")
    if os.path.exists("testSubject.txt"):
        with oriOpen(f"testSubject.txt") as tf:
            s = tf.read()
            assert(s.find("NET3204 Distributed System") != -1 )


def test_case2(monkeypatch, capsys):
    number_inputs = StringIO('2\n')
    monkeypatch.setattr("builtins.open", openfile)
    monkeypatch.setattr('sys.stdin', number_inputs)
    lab8q1.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert os.path.exists("testSubject.txt")
    if os.path.exists("testSubject.txt"):
        with oriOpen(f"testSubject.txt") as tf:
            s = tf.read()
            assert(s.find("NET3204 Distributed System") != -1 )

def test_case3(monkeypatch, capsys):
    number_inputs = StringIO('3\nCSC1024 Programming Principles')
    monkeypatch.setattr("builtins.open", openfile)
    monkeypatch.setattr('sys.stdin', number_inputs)
    lab8q1.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert os.path.exists("testSubject.txt")
    if os.path.exists("testSubject.txt"):
        with oriOpen(f"testSubject.txt") as tf:
            s = tf.read()
            assert(s.find("CSC1024 Programming Principles") != -1 )