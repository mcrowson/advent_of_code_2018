from aocd import data
import re
import string


def generate_prepreqs(d):
  p = re.compile(r'Step (\w) must be finished before step (\w) can begin\.')
  pairs = [p.match(l).groups() for l in d]

  pre_reqs = {}
  for p in pairs:
    if p[1] not in pre_reqs:
      pre_reqs[p[1]] = set()
    if p[0] not in pre_reqs:
      pre_reqs[p[0]] = set()
    pre_reqs[p[1]].add(p[0])
  return pre_reqs


def part_a(d):
  pre_reqs = generate_prepreqs(d)

  answer = []
  while len(answer) < len(pre_reqs.keys()):
    available = sorted([k for k, v in pre_reqs.items() if len(v) == 0 and k not in answer])  # Find keys without any open prereqs
    if len(available) > 0:
      answer.append(available[0])  # Grab first alphabetically
      [pre_reqs[k].remove(available[0]) for k in pre_reqs.keys() if available[0] in pre_reqs[k]]  # Remove it from the prereq as its done
  return ''.join(answer)


def part_b(d, workers, time_pad):
    pre_reqs = generate_prepreqs(d)

    # Turn values from sets into dicts with pre_reqs and times
    for k, v in pre_reqs.items():
      pre_reqs[k] = {
        'pre': v,
        'time': time_pad + string.ascii_uppercase.index(k),
        'assigned': False
      }

    answer = []
    seconds = 0
    
    while len(answer) < len(pre_reqs.keys()):
      # Check for finished 
      for k, v in pre_reqs.items():
        if v['time'] == 0 and v['assigned']:
          workers += 1  # Free up worker
          v['assigned'] = False
          [pre_reqs[o]['pre'].remove(k) for o in pre_reqs.keys() if k in pre_reqs[o]['pre']]  # Remove it from the prereq as its done
          answer.append(k)

      # Assign new workers
      available = sorted([k for k, v in pre_reqs.items() if len(v['pre']) == 0 and k not in answer and not v['assigned']])  # Find keys without any open prereqs
      for a, w in zip(available, range(workers)):
        # combine available tasks with available workers
        pre_reqs[a]['assigned'] = True
        workers -= 1
      
      # Mark time on working nodes
      for k, v in pre_reqs.items():
        if v['assigned']:
          v['time'] -= 1

      seconds += 1
    return seconds - 1  # Return seconds corrected for index incr

    
ex1 = ['Step C must be finished before step A can begin.',
       'Step C must be finished before step F can begin.',
       'Step A must be finished before step B can begin.',
       'Step A must be finished before step D can begin.',
       'Step B must be finished before step E can begin.',
       'Step D must be finished before step E can begin.',
       'Step F must be finished before step E can begin.']

assert part_a(ex1) == 'CABDFE'
print("A: {}".format(part_a(data.split('\n'))))

assert part_b(ex1, 2, 1) == 15
print("B: {}".format(part_b(data.split('\n'), 5, 61)))