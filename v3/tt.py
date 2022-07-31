
myDict = { 'a': 1,
           'b': { 
              'b1': {'x': 1,
                    'y': 2} },
           'c': ['hi', 'bar'] 
         }
a=defDictToObject(myDict)
print(a.a)