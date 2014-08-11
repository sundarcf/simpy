import simpy

def my_proc(env):
    while True:
        print(env.active_process)  # will print "p1"
        subfunc(env)
        yield env.timeout(1)
        env.exit(42)  # Py2 equivalent to "return 42"


def subfunc(env):
    print(env.active_process)  # will print "p1"


def other_proc(env):
    subfunc(env)
    ret_val = yield env.process(my_proc(env))
    assert ret_val == 42


env = simpy.Environment()
p1 = env.process(my_proc(env))
env.active_process  # None
env.step()
p2 = env.process(other_proc(env))
env.step()