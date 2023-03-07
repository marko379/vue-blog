<template>

<div class="main-home">

  <div class="msg-for-succsefully-created-user" v-show="isVisible">
     <h1 class="title is-3" v-show="username_created != null">Welcome {{username_created}} You can login now!</h1>
     <h1 class="title is-3" v-show="username_login != null">Welcome {{username_login}} You are logged in!</h1>
  </div>

  <div class="container-articles">
    <div v-for="article in Articles" :key="article.id" class="container"> <!--  v-if="Articles.length % 2 !== 0" -->
      <router-link :to="{ name: 'article' ,  params: {slug: article.slug}}"><img class="home-images" :src="article.image_path"></router-link>
      <div>
        <h1 class="title is-5">{{article.name}}</h1>
        <p>{{article.description.substring(0,20)+"..."}}</p>
        <p>{{article.date_added}}</p>
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
}


.main-home{
  background-color: white;
}



.msg-for-succsefully-created-user{
  background-color: #b3ffb3;
  width: 90%;
  margin: auto;
  margin-top: 15px;
  text-align: center;
  padding: 15px;

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
  width: 400px;
  // height: 400px;
  // border:dotted;
  margin: 10px;
}

.home-images:hover {
  transition: transform 0.7s, filter 0.4s linear;
  filter: grayscale(90%);
  transform: scale(0.95);
}

</style>


<script>
import axios from 'axios'
export default {
  name: 'HomeView',
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
      this.poppupShow()
    },


    methods: {
      async getArticles(){
        // 'http://127.0.0.1:8000/' base url in main.js
        await axios.get('articles/').then(response => {this.Articles = response.data}).catch(error => {console.log(error)})
      },
      poppupShow() {
        if(this.$cookies.get("user-succsesfully-created-cookie-mg-blog") || this.$cookies.get("popup-user-msg")){
          this.isVisible = true;
          this.username_created = this.$cookies.get("user-succsesfully-created-cookie-mg-blog");
          this.username_login = this.$cookies.get("popup-user-msg");
          setTimeout(() => this.isVisible = false, 5000);
        }
      },
    }
}
</script>
