<template>

<div class="notification is-info is-light">
    <h1 class="title is-4">Serach results for: <span class="is-underlined is-capitalized has-text-weight-bold is-italic">{{data}}</span></h1>
</div>


  <div class="container-articles-search-results">
    <div v-for="book in books" :key="book.id" class="container box"> <!--  v-if="Articles.length % 2 !== 0" -->
        <router-link :to="{ name: 'article' ,  params: {slug: book.slug}}">
            <img class="home-images" :src="book.image_path" width="200">
        </router-link>

        <h1 class="title is-5">{{book.name}}</h1>
        <div class="basket-container">
          <Basket :slug="book.slug" :bookName="book.name" :bookPhoto="book.image_path" :bookPrice="book.price"/>
        </div>
        <div class="stars-home-view-container">
          <ArticleStarsHome :slug="book.slug"/>
        </div>
        <div class="home-view-comments">
          <h1 class="title is-5">{{book.num_of_comments}} reviews</h1>
        </div>
        

    </div>
  </div>


</template>



<style lang="scss">

.container-articles-search-results{
    display:flex;
}

</style>





<script>
import axios from 'axios'
import Basket from '@/components/Basket.vue'
import ArticleStarsHome from '@/components/ArticleStarsHome.vue'

export default {
    props: ['data'],

    name: 'SerachResults',
      components: {
          Basket,
          ArticleStarsHome,
      },
    data() {
        return {
           books:[] 
        }
    },

    mounted(){
        this.getBooks(this.$route.params.data)
    },

    methods: {
      getBooks(value){
        axios.get(`/articles/search_books/${value}/`).then(response => {this.books = response.data}).catch(error => {console.log(error)})
      },
    },

    watch: { 
        data (newVal, oldVal) {
        this.getBooks(newVal)
        }
    }

}
</script>