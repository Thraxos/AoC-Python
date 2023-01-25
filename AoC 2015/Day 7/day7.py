import os
import sys
import functools
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

wire_signals = {}

for line in lines:
    line = line.rstrip()
    signal, destination = line.split(" -> ")
    wire_signals[destination] = signal

@functools.lru_cache()
def get_signal(source):
    try:
        return int(source)
    except ValueError:
        pass

    signal = wire_signals[source].split(" ")

    if "NOT" in signal:
        return ~get_signal(signal[1])
    if "AND" in signal:
        return get_signal(signal[0]) & get_signal(signal[2])
    elif "OR" in signal:
        return get_signal(signal[0]) | get_signal(signal[2])
    elif "LSHIFT" in signal:
        return get_signal(signal[0]) << get_signal(signal[2])
    elif "RSHIFT" in signal:
        return get_signal(signal[0]) >> get_signal(signal[2])
    else:
        return get_signal(signal[0])

print(f"The signal from wire 'a' is initially: {get_signal('a')}")
wire_signals["b"] = str(get_signal('a'))
get_signal.cache_clear()
print(f"The signal from wire 'a' after overriding wire 'b' with the initial value from 'a' is: {get_signal('a')}")