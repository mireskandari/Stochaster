def tupleargs(*args):
  print(tuple(args[0]) if args is not None and type(args[0]) in (tuple, list) \
         else args)
  return tuple(args[0]) if args is not None and type(args[0]) in (tuple, list) \
         else args