"""
This problem is solved on small value of n and m.
However, for larger value of n and m, I need to implement some kind of memoization technique - I haven't figured it out yet :(
"""

ins = lambda: [int(x) for x in input().split(' ')]

def solve() -> int:
  n, m = ins()
  a = ins()
  b = ins()
  c = ins()

  exp_out = 0

  # print(n, m , a, b, c, sep='\n')

  diff = [x-y for x, y in list(zip(a, b))]
  a_diff_sorted = sorted(list(zip(a, diff)), key=lambda x: x[1])
  # print(a_diff_sorted)

  for j in range(m):
    a_index = 0
    cur_c = c[j]
    while a_index < n:
      cur_a, cur_diff = a_diff_sorted[a_index]
      if cur_c >= cur_a:
        rang = cur_c - cur_a
        exp_out += 2
        num_ops = int(rang / cur_diff)
        cur_c -= cur_diff * (num_ops + 1)
        exp_out += num_ops * 2
      a_index += 1

  return exp_out

print(solve())
