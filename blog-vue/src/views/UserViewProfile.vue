<template>

<div v-show="username == ''">
  <h1 class="title">Please login/register so that you can see your profile</h1>
</div>

<div v-show="username != ''" class="profile">
  <div>
    <h1 class="title is-5">Username: {{username}}</h1>
    <h1 class="title is-5">Email: {{email}}</h1>
    <img :src="user_photo" alt="no photo" width="200">
    <br>
    <button class="button is-medium is-danger is-rounded" @click="showModalProfile">delete this profile</button>    
  </div>
</div>


<div class="modal" ref="modalProfile">
  <div class="modal-background"></div>
  <div class="modal-card">
    <section class="modal-card-body">
      <div class="">
          <h1 class="title is-5 is-italic ml-3">Delete this profile</h1>
      </div>
    </section>
    <footer class="modal-card-foot">
      <button class="button is-success" @click="deleteProfile">Confirm</button>
      <button class="button is-danger is-outlined" @click="removeModalProfile">Cancel</button>
    </footer>
  </div>
</div>



</template>



<style lang="scss">

body{
  background-color:#f2f2f2;
}

.profile{
  display: flex;
  flex-direction: column;
  margin: auto;
  // border: solid;
  max-width: 250px;
}

</style>


<script>
import axios from 'axios'
export default {
  name: 'UserViewProfile',
    data() {
      return {
        userToken: null,
        username: '',
        email:'',
        user_photo:null,
        userID:null
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
        this.userToken = this.$cookies.get("user-token");
        await axios.get('users/profile-user/',{'headers':{'Authorization':`Token `+ this.userToken}})
        .then(response => 
          {
          this.username = response.data['user'].username,
          this.email = response.data['user'].email,
          this.user_photo = response.data['user_photo'].image_path
          }).catch(error => {console.log(error)})
      },
      showModalProfile(){
        this.$refs.modalProfile.classList.add('is-active')
      },
      logoutAfterDelete(){
          this.$cookies.remove("userID")
          this.$cookies.remove("user-succsess")
          this.$cookies.remove("user-token")
          localStorage.removeItem('myPhoto');
          this.$router.go(0)
      },
      deleteProfile(){
        const data = new FormData()
        data.append('userID', this.userID = this.$cookies.get("userID"))
        axios.post("users/delete-profile/",data).then(this.logoutAfterDelete())
        .catch(error => {console.log(error)})
      },
      removeModalProfile(){
        this.$refs.modalProfile.classList.remove('is-active')
      }
    }
}
</script>
