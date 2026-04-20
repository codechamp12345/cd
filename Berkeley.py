from datetime import datetime, timedelta

def to_time(t):
    return datetime.strptime(t, "%H:%M")

def to_str(t):
    return t.strftime("%H:%M")

def berkeley():
    # system times
    s1 = to_time("03:00")  # coordinator
    s2 = to_time("02:50")
    s3 = to_time("03:25")

    systems = [s1, s2, s3]

    print("Before Synchronization:")
    for i, s in enumerate(systems, 1):
        print(f"System-{i}:", to_str(s))

    # convert all to minutes
    times = [s.hour * 60 + s.minute for s in systems]

    # calculate average
    avg = sum(times) // len(times)

    print("\nAverage Time:", f"{avg//60:02}:{avg%60:02}")

    print("\nAfter Synchronization:")
    for i, t in enumerate(times, 1):
        diff = avg - t
        new_time = t + diff
        print(f"System-{i}: {new_time//60:02}:{new_time%60:02}")

berkeley()