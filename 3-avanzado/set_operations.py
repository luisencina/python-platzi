# Utility
def sets() -> None:
  """Multiple Operations with sets"""
  my_set1 = {'1', '2', '3', '4', '5'}
  my_set2 = {'6', '2', '7', '4', '8'}
  print("  →  Set 1:", my_set1)
  print("  →  Set 2:", my_set2)
  print('')
  # Union
  my_set3 = my_set1 | my_set2
  print("     Union                  :", my_set3)
  # Intersection
  my_set4 = my_set1 & my_set2
  print("\n     Intersection           :", my_set4)
  # Difference
  my_set5 = my_set1 - my_set2
  print("\n     Difference set1 - set2 :", my_set5)
  my_set6 = my_set2 - my_set1
  print("\n     Difference set2 - set1 :", my_set6)
  # Symmetric Difference
  my_set7 = my_set1 ^ my_set2
  print("\n     Symmetric Difference   :", my_set7)


if __name__ == '__main__':
  print("*** O P E R A T I O N S    W I T H    S E T S ***\n")
  sets()
