import simpy


def my_callback(event):
    print('Called back from', event)


env = simpy.Environment()
event = env.event()
event.callbacks.append(my_callback)
print(event.callbacks)
