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

// console.log(first_name);
/*_localVariable.name();*/
/*console.log(first_name);*/


// console.log(typeof list);
// console.log(typeof dict);
// console.log(typeof age);
// console.log(typeof str);
// console.log(typeof str1);
// console.log( str === false);
// console.log(str1 === false);

// switch (age) {
//   case age > 18:
//     console.log("Het teen");
//     break;

//   case age > 40:
//     console.log("Gia roi");
//     break;

//   default:
//     console.log("Ban con qua nho");
//     break;
// }

// function birthYear(year) {
//   var my_old = 2018 - year;
// }

// var input_year = prompt("Nam sinh cua ban la bao nhieu");

// var name = 'Phong';

// function first() {
//   a = 'mot';
//   second();
//   name += a;
//   return name;
// }

// function second() {
//   b = 'hai';
//   third();
//   name += b;
// }

// function third() {
//   c = 'ba';
//   name += c;
// }

// var fir = first()

// // phongbahaimot
// console.log(fir);

// function name(ten) {
//   console.log(ten)
// }

// var name1 = function(ten) {
//   console.log(ten)
// }

// function arrow
// (param, ...) => <return> statements
// var name2 = (ten) => console.log(ten);
// tuoi() function arrow
//
// var variableName: có thể dùng ngoài outblock khối ìf, while, for, switch
// let variableName: chỉ dùng trong inblock if, while, for ...
// const variableName: không thể thay đổi giá trị
// const name = ['phong', 'nhut'] => name = ['tan', 'nhut'] -> error
// name[0] = 'vo' -> allowed => có thể dùng method() để change value cho từng
// item
// obj.fullName.call(obj1) => truyen attributes cua obj1 vao fullName of obj du dung
//
// var self = {
//   old: 25,
//   tuoi: () => console.log(self.old, self),
//   c: function() { console.log(self.old, self)},
// };

// b, c la kiểu khai vao function trong obj self
//
// có 2 loại object
// var list = []
// vả dict = {name: value, ...}

// dict.name = value
// dict["name"] = value
//
function checkAddress(fieldId) {
    var mail = document.getElementById(fieldId).value;

    if (mail ===  ""){
        alert("Email address required.");
    }
}


function getDateNow(){
    var date = new Date();

    show = document.getElementById("show");
    show.textContent = date;
}


function runRandom(){
    var run = document.getElementById("show");
    run.textContent = Math.random()*10;
}


function setRandom(){
    var divRandom = document.getElementById("myDIV");
    divRandom.addEventListener("mousemove", runRandom);
}


function stopRandom(){
    var stop = document.getElementById("myDIV");
    stop.removeEventListener("mousemove", runRandom);
}


function createParaBefore () {
    var createPara = document.createElement("p");
    var createText = document.createTextNode("Create before Year!!!");
    createPara.appendChild(createText);

    var parents = document.getElementsByClassName("container");
    var targets = parents[0].children;

    parents[0].insertBefore(createPara, targets[0]);

}


function main(){
    var divRandom = document.getElementById("myDIV");
    divRandom.addEventListener("mousemove", runRandom);

    var sRandom = document.getElementById("removeRandom");
    sRandom.addEventListener("click", stopRandom);

    var rRandom = document.getElementById("runRandom");
    rRandom.addEventListener("click", setRandom);

    var date = document.getElementById("runDate");
    date.addEventListener("click", getDateNow );

    var buttB = document.getElementById("runBefore");
    buttB.addEventListener("click", createParaBefore);
}

main();
