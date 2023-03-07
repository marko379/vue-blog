<template>
    
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign up</h1>

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
                            <input type="password" class="input" name="password" v-model="password1">
                        </div>
                    </div>

                    <div class="field">
                        <label>Repeat password</label>
                        <div class="control">
                            <input type="password" class="input" name="password2" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                     <div>
                        <input type="file" ref="image" name="image" id="image" v-on:change="selectFile"/>
                        <button  @click="upload">upload</button>
                     </div>      

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Sign up</button>
                        </div>
                    </div>

                    <hr>

                    Or <router-link to="/log-in">click here</router-link> to log in!
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
// import { toast } from 'bulma-toast'
export default {
    name: 'UserView',
    data() {
        return {
            username: '',
            password1: '',
            password2: '',
            image: null,
            errors: []
        }
    },
    methods: {
        submitForm() {
            const formData = new FormData()
            this.errors = []
            if (this.username === '') {
                this.errors.push('The username is missing')
            }
            if (this.password.length < 4 ) {
                this.errors.push('The password is too short, at least 4 charachters')
            }
            if (this.password !== this.password2) {
                this.errors.push('The passwords doesn\'t match')
            }
            if (!this.errors.length) {
                const formData = new FormData()
                formData.append('username', this.username)
                formData.append('password', this.password)
                formData.append('image', this.image)
                  axios.post("users/u/", formData)
                    .then(response => this.$router.push('/home-page'),this.$cookies.set("user-succsesfully-created-cookie-mg-blog", this.username ,"10s")).catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            
                            console.log(JSON.stringify(error))
                        }
                    })
                    
            }
        },
        selectFile(e){
          this.image = this.$refs.image.files.item(0)
          this.document = this.$refs.image.files.item(0)
          console.log(this.document)
          console.log(this.image,'kljhhhhhhhh')
        },
    }
}
</script>
