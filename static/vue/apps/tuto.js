new Vue({
    el: '#app',
    delimiters: ['{$', '$}'],
    data: {
        mensajes: [],
        message: 'funciono putitos',
        tutoria: '',
        Usuario: ''
    },
    watch: {
        kword: function(kword) {
            this.request()
        }
    },
    methods:{
        getMensajes: function() {
            this.request()
        },
        request: function() {
            axios.get('getmensajes?tutoria='+
            this.tutoria+
            '&Usuario='+this.Usuario).then(
                response => {
                    this.mensajes = response.data.mensajes;
                    console.log(this.mensajes)
                }
            )
        }

    },
    beforemount(){
        this.getMensajes()
    }
});
