<template>


<div class="about">
    <h1 class="title is-6"> Tech | Healty Living | News | Buy Books   </h1>
</div>

<nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" href="">
       <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
    </a>

    <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample" @click="toggleNavBar">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div id="navbarBasicExample" class="navbar-menu" ref="xxx"> 
    <div class="navbar-start">
      <!-- <a class="navbar-item"> -->
        <router-link to="/home-page" class="navbar-item"><h1 class="title is-5">Home</h1></router-link>
      <!-- </a> -->

      <!-- <a class="navbar-item"> -->
        <router-link to="/about" class="navbar-item"><h1 class="title is-5">About</h1></router-link>
      <!-- </a> -->

      <!-- <a class="navbar-item"> -->
        <router-link to="/user-profile" class="navbar-item"><h1 class="title is-5">My profile</h1></router-link>
      <!-- </a> -->
      <router-link to="/exe" class="navbar-item"><h1 class="title is-5">exe</h1></router-link>

      <div class="navbar-item  is-hoverable  has-dropdown">  
        <a class="navbar-link">
          <h1 class="title is-5">Categories</h1>
        </a>

        <div class="navbar-dropdown">
          <!-- <a class="navbar-item"> -->
            <router-link to="/home-page" class=""><h1 class="title is-5 navbar-item">Tech</h1></router-link>
          <!-- </a> -->
          <!-- <a class="navbar-item"> -->
            <router-link to="/home-page" class="navbar-item"><h1 class="title is-5">Healty living</h1></router-link>
          <!-- </a> -->
          <!-- <a class="navbar-item"> -->
            <router-link to="/home-page" class="navbar-item"><h1 class="title is-5">News</h1></router-link>
          <!-- </a> -->
          <!-- <a class="navbar-item"> -->
            <router-link to="/home-page" class="navbar-item"><h1 class="title is-5">Books</h1></router-link>
          <!-- </a> -->
        </div>
      </div>
    </div>

    <div class="navbar-end" v-show="userLoggedIn == null ">
      <div class="navbar-item">
        <div class="buttons">
          <a class="button is-primary">
            <strong>Sign up</strong>
          </a>
          <a class="button is-light">
            Log in
          </a>
        </div>
      </div>
    </div>

    <div v-show="userLoggedIn != null ">
      <h3 class="title is-1">Hi {{userLoggedIn}}</h3>
    </div>


  </div>

    <figure class="image is-96x96">
      <img :src="userPhoto" class="is-rounded">
    </figure>
</nav>

<br>

<router-view/>
</template>


<style lang="scss">



@import '../node_modules/bulma';

#app{
  background-color: white;
}


.is-rounded{
  // width: 40px;
  // height: 40px;

}
.navbar{
  min-height: 5.3rem;

  background-color:  #99d6ff;
  // padding: 0px;

}


.about{
  display: flex;
  justify-content: center;
  width:100;
  margin: auto;
  padding:10px;
  background-color: #ffff66;
}


@media screen and (max-width: 1024px){        
    .navbar-link{
      display:none;
    }
}

</style>


<script>
import Login from '@/views/Login.vue'
import axios from 'axios'
export default {
  name: 'App',
  data() {
      return {
        userLoggedIn: null,
        showModel: false,
        userPhoto:null,
      }
    },


  mounted(){
    
  },

  watch: {
      $route(to, from) {
          console.log(to)
          if (to.name === 'home') {
            this.userLoggedIn = this.$cookies.get("user-succsess");
            this.userPhoto = localStorage.getItem('myPhoto')
              // this.getCategory()
          }
      }
  },

  methods: {
    toggleNavBar(e){
     e.target.classList.toggle("is-active")
     this.$refs['xxx'].classList.toggle("is-active");
    },

  },
}
</script>


