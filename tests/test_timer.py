# Copyright (c) Prometeo AI, Inc. All rights reserved.


from lib.common.timer import Timer


def test_timer_init():
    t = Timer()
    assert t.interval == 0
    assert str(t) == "0:00:00"


def test_timer_instance():
    big_num = 1000
    t = Timer()
    t.start()
    r = 0
    a = [r + i for i in range(big_num)]
    t.stop()
    assert t.interval < 1


def test_timer_context():
    big_num = 1000
    r = 0
    with Timer() as t:
        a = [r + i for i in range(big_num)]
    assert t.interval < 1
