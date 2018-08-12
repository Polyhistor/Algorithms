def list_duplicates(seq):

  seen = set()
  seen_add = seen.add


  seen_twice = set( x for x in seq if x in seen or seen_add(x) )

  return list( seen_twice )

a = [1,2,3,2,1,5,6,5,5,5]
print(list_duplicates(a))