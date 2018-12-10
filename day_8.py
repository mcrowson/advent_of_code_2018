from aocd import data
from dataclasses import dataclass


def part_a(d):
  tree = map(int, d.split())

  class Node:
    def __init__(self):
      self.child_count = next(tree)
      self.meta_count = next(tree)

    def child_sums(self):
      sums = list()
      for i in range(self.child_count):
        node = Node()
        sums.append(node.get_checksum())
      return sums

    def meta_vals(self):
      return [next(tree) for _ in range(self.meta_count)]

    def get_checksum(self):
      child_values = self.child_sums()
      metadata_values = self.meta_vals()

      return sum(child_values + metadata_values)

  root = Node()
  checksums = root.get_checksum()
  

  return checksums


def part_b(d):
  tree = map(int, d.split())
  class Node:
    def __init__(self):
      self.child_count = next(tree)
      self.meta_count = next(tree)

    def child_sums(self):
      sums = list()
      for i in range(self.child_count):
        node = Node()
        sums.append(node.get_checksum())
      return sums

    def meta_vals(self):
      return [next(tree) for _ in range(self.meta_count)]

    def get_checksum(self):
      child_values = self.child_sums()
      metadata_values = self.meta_vals()

      if self.child_count == 0:
        return sum(metadata_values)
      else:
        check_sums = 0
        for m in metadata_values:
          if m - 1 < self.child_count:
            check_sums += child_values[m - 1]
        return check_sums

  root = Node()
  checksums = root.get_checksum()
  return checksums

    
ex1 = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

assert part_a(ex1) == 138
print("A: {}".format(part_a(data)))

assert part_b(ex1) == 66
print("B: {}".format(part_b(data)))