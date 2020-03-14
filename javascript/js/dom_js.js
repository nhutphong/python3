==, !=, &&, ||, !=not
===, !==,
age++ -> lam cai gi do roi moi +1
++age -> +1 roi moi lam


var first_name = "glocal";
var age = 10;
var str = '';
var str1 = 0;
var list = [];
var dict = {};

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

var name = 'Phong';

function arrow
(param, ...) => <return> statements
var name2 = (ten) => console.log(ten);

var variableName: có thể dùng ngoài outblock khối ìf, while, for, switch
let variableName: chỉ dùng trong inblock if, while, for ...
const variableName: không thể thay đổi giá trị
const name = ['phong', 'nhut'] => name = ['tan', 'nhut'] -> error
name[0] = 'vo' -> allowed => có thể dùng method() để change value cho từng
item

obj.fullName.call(obj1, param, param1,...) => truyen attributes cua obj1 vao fullName of obj du dung <=> fullName(param, param1, ...)

obj.fullName.apply(obj1, [param, param1,...]) =>

var self = {
  old: 25,
  tuoi: () => console.log(self.old, self),
  c: function() { console.log(self.old, self)},
};

tuoi() function arrow
b, c la kiểu khai vao function trong obj self
có 2 loại object
var list = []
vả dict = {name: value, ...}

dict.name = value
dict["name"] = value


===============================================================================

                                HTML DOM
function changeText(el) {
    el.innerHTML = "Ooops!";
}
// <h1 onclick="changeText(this)">Click on this text!</h1>
// changeText(this) =>param this = refer el<h1>
// <h1 onclick="this.innerHTML='Ooops!'">Click on this text!</h1>
//
document.getElementById(id).attribute = new_value;
document.getElementById(id).style.property = new_style;

property -> css -> color, background, ...
element = the html -> <a>, <p>, ...



===============================================================================

                                EVENTS JS

Gán sư kiện trưc tiếp từ file JavaScript.js

selectElement.addEventListener("click", mySecondFunction);
selectElement.addEventListener("mouseout", myThirdFunction);

itselfElement.addEventListener("mousemove", myFunction);
itselfElement.removeEventListener("mousemove", myFunction);
// bo on truoc name events
// dac biet: mousemove = runFunction lien tuc khi chuot di chuyen trong element
document.getElementById("myBtn").onclick = displayDate; //displayDate()

===============================================================================

                                EVENTS HTML

events như controllers => để run(kích hoạt) các Function trong file JavaScript.js


event trong file.html có (on) => onclick = "runFunction()" phải có dấu ->()
// Events = onclick-> click moi runFunction,
//          onload->vao trang web auto runFunction
//          onmouseover -> re chuot vao -> runFunciton
//          onmouseout -> ko co chuot -> run
//
//          onmousedown -> re chuot vao va click giu chuot va out khoi el tha chuot ->runFunction
//          onmouseup -> click thi runFunction
//          onchange -> change value trong el, thoat khoi el se runFunction
//
===============================================================================

                            ATTRIBUTES OF ELEMENT
elementP.attributes = array [
                                {name: 'class', value:'myClass'},
                                {name: 'id', value: 'myId'},
                                {name: 'onclick', value: 'myFunction()'},
                                ...
                        ];

-> chỉ dùng được attris = element.attributes=> HTML collection attributes itself
-> attris[index].name = name_attribute
-> attris[index].value = value_ò_name_attribute



===============================================================================

                                HTML COLLECTION

array[elements] nhung ko dung duoc cac method array cua javascript
var y = document.getElementsByTagName("p"); // [all elements <p>] scope html
var elP = man.getElementsByTagName("p"); //array = [all elemments <p>] chua trong el x
vả elements = document.getElementsByClassName("container") = HTML collection
-> elements[index] = dung select element can dung



var elForms = document.forms[id_form] // -> array = [elements] con cua forms
//rieng forms dung -> elForms.value <- not elForms.nodeValue
//
//co the dung elp[index] kho the dung method cua array

var myNodeList = document.querySelectorAll(".className"); // array [elements <p>]
var myNodeList = document.querySelector(".class_name"); select first element

var man = document.getElementById("main");
man.children = // array [elements con của man]    ko co text giong childNodes

el.innerHTML === el.textContent = content cua element
element.nodeName===element.tagName -> name_elements= h1, h2,a, ...

element.parentNode => chuyển về element parent

element.firstChild.nodeValue -> value=content of element
element.lastChild.nodeValue ->
element.childNodes -> array [text, element, text, el, ...] xen ke nhau, neu el=4 thi text=5, .length = 9 =====> array [con cua element]


===============================================================================

                                STYLE.PROPERTY

DOM Style = CSS <- change css
element.style.<property> = value;

<property> =  xem o https://www.w3schools.com/jsref/dom_obj_style.asp


===============================================================================

                                ELEMENT.PROPERTY

Các element có property(attributes) riêng có thể dùng như sau
vd: element:  <input type="text" id="myId">, ...
document.getElementById("myId").size = "50"; => có thể gán gía trị

<input type="text" id="myId" size="50">
