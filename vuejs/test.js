var app_1 = new Vue({
    el: "#app-1",
    data: {
        myName: "Vo Thanh Phong",
        seen: true,

        todos: [
            {text: "Tao la text 1"},
            {text: "Vo Thanh Phong 2"},
            {text: "Duong Ngoc Hanh 3"},
        ],

    },
    methods: {
        reverseNameVue: daoChuoi,

    }

});


var app_2 = new Vue({
    el: "#app-2",
    data: {
        myName: "Vo Thanh Phong",
        seen: true,

        todos: [
            {text: "Tao la text 1"},
            {text: "Vo Thanh Phong 2"},
            {text: "Duong Ngoc Hanh 3"},
        ],

    },
    methods: {
        runRandomVue: setRandom,
        runStopRandomVue: stopRandom,
        runDateNowVue: getDateNow,

    }

});


var app_3 = new Vue({
    el: "#app-3",
    data: {
        row: 0,
        col: 0,
        count:0,
    },
    methods: {
        runMoveVue: getMove,
        runAlertVue: getAlert,
    }

});


var app_4 = new Vue({
    el: '#app-4',
    data: {
        numberA: 0,
        numberB: 0,
        numberSum: 0,
        dataToUpper: "",

    },
    methods: {
        runTongVue: getSum,
        runToUpperVue: getToUpper,

    }
});


var app_5 = new Vue({
    el: '#app-5',
    data: {
        dataMessage: 'Hello Vue.js',
        dataName: 'Thanh Phong',
        cssBgColor: '#3333',
        cssTextColor: 'yellow',
        cssTextSize: '',

    },

});


Vue.component('list-dict', {
  props: ['dict'],
  template: '<li>{{ dict.text }} and {{ dict.id  }}</li>'
});

var app_6 = new Vue({
  el: '#app-6',
  data: {
    groceryList: [
      { id: 0, text: 'Vegetables' },
      { id: 1, text: 'Cheese' },
      { id: 2, text: 'Whatever else humans are supposed to eat' }
    ],
    dMessage: "Thanh Phong",

  },

  methods: {
    mGetMethods: function(){
        return `Tao la methods: mGetName()`
    }
  },

  computed: {
    cGetComputed: function(){
        return `Tao la computed: cGetComputed`
    },
    cReverseMessage: function(){
        return this.dMessage.split('').reverse().join('')
    },
  },
});


function daoChuoi() {
    app_1.myName = app_1.myName.split("").reverse().join("");
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
    var divRandom = document.getElementById("app-2");
    divRandom.addEventListener("mousemove", runRandom);
}


function stopRandom(){
    var stop = document.getElementById("app-2");
    stop.removeEventListener("mousemove", runRandom);
}

function createParaBefore(){
    var createPara = document.createElement("p");
    var createText = document.createTextNode("Create before Year!!!");
    createPara.appendChild(createText);

    var parents = document.getElementsByClassName("container");
    var targets = parents[0].children;

    parents[0].insertBefore(createPara, targets[0]);

}


function getMove(event){
    app_3.col = event.offsetX;
    app_3.row = event.offsetY;

    console.log(event);
}


function getAlert(message){
    alert(message);
}


function getSum() {
    app_4.numberA = document.getElementById("myA").value;
    app_4.numberB = document.getElementById("myB").value;
    app_4.numberSum = parseInt(app_4.numberA) + parseInt(app_4.numberB);

    return app_4.numberSum
}


function getToUpper(){
    var temp = document.getElementById("idToUpper");
    temp.value = temp.value.toUpperCase();
    app_4.dataToUpper = temp.value;
}
