immutable_var = 1, True, "Float"
print("immutable_var: ", immutable_var)
#immutable_var[0] = 7     immutable_var - кортеж. Кортеж не поддерживает операцию замены одного элемента (в данном случае, 0-го индекса) на другой
mutable_list = [1, True, "Float"]
mutable_list[0] = False
print("mutable_list: ", mutable_list[0:1])
