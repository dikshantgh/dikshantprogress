from dikshantprogress import TriggeredProgressBar
import random

def random_start():
    return random.random() > 0.8  # 20% chance to start

def random_stop():
    return random.random() > 0.9  # 10% chance to stop

bar = TriggeredProgressBar(random_start, random_stop)
bar.monitor()

# Keep program running
while bar.running:
    time.sleep(0.1)