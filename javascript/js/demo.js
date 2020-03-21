
var myName = 'phong';

var myInfo = {
  name: "thanh dung",
  old: 27,
  city: "ha noi",
  country: "viet nam"
}
// myInfo = object khong dung for(value of data){}

function showLoop(data){
  for(key in data){
    console.log("for in xuat key|index: " + key);
  }

  for(value of data){
    console.log("for of xuat value: " + value)
  }
}

showLoop(myName)