from opentelemetry.sdk.metrics.export.aggregate import CounterAggregator
import concurrent.futures
import threading
import random
import time

counter = CounterAggregator()

start_event = threading.Event()
done = False
workers = 2
test_time = 10

take_checkpoint = True

def update_counter(counter):
  total = 0

  start_event.wait()  # wait until parent tell us to start

  while not done:
    val = random.getrandbits(32)
    counter.update(val)
    total += 1

  return total


def take_checkpoint_counter(counter):
  start_event.wait()  # wait until parent tell us to start

  while not done:
    counter.take_checkpoint()
    time.sleep(0.01)

with concurrent.futures.ThreadPoolExecutor() as ex:
  futs = [ex.submit(update_counter, counter) for _ in range(workers)]

  if take_checkpoint:
    ex.submit(take_checkpoint_counter, counter)

  start_event.set()
  time.sleep(test_time)
  done = True

  total = 0
  totals = {}
  for index, fut in enumerate(futs):
    totals[index] = fut.result()
    total += totals[index]

updates_thread_per_second = total / workers / test_time

print("print updates/thread/second = {}".format(updates_thread_per_second))
print("per thread info: {}".format(totals))
