from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["pikachu","Squirtle","charmander"])
table.add_column("Type",["electric", "water", "fire"])

table.align = "l"
print(table)