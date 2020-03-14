tuple(): không thể thêm 1 giá trị mới vào
			: tup[0] = 'add' = > bao error
			: tup3 = tup1 + tup2 va tup * int=so tu nhien
			: có có thể xóa tup(): del tup1()

===============================================================================

các methods() của list() đều change itself
đa số các methods() change itself -> đêu không có return | return None
đều la type(my_func()) => <class 'NoneType'>

 list[]  : có thể thêm xóa sữa...  list[] lst +, * voi int=so tu nhien
            : change itself modify: trong scope cua minh len(list)
            # index ton tai moi change = 'phong' duoc
            : list[3] = 'phong'
            change itself extend updates:
			: l.append('nhut') -> None = > thêm giá trị vào cuối danh sách
			: l.extend(iterable) -> None = > new list = thêm nhiều giá trị tử iterable
            : l.insert(2,'phong') -> xác định vị trí và thêm giá trị

            change itself sort:
            : l.sort(reverse=False, key=my_func) -> sắp xếp tăng or giảm
            change itself right->left
            : l.reverse() => None -> la đảo ngược cac items từ right -> left

            change itself delete updates:
            : l.clear() ->[] xóa hết giá trị trong list
            : l.pop(2) -> xóa value theo index=2 (pop() thì nó sẽ xoa vị trí cuối)
            : l.remove('vo') -> None = > xóa value=giá_trị có nội dung là "vo"

            show index:
			: l1=l.copy() => l1 = l => lít
			: l.index(value[,start,end]) -> int = trả về index của value
			: l.count(value) -> int = đếm số lần xuất hiện của
            : help([].pop) xem syntax của pop

===============================================================================

 dict{}
 			dic = {}

            : change itself update
            : dic['age'] = 25 => update dic ko can dung methods()

			: dic={'name':'phong','age':22} cơ bản
			: dic1=dict(city='phong',tuoi=22)
			: dic2={'phong':{'nane':'thanh phong'} ,'thông'{'name':'chi thông','age':21} } mở rộng

			: dic.has_key('name') kiểm tra khóa có tồn tại không : True or False
			: dic.get('name','dong nai') => return value 'phong' cua key->nếu key 'name' ko tồn tại thì trả về 'dong nai'(string)
			: dic.setdefault('name','thông') nếu key 'name' tồn tại trả về giá trị, else gán dic['name'] = 'thông' (gán giá trị cho
				key['name'])

            show keys and values:
			: dic.keys() show tất cả các khóa
			: dic.values() show tất cả các giá trị
			: dic.items() cho khóa và giá trị của nó về dạng tuple() theo từng cặp

            change itself
			: dic.pop('name') => dic['name'] = xoa khóa(key) name trong dic
			: dic.popitem() => {key_cuoi: val_cuoi} = xóa key cuối
            : dic.clear() => {}, delete all items in dic
			: dic.fromkeys(iterable=key, value) => {iter1:value, iter2:Value...}
			: dic.update(dic1) => cập nhật giá trị dic1 vào dic
            : dic['singel'] ="ca si" thêm 1 khóa vào dic
			: kaka=dic.copy() => kaka copy từ dic
			: del dic['name'] => xóa key 'name' trong dic
			help({}.items) xem syntax của items
			:l= [x for x in range(10)] => sẽ đưa các giá trị của từng vòng lặp vào 1 list
			:l= {x:dic[x] for x in dic} => sẽ đưa các giá trị của từng vòng lặp vào 1 dict

            b = {'one': 1, 'two': 2, 'three': 3}
            a = dict(one=1, two=2, three=3)
            e = dict({'three': 3, 'one': 1, 'two': 2})

            c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
            d = dict([('two', 2), ('one', 1), ('three', 3)])
            dic = [(key, value), (k1, val1), ...]
            dict(dic)

            name = 'Vo thanh Phong'
            list(name)
            tuple(name)
            set(name)

===============================================================================


s = set({1,2,3}) = {1,2,3} => ko co keys and not s[index] ko dung duoc
a = {1,2,3,11,12}, b = {4,5,6,11,23}, c = {7,8,9}

    :a.add(4) thêm value = 4 -> them one item
    :co = a.copy()
    :a.update(b, ...{}) => change itself a -> them more items <=> a |= b

    :s.union({}, {}, ...) => them item vao s -> not change itself
    a | b | c = a.union(b,c)= lay tat ca
    a |= b <=> a += b set ko ho tro operator(+)

    a - b = {1,2,3}
    a.difference(b) => lay item in a, not in b
    a.difference_update(b) lay khac nhau change itself a <=> a -= b

    a & b = lay giao nhau {11,12}
    a.intersection(b) => lay giao nhau
    a.intersection_update(b) = lay giao nhau change itself cho a <=> a &= b

    a ^ b = lay khac nhau {1,2,3,4,5,6}
    a.symmetric_difference(b) => lay khac nhau cua ca a and b
    s.symmetric_difference_update(b) => change itself cho a <=> a ^= b

    :a.remove(3)  => xóa value = 3, raise if 3 not exist
    :a.discard(2) => xoa value = 2, not raise
    :a.pop() => delete last item
    :a.clear() => a = set() xóa tất cả pt

    :s1 = s.copy() => {1,2,3} ----> s1 is s = False

    :a.issubset(b) => True if a la con b <=>     a <= b
    :a.issuperset(a) => True if a la cha b <=>   a >= b
    :a.isdisjoint(b) =>  True if a and b ko co item giong nhau

x = frozenset(iterable) -> giong set(), dung method() va operator(|, &, ^, -)
cua set() nhung ko co method() change itself cua set()





