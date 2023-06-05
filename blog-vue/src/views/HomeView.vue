<template>

<div class="main-home">

  <div class="container-articles">
    <div v-for="article in Articles" :key="article.id" class="container box"> <!--  v-if="Articles.length % 2 !== 0" -->
        <router-link :to="{ name: 'article' ,  params: {slug: article.slug}}">
            <img class="home-images" :src="article.image_path" width="200" referrerpolicy="unsafe-url">
        </router-link>

        <h1 class="title is-5">{{article.name}}</h1>
        <div class="basket-container">
          <Basket :slug="article.slug" :bookName="article.name" :bookPhoto="article.image_path" :bookPrice="article.price"/>
        </div>
        <div class="stars-home-view-container">
          <ArticleStarsHome :slug="article.slug"/>
        </div>
        <div class="home-view-comments">
          <h1 class="title is-5">{{article.num_of_comments}} reviews</h1>
        </div>
        

    </div>
    <div class="container"></div>
    <div class="container"></div>
  </div>

</div>

</template>



<style lang="scss">

body{
  background-color: white;
  font-family: 'Playfair Display', cursive;

}

.stars-home-view-container{
  margin-top: 5px;
  margin-bottom: 5px;
}

.ArticleStarsHome-div{
  display: flex;
}

.main-home{
  background-color: white;
}

// .basket-container{
//   width: 200px;
// }

.msg-for-succsefully-created-user{
  background-color: #b3ffb3;
  width: 90%;
  margin: auto;
  margin-top: 15px;
  text-align: center;
  padding: 15px;

}

.home-view-comments{
  margin-top: 5px;
}
.container-articles{
  background-color: white;
  display: flex;
  max-width: 1400px;
  width: 100%;
  // border: solid;
  justify-content: space-evenly;
  flex-wrap: wrap;
  margin: auto;
  // margin-top: 30px;

}

.container{
  flex-grow: 0;
  width: 240px;
  // height: 400px;
  // border:dotted;
  margin: 10px;
  // margin: auto;
}

.home-view-images{
  margin:auto;
  width:200px;
  border:solid;
}

.desc-container{
  margin: auto;
  border:solid;
}
.home-images:hover {
  transition: transform 0.7s, filter 0.4s linear;
  filter: grayscale(90%);
  transform: scale(0.95);
}

</style>

<script>
import axios from 'axios'
import Basket from '@/components/Basket.vue'
import ArticleStarsHome from '@/components/ArticleStarsHome.vue'

export default {
  name: 'HomeView',
  components: {
      Basket,
      ArticleStarsHome,
  },
    data() {
      return {
        Articles: [],
        isVisible: false,
        username_created: null,
        username_login: null,
        userLoggedIn: null,
      }
    },

    mounted() {
      this.getArticles()
    },


    methods: {
      async getArticles(){
        // 'http://127.0.0.1:8000/' base url in main.js
        await axios.get('articles/').then(response => {this.Articles = response.data}).catch(error => {console.log(error)})
      },
    }
}
</script>
