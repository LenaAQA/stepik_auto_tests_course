def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
r = 0
res = []
for i in range(77):
    p = r * 10 + 7
    res.append(p)
    r = p
my_frozen = frozenset(res)
print(res)
print(my_frozen)
