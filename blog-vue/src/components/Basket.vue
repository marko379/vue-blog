<template>

<button class="button is-medium is-fullwidth is-success is-rounded button-add-to-basket" @click="bookToBasket(bookName,bookPrice,bookPhoto,slug); 
 addPrice(bookPrice); addBookPopUpMsg();">add to basket</button>

</template>



<style lang="scss">

.button-add-to-basket{
    margin-top: 15px;
}




</style>

<script>
import axios from 'axios'

export default {
    // props are coming from home view 
    props: ['bookName','bookPrice','bookPhoto','slug'],
    // emits: ["close","myComment"],
    name: 'Basket',
    data() {
        return {
            num:0,
            track:0,
            newTrack:null,
            count: 0,
            l:[]
        }
    },
    methods: {
      
      bookToBasket(bookName,bookPrice,bookPhoto,slug){
        this.l.push(bookName)
        this.l.push(bookPrice)
        this.l.push(bookPhoto)
        this.l.push(slug)
        this.$store.commit('addBookToBasket',this.l)

        if(this.$cookies.get("userID") || this.$store.state.userId){
            const data = new FormData()
            data.append('user_id', this.$cookies.get("userID"))
            data.append('slug', slug)
            axios.post("articles/book-to-basket/",data)
        }
      },

      addPrice(addPrice){
        this.$store.commit('addPriceStore',addPrice)
      },

      addBookPopUpMsg(){
        this.$store.commit('showMsgBasket','book added in the basket')
      } 


    }

}
</script>