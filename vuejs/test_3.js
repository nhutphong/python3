var app_1 = new Vue({
    el: "#app-1",
    data: {
        dfullName: "Vo Thanh Phong",
        dfirstName: '',
        dlastName: '',
        dchecked: false,
        dcheckedNames: [],
        dpicked: '',
        dselected: '',
        dcount: 0,

    },

    methods: {
        mfirstName: function(){
            var temp = this.dfullName.split(' ');
            this.dfirstName = temp[0];
            return this.dfirstName
        },

        mlastName: function(){
            var temp = this.dfullName.split(' ');
            this.dlastName = temp[temp.length -1];
            return this.dlastName
        },

    },

    computed: {

    },
});


function main(){

}
