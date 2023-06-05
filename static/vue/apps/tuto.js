new Vue({
    el: '#app',
    delimiters: ['{$', '$}'],
    data: {
        messages: [],
        message: 'funciono putitos'
    },
    methods:{
        getMensajes: function() {
            this.request()
        }
        request: function() {
            
        }

    },
    beforemount(){
        this.getMensajes()
    }
});
