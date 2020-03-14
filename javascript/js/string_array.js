var food = ["Banana", "Orange", "Apple", "Mango", "Kiwi", "Papaya"];

1. new array = var <name> => tao new variable
food.concat(array2, array3, ..., arrayX) => new []
food.join(separator) => string <- noi item in food

food.slice(1,3) <=> food[1:3] in python
var x = food.entries() => iterator [0,item_1], [1,item_2], ... x.next().value
= value
food.filter(my_function) => [item, ...] <- item in food that pass a test of my_function
food.find(my_function) => value <- first item in food pass a test of my_function
food.findIndex(my_function) => index <- first item in food pass a test of my_function
food.indexOf(item, start=2) = index of item <- chay tu index=2 of food


2. filter => true | false
food.every(my_function) => true if all items in food la true


3 change itself(update chính nó)
food.push(item1, item2, ..., itemX) => length food <- them dau
food.unshift(item1, item2, ..., itemX) => length food <- them cuoi

food.pop() => value of item end <- delete item cuoi
food.shift() => delete dau
food.splice(2,1,'item1', 'item2', ...) => tu index=2 xoa 1 item roi them cac items

food.copyWithin(target=value, start, end) => copy value
food.fill(value, start, end) =>  change item with value
food.sort() = sap xep tang
food.reverse() = sap xep giam

-------------------------------------------------------------------------------

4 string => method() string not change itself
name = "thanh phong";
name.split('').reverse().join(''); => đảo chuỗi name="gnohp hnaht"

name.replace("phong", "nhut") => "thanh nhut"
name.slice(3,8) => name[3:8] in python
name.split("") => cat rong -> cat tung tu, return stirng con lai
name.split("o") => cat o -> return string con lai
name.split('o', 3) => cat o 3  lan -> return string trong 3 lan cat do




