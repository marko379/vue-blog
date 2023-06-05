<template>

<div id="app">


<div class="nav-container">

<nav class="my-nav">

  <div class="main-nav">
      <router-link to="/home-page"><h1 class="title is-5 my-nav-link">Home</h1></router-link>

      <router-link to="/user-profile"><h1 class="title is-5 my-nav-link">Profile</h1></router-link>


      <!-- categories -->
      <div class="dropdown is-hoverable ">
        <div class="dropdown-trigger">
           <h1 class="title is-5 my-nav-link"><font-awesome-icon icon="fa-solid fa-arrow-down" /> Categories</h1>
        </div>
        <div class="dropdown-menu" id="dropdown-menu4" role="menu">
          <div class="dropdown-content">
            <div class="dropdown-item">
                <router-link :to="{ name: 'search-book-by-genre', params: { genre: 'Horror' }}" class="navbar-item" ><h1 class="title is-5" >Horror</h1></router-link>
                <router-link :to="{ name: 'search-book-by-genre', params: { genre: 'Health' }}" class="navbar-item" ><h1 class="title is-5" >Health</h1></router-link>
                <router-link :to="{ name: 'search-book-by-genre', params: { genre: 'Adventure' }}" class="navbar-item" ><h1 class="title is-5" >Adventure</h1></router-link>
                <router-link :to="{ name: 'search-book-by-genre', params: { genre: 'Thriller' }}" class="navbar-item" ><h1 class="title is-5" >Thriller</h1></router-link>
                <router-link :to="{ name: 'search-book-by-genre', params: { genre: 'Romance' }}" class="navbar-item" ><h1 class="title is-5" >Romance</h1></router-link>
                <router-link :to="{ name: 'search-book-by-genre', params: { genre: 'Crime' }}" class="navbar-item" ><h1 class="title is-5" >Crime</h1></router-link>
                <router-link :to="{ name: 'search-book-by-genre', params: { genre: 'Science-Fiction' }}" class="navbar-item"><h1 class="title is-5" >Science Fiction</h1></router-link> 
            </div>
          </div>
        </div>
      </div>
  </div>

      <!-- popout basket window  -->
      <div class="basket-container"  @mouseover="showBasket" @mouseleave="hideBasket">
        <div class="basket-icon">
          <font-awesome-icon icon="fa-solid fa-cart-shopping" size="3x"/>
          <h1 class="title is-2">{{$store.state.count}}</h1>  
        </div>
        <div class="popout-basket" v-show="basket">
          <div class="popout-basket-button" v-if="$store.state.totalPrice.toFixed(2) > 1">
            <button class="button is-fullwidth is-success is-large" @click="showModalApp">checkout £{{$store.state.totalPrice.toFixed(2)}}</button>
          </div>
          <div class="popout-basket-button" v-else>
            <h1 class="title is-1">There are not any books in the basket yet :(</h1>
          </div>
          <div class="basket-items-container">
            <div  v-for="item , index in $store.state.basketList">
              <div class="basket-items">
                <div>
                  <img :src="item['book-photo']" alt="" width="70">
                  <p>{{item['book-name']}}</p>       
                </div>
                <div>
                  <p class="basket-paragraf-price">£{{item['price']}}</p>
                  <button class="button is-small is-danger is-rounded remove-button-basket" @click="removeFromBasket(index,item['slug']); subtractPrice(item['price']); removeBookPopUpMsg()">remove</button>  
                </div>
              </div>
              <hr>
            </div>
          </div>
        </div>
      </div>


  <div class="modal" ref="modalApp">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head is-flex is-justify-content-space-between">
        <div><p class="modal-card-title">you're buying {{$store.state.count}} book</p></div> 
        <div><p class="modal-card-title has-text-dark has-text-weight-bold">total: {{$store.state.totalPrice.toFixed(2)}}</p></div> 
      </header>
      <section class="modal-card-body">
        <div class="is-flex m-2" v-for="book in $store.state.basketList">
          <img :src="book['book-photo']" width="70">
          <div>
            <h1 class="title is-5 is-italic ml-3">{{book['book-name']}}</h1>
            <h1 class="title is-5 is-italic ml-3">£{{book['price']}}</h1>
          </div>
        </div>
        
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" @click="removeModalApp"><router-link to="/books-checkout">Confirm</router-link></button>
        <button class="button is-danger is-outlined" @click="removeModalApp">Cancel</button>
      </footer>
    </div>
  </div>


  <div class="navbar-end" v-if="$store.state.userId == null">
    <div class="navbar-item">
      <div class="buttons">
        <button class="button"><router-link to="/register"><h1 class="title is-5">Sing-up</h1></router-link></button>
        <button class="button"><router-link to="/login"><h1 class="title is-5">Login</h1></router-link></button>
      </div>
    </div>
  </div>


  <div class="username-photo-container-main" v-show="$store.state.userId != null">
    <div class="username-photo-container">
      <div class="username-photo" @mouseover="showLogout" v-if="user">
        <figure class="image is-48x48 user-image">
          <img :src="$store.state.userImage" class="is-rounded">
        </figure>

        <div v-show="$store.state.userId != null" class="user-username">
          <h3 class="title is-3">{{$store.state.username}}</h3>
        </div>
      </div>

      <div @mouseleave="hideLogout" class="logout-icon" v-if="Logout">
        <a class="button is-info logout-button is-fullwidth" @click="logout">
          <span class="icon">
            <font-awesome-icon icon="fa-solid fa-right-from-bracket" size="2x"/>
          </span>
          <h1 class="title is-5" style="color:white;"> log me out</h1>
        </a>
      </div>
    </div>
  </div>



  <div class="message-pop-out" v-show="$store.state.popOutMsg != null" >
     <h1 class="title is-4 " >{{$store.state.popOutMsg}}</h1>
  </div>

  <div class="message-pop-out-basket" v-show="$store.state.popOutMsgBasket != null" >
     <h1 class="title is-4 " >{{$store.state.count}}-{{$store.state.popOutMsgBasket}}</h1>
  </div>

  <div class="message-payment" v-show="$store.state.paymentMessage === true" >
     <h1 class="title is-3 " >Payment succsefull</h1>
     <h1 class="title is-3 " >Confirmation email will be send shortly</h1>
  </div>

</nav>

</div>


<div class="field has-addons search-container">
  <div class="control is-expanded">
    <input class="input is-hovered" type="text" v-model="value" placeholder="Find a book">
  </div>
  <div class="control">
    <a class="button is-info">
      <span class="icon is-small">
        <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
      </span>
      <router-link :to="{ name: 'search', params: { data: value }}"><h1 class="title is-5" style="color:white;">Search</h1></router-link>
    </a>
  </div>
</div>


<router-view :key="$route.fullPath"></router-view>

</div>
</template>


<style lang="scss">

@import '../node_modules/bulma';

@import '@/assets/css/AppCss.css';

</style>




<script>
import Login from '@/views/Login.vue'
import axios from 'axios'
export default {
  name: 'App',
  data() {
      return {
        showModel: false,
        basket:false,
        Logout:false,
        value:null,
        l:[],
        price:0,
        user:true,
      }
    },

  watch: {
    // you can use from or to , 
    $route(to, from) {
      if (from.name === 'log-in') {
        this.$store.state.userId = this.$cookies.get("userID");
        this.$store.state.userImage = localStorage.getItem('myPhoto')
        this.$store.state.username = this.$cookies.get("user-succsess");
        this.getBooks()
      }
    }
  },

  mounted(){
      this.$store.state.userId = this.$cookies.get("userID");
      this.$store.state.userImage = localStorage.getItem('myPhoto')
      this.$store.state.username = this.$cookies.get("user-succsess");
      this.getBooks()
  },

  methods: {
    showBasket(){
      this.basket = true
    },
    hideBasket(){
      this.basket = false
      console.log('leave')
    },
    showLogout(){
      this.Logout = true
      this.user = false
    },
    hideLogout(){
      this.Logout = false
      this.user = true
    },
    removeFromBasket(removeItemIndex,slug){
      this.$store.commit('removeFromBasketStore',removeItemIndex)
      if(this.$cookies.get("userID") || this.$store.state.userId){
        const data = new FormData()
        data.append('user_id', this.$cookies.get("userID"))
        data.append('slug', slug)
        axios.post("articles/delete-book-from-basket/",data)
      }
      if(this.$store.state.basketList.length == 0){
        this.basket = false
      }
    },
    subtractPrice(subtractPrice){
      this.$store.commit('subtractPriceStore',subtractPrice)
    },
    removeBookPopUpMsg(){
      this.$store.commit('showMsg','book removed from the basket')
    },
    getBooks(){
        var self = this
        if(this.$cookies.get("userID") || this.$store.state.userId){
          const data = new FormData()
          data.append('user_id', this.$cookies.get("userID"))
          axios.post("articles/get-books-from-basket/",data).
          then(response =>{
            console.log(response.data)
            response.data.forEach(function(item){
              self.price += item.book_price
              self.l.push(item.book)
              self.l.push(item.book_price)
              self.l.push(item.image_path)
              self.l.push(item.slug)
              self.$store.commit('addBookToBasket',self.l)
              self.l = []            
            }); self.$store.state.totalPrice = self.price
          }).catch(error => {console.log(error)})
      }
    },
    logout(){
        this.$cookies.remove("userID")
        this.$cookies.remove("user-succsess")
        this.$cookies.remove("user-token")
        localStorage.removeItem('myPhoto');
        this.$router.go(0)
    },
    searchGenre(genre){
      axios.get(`/articles/books-by-genres/${genre}/`)
        .then(response => {console.log(response.data)})
        .catch(error => {console.log(error)})
    },
    showModalApp(){
      this.$refs.modalApp.classList.add('is-active')
    },
    removeModalApp(){
      this.$refs.modalApp.classList.remove('is-active')
    }

  }

}
</script>
