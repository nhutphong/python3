var first_name = "glocal";
var age = 10;
var str = '';
var str1 = 0;
var list = [];
var dict = {};

var a = 6;
var out = a++; gan out=6 ; tang a=7 sau
a++ gan truoc tinh sau
++a tinh truoc gan sau

var outTwo = ++a; tang a=7 ; outTwo=7



var _localVariable = {
  name: function(){
    console.log(first_name);
    first_name = "nhutphong";
    console.log("Day la local " + first_name)

},
}

console.log(first_name);
_localVariable.name();
console.log(first_name);


console.log(typeof list);
console.log(typeof dict);
console.log(typeof age);
console.log(typeof str);
console.log(typeof str1);
console.log( str === false);
console.log(str1 === false);

switch (age) {
  case age > 18:
    console.log("Het teen");
    break;

  case age > 40:
    console.log("Gia roi");
    break;

  default:
    console.log("Ban con qua nho");
    break;
}

function birthYear(year) {
  var my_old = 2018 - year;
}

var input_year = prompt("Nam sinh cua ban la bao nhieu");


function arrow
(param, ...) => <return> statements
var name2 = (ten) => console.log(ten);
tuoi() function arrow

#function contructor
function Person(firstName, lastName, age, eyeColor) {
  this.firstName = firstName; 
  this.lastName = lastName;
  this.age = age;
  this.eyeColor = eyeColor;
  this.changeName = function (name) {
    this.lastName = name;
  };
  this.get_nationality = function() {
    return this.nationality
  }
}

#add attributes cho Person
Person.prototype.nationality = "English";

person = new Person('thanh', 'dung', 27, 'xanh')
person.nationality
person.get_nationality()

var variableName: có thể dùng ngoài outblock khối ìf, while, for, switch
let variableName: chỉ dùng trong inblock if, while, for ...
const variableName: không thể thay đổi giá trị
const name = ['phong', 'nhut'] => name = ['tan', 'nhut'] -> error
name[0] = 'vo' -> allowed => có thể dùng method() để change value cho từng
item
obj.fullName.call(obj1) => truyen attributes cua obj1 vao fullName of obj du dung


có 2 loại object
var list = []
vả dict = {name: value, ...}

dict.name = value
dict["name"] = value

var person1 = {firstName: 'Jon', lastName: 'Kuperman'};

function say(greeting1, greeting2) {
 console.log(greeting1 + ',' + greeting2 + ' ' + this.firstName + ' ' + this.lastName);
}

say.call(person1, 'Hello', 'Good morning'); // => Hello,Good morning Jon Kuperman

say.apply(person1, ['Hello', 'Good moring']); // => Hello,Good moring Jon Kuperman

var sayHelloJon = say.bind(person1, 'Hello', 'Good morning');
sayHelloJon(); // => Hello,Good morning Jon Kuperman

Nhìn chung, hàm call và apply là gần giống nhau. Chúng đều gọi hàm trực tiếp. 
Chỉ khác ở cách truyền tham số vào (với call thì đối số phân cách bởi dấu phẩy
comma và với apply thì đối số cho bởi mảng array)

Hàm bind thì hơi khác hơn một chút. Hàm này không gọi hàm trực tiếp mà nó sẽ trả
về một hàm mới. Và bạn có thể sử dụng hàm số mới này sau. 
Về cách truyền tham số vào thì nó giống với hàm call.


