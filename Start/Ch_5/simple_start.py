# Example file for Advanced Python: Language Features by Joe Marini
# Simple pattern matching using literal values

x = 0

# TODO: Literal patterns are explicit values: integers, strings, Booleans, etc
match x:
    case 0:
      print("Zero")
    case 1:
      print("One")
    case _:
      print("No match")
