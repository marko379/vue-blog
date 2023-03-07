<template>
  <div>
    <div class="container-slika">
      <img src="" alt="slslslsl" class="slika" ref="aaa">
    </div>

    <br>

    <div class="blob-slika">
      <img :src="newImg" class="rounded">
    </div>

    
    <div class="file is-link">
      <label class="file-label">
        <input class="file-input" type="file" ref="xxx" v-on:change="onFileChange"/>
        <span class="file-cta">
          <span class="file-icon">
            <i class="fas fa-upload"></i>
          </span>
          <span class="file-label">
            upload image
          </span>
        </span>
      </label>
    </div>    
  </div>

  <br>

  <button class="button is-danger" @click="imageCrop">Button</button>


</template>


<style lang="scss">

.slika{
  display: block;
  /* This rule is very important, please don't ignore this */
  max-width: 100%;
  border: solid;
}

.container-slika{
  max-width:  500px;

}

.blob-slika{
  display: block;
  /* This rule is very important, please don't ignore this */
  max-width: 100%;
  border: solid;
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
import axios from 'axios'
import Cropper from 'cropperjs';
export default {
  name: 'AboutView',
  data() {
    return {
      url: null,
      cropper:null,
      newImg:null,
      canvas:null,


    }
  },

  methods: {
    onFileChange() {
      this.url = URL.createObjectURL(this.$refs.xxx.files.item(0));
    },
    imageCrop(){
      this.canvas = this.cropper.getCroppedCanvas();
      this.canvas.toBlob(blob => {this.newImg = URL.createObjectURL(blob)})
    }
  },



  watch:{
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