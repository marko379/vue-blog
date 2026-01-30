<template>

    <div v-show="userNotLoggedIn != false" class="userNotFound">
        <h1 class="title is-3">User not found, please try again</h1>
    </div>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log in</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" name="username" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" name="password" v-model="password">
                        </div>
                    </div>


                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">login</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>


<style lang="scss">

.userNotFound{
  background-color: #ffb3b3;
  width: 90%;
  margin: auto;
  margin-top: 15px;
  text-align: center;
  padding: 15px;
}

</style>

<script>
import axios from 'axios'
// import router from 'router'
// import { toast } from 'bulma-toast'
export default {
    name: 'Login',
    data() {
        return {
            username: '',
            password: '',
            password2: '',
            userLoggedIn: null,
            userNotLoggedIn: false,
            errors: []
        }
    },

    //  after user delete profile this will be executed
    mounted() {
      if (this.$route.query.deleted === 'true') {
     
        this.$store.commit('showMsg', 'User removed successfully'); 
        this.$router.replace({ query: {} });

      }
    },



    methods: {
        submitForm() {
            let self = this;
            this.errors = []
            if (this.username === '') {
                this.errors.push('The username is missing')
            }   
            if (this.username.split(" ").map(item => item.trim()).length > 1) {

                this.errors.push('Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.')
            }
            if (this.password.length < 3 ) {
                this.errors.push('The password is too short, at least 8 charachters')
            }
            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }
                axios.post("users/login/", formData).then(function (response) {
                    if(response.data == 'UserNone'){
                        self.$store.commit('showMsg','user dose not exist')
                        return self.$router.push('/login')
                    }
                    else{
                        self.$cookies.set("user-token", response.data['user_id'])
                        self.$cookies.set("userID", response.data['userID'])
                        self.$cookies.set("user-succsess", response.data['user'])
                        localStorage.setItem('myPhoto', response.data['photo'])
                        self.$store.commit('showMsg','welcome ' + response.data['user'])                            
                        return self.$router.go(-1)
                    };
                })

            }
        },
    
    }
}
</script>