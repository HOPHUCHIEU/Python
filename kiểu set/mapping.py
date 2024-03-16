class Map_Class:
           def keys(self):
                 return [1, 2, 3]
           def __getitem__(self, key):
                 return key * 2

map_obj = Map_Class()
 dic = dict(map_obj)
 dic
{1: 2, 2: 4, 3: 6}
print(dic)