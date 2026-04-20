<template>

<div id="app">



<div class="nav-container">

<nav class="my-nav">

  <div class="main-nav">
      <router-link to="/home-page" class="router-link"><h1 class="title is-5 my-nav-link">Home</h1></router-link>

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
          <img v-show="$store.state.count == 0" src="https://res.cloudinary.com/dzxfhtmis/image/upload/v1775246300/m3glicprqil6hcsjrvju.png"  width="45" >
          <img v-show="$store.state.count > 0" src="https://res.cloudinary.com/dzxfhtmis/image/upload/v1775246342/swxumgqkzflbdtyumktz.png"  width="45">
          <h1 class="title is-2" style="color:#8B5E3C;"> {{$store.state.count}}</h1>  
        </div>
        <div class="popout-basket" v-show="basket">
          <div class="popout-basket-button" v-if="$store.state.totalPrice.toFixed(2) > 1">
            <button class="button is-fullwidth is-success is-large" @click="showModalApp">checkout £{{$store.state.totalPrice.toFixed(2)}}</button>
          </div>
          <div class="popout-basket-button" v-else>
            <h1 class="title is-1">Basket is empty!</h1>
            <h1 class="title is-1">🙁</h1>
          </div>
          <div class="basket-items-container">
            <div v-for="item , index in $store.state.basketList">
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
        <!-- <button class="button"><router-link to="/register"><h1 class="title is-5">Sing-up</h1></router-link></button> -->
        <div><router-link to="/register" class="btn">Sing-up</router-link></div>
        <!-- <button class="button"><router-link to="/login"><h1 class="title is-5">Login</h1></router-link></button> -->
        <div><router-link to="/login" class="btn">Login</router-link></div>
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



  <div class="message-pop-out" v-show="$store.state.popOutMsg != null">
     <h1 class="title is-3">{{$store.state.popOutMsg}}</h1>
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

<div class="quote-container">
  <div class="quote">
    “{{ currentQuote.text }}”
    <span class="author">{{ currentQuote.author }}</span>
  </div>
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

body {
  background-color: #F5F5F5;  /* soft white */
  color: #333333;
}


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
        index:0,

      quotes: [
        { text: "A room without books is like a body without a soul.", author: "Cicero" },
        { text: "I cannot live without books.", author: "Thomas Jefferson" },
        { text: "Books are a uniquely portable magic.", author: "Stephen King" },
        { text: "There is no friend as loyal as a book.", author: "Ernest Hemingway" },
        { text: "A book is a dream you hold in your hand.", author: "Neil Gaiman" },
        { text: "Books are the quietest and most constant of friends.", author: "Charles W. Eliot" },
        { text: "So many books, so little time.", author: "Frank Zappa" },
        { text: "A book is a gift you can open again and again.", author: "Garrison Keillor" },
        { text: "Reading helps you rise above the ordinary.", author: "Jim Rohn" },
        { text: "Books are the mirrors of the soul.", author: "Virginia Woolf" },
        { text: "The more you read, the more you will know.", author: "Dr. Seuss" },
        { text: "A good book is an event in my life.", author: "Stendhal" },
        { text: "Books are the plane, the train, and the road.", author: "Anna Quindlen" },
        { text: "Read widely or you’ll only think like others.", author: "Haruki Murakami" },
        { text: "Books are my friends and companions.", author: "Christopher Morley" },
        { text: "A house without books lacks windows.", author: "Horace Mann" },
        { text: "Reading brings us unknown friends.", author: "Honoré de Balzac" },
        { text: "Books are compasses and charts of the mind.", author: "Ralph Waldo Emerson" },
        { text: "Paradise will be a kind of library.", author: "Jorge Luis Borges" },
        { text: "Not reading books is worse than burning them.", author: "Joseph Brodsky" },
        { text: "Books are the treasured wealth of the world.", author: "Henry David Thoreau" },
        { text: "A great book leaves you with many experiences.", author: "Nadine Gordimer" },
        { text: "Books transport us to new worlds.", author: "Unknown" },
        { text: "Reading is exercise for the mind.", author: "Joseph Addison" },
        { text: "A book is a garden carried in the pocket.", author: "Chinese Proverb" },
        { text: "The world is a book; some read only one page.", author: "Augustine of Hippo" },
        { text: "One glance at a book and you hear another voice.", author: "You Xia" },
        { text: "A book is a version of the world.", author: "Susan Sontag" },
        { text: "Books are the carriers of civilization.", author: "Barbara W. Tuchman" },
        { text: "I love books. I adore everything about them.", author: "Lemony Snicket" },
        { text: "Books are food for the soul.", author: "Unknown" },
        { text: "Reading talks with the finest minds.", author: "Unknown" },
        { text: "A good book is the best of friends.", author: "Martin Farquhar Tupper" },
        { text: "Books are legacies from great minds.", author: "Joseph Addison" },
        { text: "The book you don’t read won’t help.", author: "Jim Rohn" }
      ]



       
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

  // computed reacts whenever value(index) inside of it change... thats how computed works...
  //   A computed property: Depends on reactive data (like data, props, or other computed values)
  // Recalculates only when those dependencies change
  // Is cached (unlike methods)
  computed: {
    currentQuote() {
      return this.quotes[this.index];
    }
  },

  mounted(){
      this.$store.state.userId = this.$cookies.get("userID");
      this.$store.state.userImage = localStorage.getItem('myPhoto')
      this.$store.state.username = this.$cookies.get("user-succsess");
      this.getBooks()
      this.startQuotes();
  },

  methods: {
    showBasket(){
      this.basket = true
    },
    hideBasket(){
      this.basket = false
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
    },

    startQuotes() {
      setInterval(() => {
        this.index = (this.index + 1) % this.quotes.length;
      }, 4000);
    }

  }

}
</script>
