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

                    <hr>

                    Or <router-link to="/log-in">click here</router-link> to log in!
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

    mounted(){
    },
    methods: {
        submitForm() {
            let self = this;
            this.errors = []
            if (this.username === '') {
                this.errors.push('The username is missing')
            }
            if (this.password.length < 4 ) {
                this.errors.push('The password is too short, at least 8 charachters')
            }
            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }
                axios.post("users/login/", formData).then(function (response) {
                        // if respone is UserNone then execute code bellow and return login (same page)
                        if(response.data == 'UserNone'){
                            // this function is implemented just to show pop up message for 15 sec that user is not logged in
                            self.userNotLoggedIn = true
                            setTimeout(() => self.userNotLoggedIn = false, 15000);
                            return '/login'
                        }else{
                            // if response.data is != 'UserNone' then execute code bellow
                            // self.$cookies.set("user-succsess", response.data['user']) we this cookie we just showing client that useer is logged in, we can grab that cookie from anywhere and display it
                            //  self.$cookies.set("user-logged-in", response.data['user_id']) with this cookie we get token so we can put Authentication for same pages,profile page can be seen just for Authenticated users,check UserViewProfile page 
                            self.$cookies.set("user-succsess", response.data['user'])
                            self.$cookies.set("user-logged-in", response.data['user_id'])
                            self.$cookies.set("popup-user-msg", response.data['user'],20)
                            self.$cookies.set("userID", response.data['userID'])
                            // with local storage we can accsess my photo(user) from anywhere in the app
                            localStorage.setItem('myPhoto', response.data['photo'])
                            console.log(response.data['photo'])
                            return '/home-page'
                        };
                      // value will be return from if or else  (return '/login' or return '/home-page')
                      }).then(value => this.$router.push(value))

                      .catch(function (error) {
                        console.log(error);
                });
            }
        },
    
    }
}
</script>