class ds:
    def lists(self, _list):
        print(_list)
        _list.append(10)
        _list.insert(1, 0)
        _list.pop()
        _list.pop(3) # method(index)
        _list.append([4,5])
        _list.extend([4,5])
        print(f"New List : {_list}")

    def tuples(self, _tuple):
        print(type(_tuple))
        _tuple = list(_tuple)
        print(type(_tuple))
        _tuple.append(10)
        _tuple = tuple(_tuple)
        print(f"type : {type(_tuple)}, {_tuple}")

    def dicts(self, _dicts):
        print(_dicts)
        print(f"Keys : {_dicts.keys()}, values : {_dicts.values()}")
        for i,j in _dicts.keys(),_dicts.values():
            print(i , j)
        for i in _dicts:
            print(i, _dicts[i])
        for key,value in _dicts.items():
            print(key, value)
        #addition of new item in Dict
        #_dicts[key] = Value
        _dicts["Name"] = "Ram"
        print(_dicts)
        _dicts["Name"] = "Lakshman" # updation of key
        print(_dicts)

        #pop/deletion
        _dicts.pop("Name")
        print(_dicts)
        _dicts.popitem() # Deletes Last item in Dict
        print(_dicts)

    def sets(self, _set):
        print(type(_set), _set) 
        #print(_set[0]) #Error: 'set' object is not subscriptable
        _set.add(5)
        _set.update([8,9])
        _set.pop()
        print(_set)

if __name__ == "__main__":
    obj = ds()
    obj.lists([1,2,3,4,5])  #mutuable, ordered, duplicate
    obj.tuples((1,2,3,4,5)) #immutable, ordered, duplicate
    obj.dicts({ 1:"a", 2:"b" }) #mutable, ordered, unique key
    obj.sets({1,2,3,4,5,6}) #immutable, un-ordered, no duplicate

