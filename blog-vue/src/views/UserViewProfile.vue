<template>

<div v-show="username == ''">
  <h1>Please login/register so that you can see your profile</h1>
</div>

<div v-show="username != ''">
  <h1 class="title is-5">Username: {{username}}</h1>
  <h1 class="title is-5">Email: {{email}}</h1>
  <img :src="user_photo" alt="no photo">
</div>


</template>



<style lang="scss">

body{
  background-color:#f2f2f2;
}


</style>


<script>
import axios from 'axios'
export default {
  name: 'UserViewProfile',
    data() {
      return {
        userLoggedIn: null,
        username: '',
        email:'',
        user_photo:null,
      }
    },

    mounted() {
      this.getUser()
    },

    // this method will return my profile page where users details will be displayed 
    // this.userLoggedIn return token of user which we use to accses/authenticate user and allows them they can see page
    // then we use token in headers , thats how authentication is done in DRF
    methods: {
      async getUser(){
        this.userLoggedIn = this.$cookies.get("user-logged-in");
        await axios.get('users/profile-user/',{'headers':{'Authorization':`Token `+this.userLoggedIn}})
        .then(response => 
          {
          this.username = response.data['user'].username,
          this.email = response.data['user'].email,
          this.user_photo = response.data['user_photo'].image_path
          }).catch(error => {console.log(error)})
      }
    }
}
</script>
