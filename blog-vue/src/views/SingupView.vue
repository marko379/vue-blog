<template>

<div class="page-sign-up">
    <div class="columns">
        <div class="column is-4 is-offset-4">
            <h1 class="title">Sign up</h1>

            <form @submit.prevent="submitForm">
                <div class="field">
                    <label>Required</label>
                    <div class="control">
                        <input type="text" class="input" name="username" v-model="username" placeholder="Username">
                    </div>
                </div>

                <div class="field">
                    <label>Required</label>
                    <div class="control">
                        <input type="password" class="input" name="password1" v-model="password1" placeholder="Password">
                    </div>
                </div>

                <div class="field">
                    <label>Required</label>
                    <div class="control">
                        <input type="password" class="input" name="password2" v-model="password2" placeholder="Repeat Password">
                    </div>
                </div>

                <div class="notification is-danger" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <!-- this is just to select file -->
                <p>Optional</p>
                <div class="file is-link">
                  <label class="file-label">
                    <input class="file-input" type="file" ref="image" name="image" id="image" v-on:change="selectFile"/>
                    <span class="file-cta">
                      <span class="file-icon">
                        <i class="fas fa-upload"></i>
                      </span>
                      <span class="file-label">
                        {{file}}
                      </span>
                    </span>
                  </label>
                </div>

                <hr>
                
                <div class="cropped-photos-div" v-show="image">
                    <h3 class="title is-3" >Your profile photo</h3>
                    <div class="container-slika">
                        <img src="" alt="" class="slika" ref="aaa">
                    </div>

                    <br>

                    <div class="blob-slika">
                        <h3 class="title is-5" v-show="canvas==null">Make your avatar</h3>
                        <img :src="avatar"  class="rounded">
                        <h3 class="title is-5" v-show="canvas==null">you do not have avatar yet</h3>
                        <h3 class="title is-5" v-show="canvas!=null">your avatar</h3>
                    </div>
                    <button class="button is-success" type="button" @click="imageCrop">Avatar-click me</button>
                </div>

                <br>                   

                <div class="field">
                    <div class="control button-field">
                        <button class="button is-success is-fullwidth">Sign up</button>
                    </div>
                </div>
                or <router-link to="/log-in">click here</router-link> to log in!

            </form>
        </div>
    </div>

</div>

</template>


<style lang="scss">


.field{
    // border:solid red;
}
.button-field{
    margin: auto;
    // border:solid;
    width:200px;
}

.page-sign-up{
    display: flex;
    justify-content: space-around;
    // border: solid;
}

.columns{
    width: 700px;
    // border: solid red;
}

.cropped-photos-div{
    width: 300px;
    // border: solid blue;
}

.slika{
  display: block;
  /* This rule is very important, please don't ignore this */
  max-width: 100%;
  // border: solid;
}

.container-slika{
  max-width:  500px;

}

.blob-slika{
  display: block;
  /* This rule is very important, please don't ignore this */
  max-width: 100%;
  // border: solid;
}

.blob-img{
  max-width:  100px;

}

.cropper-view-box,
.cropper-face{
  border-radius: 50%;
}
.rounded {
  object-fit: cover;
  border-radius: 50%;
  height: 100px;
  width: 100px;
}
</style>





<script>
import Cropper from 'cropperjs'
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
            file: 'Uplode your image',
            errors: [],
            url: null,
            cropper:null,
            canvas:null,
            avatar:null,
            avatar2: null,

        }
    },
    methods: {
        submitForm() {
            let self = this;
            const data = new FormData()
            this.errors = []
            if (this.username.length > 10) {
                this.errors.push('The username is too long, 10 characters max')
            }   
            if (!this.errors.length) {
                data.append('username', this.username)
                data.append('password1', this.password1)
                data.append('password2', this.password2)
                data.append('image', this.image)
                data.append('avatar', this.avatar2)
                  
                axios.post("users/register/", data).then(response =>{
                    if (response.data.success == 'user created'){
                        this.$store.commit('showMsg','welcome ' + response.data.name_of_user)                            
                        return this.$router.go(-1)
                    }

                    if(response.data.password2){
                        for (var i = 0; i < response.data.password2.length; i++){
                            self.errors.push(response.data.password2[i].message)
                        }

                    }
                    if(response.data.username){
                        for (var i = 0; i < response.data.username.length; i++){
                            self.errors.push(response.data.username[i].message)
                        }
                    }

                    this.username = ''
                    this.password1 = ''
                    this.password2 = ''
                    this.file = 'Uplode your image'
                    this.image = null
                    this.avatar = null
                })
                    
            }
        },
        selectFile(e){
          this.image = this.$refs.image.files.item(0)
          this.document = this.$refs.image.files.item(0)
          this.file = this.image.name
          this.url = URL.createObjectURL(this.$refs.image.files.item(0));


        },
        imageCrop(){
          this.canvas = this.cropper.getCroppedCanvas({width: 100,height: 100}); //
          this.canvas.toBlob(blob => {this.avatar = URL.createObjectURL(blob),this.avatar2 = new File([blob],this.file ,{ type: "image/png" })})
        }
    },

      watch:{
        // ovaj watch koristimo da provjerimo dali cropper ima sliku zato sto ako zelimo umetnut novu sliku u croper prvo trebao destroy() staru sliku u cropperu  da bi mogli umetnut novu 
        // ovaj url si ti deklariro u data... to nije url iz pretrazivaca
        // url predstavlja sliku to je samo ime varijable ,nema nist sa url iz pretrazivaca 
        // val represents whatever is url        
        url:function(val){
          this.$refs.aaa.src = this.url
          if (this.cropper == null){
            this.cropper = new Cropper(this.$refs.aaa, {
                 aspectRatio: 1,
            });
          }
          else if(this.cropper != null){
            this.cropper.destroy()
            this.cropper = new Cropper(this.$refs.aaa, {
                 aspectRatio: 1,
            });      
          }
        }
      }
}
</script>


