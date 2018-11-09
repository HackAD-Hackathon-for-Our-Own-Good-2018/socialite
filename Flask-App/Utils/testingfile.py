allids = ['hwl278', 'did233', 'arz268', 'ans682', 'sp4944', 'ns3774', 'jai264', 'kk3609', 'aas1066', 'ub352', 'sj2538']
p1_dont_match = ['']
already_matched = ['']
match_ok = [item for item in allids if item not in p1_dont_match]

print match_ok