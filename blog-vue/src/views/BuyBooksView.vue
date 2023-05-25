<template>

<div class="modal" ref="payment_button">
  <div class="modal-background"></div>
  <div class="modal-card">
    <header class="modal-card-head">
      <h3 class="title is-3">procesing payment</h3>
    </header>
    <section class="modal-card-body modal-body">
      <div class="loader"></div>
    </section>
    <footer class="modal-card-foot">
      <h3 class="title is-3">it may take a few min</h3>
    </footer>
  </div>
</div>



<div class="row">
  <div class="col-75">
    <div class="container-main">
      <form action="" method="POST">
    <div class="notification is-danger" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
    </div>
        <div class="row">
          <div class="col-50">
            <h3 class="title is-3">Billing Address</h3>
            <label for="fname"><font-awesome-icon icon="fa-solid fa-user" /> Full Name</label>
            <input type="text" id="fname" v-model="fname" name="firstname" placeholder="John M. Doe">
            <label for="email"><font-awesome-icon icon="fa-solid fa-envelope" /> Email</label>
            <input type="text" id="email" v-model="email" name="email" placeholder="john@example.com">
            <label for="adr"><font-awesome-icon icon="fa-solid fa-house" /> Address</label>
            <input type="text" id="adr" v-model="adr" name="address" placeholder="542 W. 15th Street">
            <label for="city"><font-awesome-icon icon="fa-solid fa-building-columns" /> City</label>
            <input type="text" id="city" v-model="city" name="city" placeholder="London">

            <div class="row">
              <div class="col-50">
                <label for="state"> <font-awesome-icon icon="fa-solid fa-location-dot" /> Postcode</label>
                <input type="text" v-model="state" id="state" name="state" placeholder="W8 6ED">
              </div>
              <div class="col-50">
                <label for="zip">Zip</label>
                <input type="text" v-model="zip" id="zip" name="zip" placeholder="10001">
              </div>
            </div>
          </div>

          <div class="col-50">
            <h3 class="title is-3">Payment</h3>
            <label for="fname">Accepted Cards</label>
            <div class="icon-container">
              <font-awesome-icon icon="fa-brands fa-cc-visa" style="color:navy;" class="bank-cards"/>
              <font-awesome-icon icon="fa-brands fa-cc-amex" style="color:red;" class="bank-cards"/>
              <font-awesome-icon icon="fa-brands fa-cc-mastercard" style="color:green;" class="bank-cards"/>

            </div>
            <label for="cname">Name on Card</label>
            <input type="text" v-model="cname" id="cname" name="cardname" placeholder="John More Doe">
            <label for="ccnum">Credit card number</label>
            <input type="text" id="ccnum" v-model="ccnum" name="cardnumber" placeholder="1111-2222-3333-4444">
            <label for="expmonth">Exp Month</label>
            <input type="text" id="expmonth" v-model="expmonth" name="expmonth" placeholder="September">

            <div class="row">
              <div class="col-50">
                <label for="expyear">Exp Year</label>
                <input type="text" id="expyear" v-model="expyear" name="expyear" placeholder="2027">
              </div>
              <div class="col-50">
                <label for="cvv">CVV</label>
                <input type="text" v-model="cvv"  id="cvv" name="cvv" placeholder="352">
              </div>
            </div>
          </div>
        </div>
      </form>
      <button class="button is-medium is-fullwidth is-success" @click="pay">Pay</button>
    </div>
  </div>

  <div class="col-25">
    <div class="container-main">
      <h4>Cart
        <span class="price" style="color:black">
          <i class="fa fa-shopping-cart"></i>
          <b>{{$store.state.count}}</b>
        </span>
      </h4>
      <p v-for="book,index in $store.state.basketList">
        <font-awesome-icon icon="fa-solid fa-trash" @click="removeFromCart(index,book['slug']); subtractPrice(book['price']);" class="remove-book-cart-icon"/>
        <router-link :to="{ name: 'article' ,  params: {slug: book['slug'] }}"><span class="book-name-cart">{{book['book-name']}}</span></router-link>
        <span class="price">£{{book['price']}}</span>
      </p>
      <hr>
      <p>Total <span class="price" style="color:black"><b>£{{$store.state.totalPrice.toFixed(2)}}</b></span></p>
    </div>
  </div>
</div>

</template>

<style lang="scss">

@import '@/assets/css/BuyBooksViewCss.css';


</style>


<script>
import axios from 'axios'

export default {
  name: 'BuyBooksView',
  components: {

  },
  data() {
    return {
      fname:'',
      email:'',
      adr:'',
      city:'',
      state:'',
      zip:'',
      cname:'',
      ccnum:'',
      expmonth:'',
      expyear:'',
      cvv:'',
      errors:[]

    }
  },

  methods: {
    pay(){
      this.errors = []
      let card_number = /^\d+$/.test(this.ccnum);
      let year = /^\d+$/.test(this.expyear);
      let cvv = /^\d+$/.test(this.cvv);
      if (this.fname.length < 2) {
        this.errors.push('The username is wrong')
        this.fname=''
      }
      if (this.email.split(" ").map(item => item.trim()).length > 1 || !this.email.includes('@')){
          this.errors.push('Enter a valid email.')
          this.email=''
      }
      if (this.adr.length < 5) {
        this.errors.push('Enter a valid address.')
        this.adr=''
      }
      if (this.city.length < 2) {
        this.errors.push('Enter a valid city.')
        this.city=''
      }
      if (this.zip.length < 5) {
        this.errors.push('Enter a valid postcode.')
        this.zip=''
      }
      if (this.cname.length < 1) {
        this.errors.push('Enter a valid card name.')
        this.cname=''
      }
      if (card_number == false || this.ccnum.split(" ").map(item => item.trim()).length > 1 || this.ccnum.length != 16 ) {
        this.errors.push('Enter a valid card number.')
        this.ccnum=''
      }
      if (year == false || this.expyear.length != 4 ) {
        this.errors.push('Enter a valid year.')
        this.ccnum=''
      }
      if (cvv == false || this.cvv.length != 3 ) {
        this.errors.push('Enter a valid cvv.')
        this.ccnum=''
      }

      if(!this.errors.length){
        this.$refs.payment_button.classList.add('is-active')
        setTimeout(() => {
          this.$refs.payment_button.classList.remove('is-active')
          this.payment_successful()
          this.$store.commit('paymentMsg')
        }, 3000);
      } 

    },
    payment_successful(){
      this.$router.push({name: 'home'})
    },

    removeFromCart(index,slug){
      this.$store.commit('removeFromBasketStore',index)
      if(this.$cookies.get("userID") || this.$store.state.userId){
        const data = new FormData()
        data.append('user_id', this.$cookies.get("userID"))
        data.append('slug', slug)
        axios.post("articles/delete-book-from-basket/",data)
      }
    },
    subtractPrice(subtractPrice){
      this.$store.commit('subtractPriceStore',subtractPrice)
    }
  }

}

</script>