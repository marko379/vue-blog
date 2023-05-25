<template> 

  <h3 class="title is-3">Similar books</h3>

  <div class="center" id="app2">
    <div class="wrapper-carousel">
      <div class="inner" ref="inner">
        <!-- @click="getBook(book.slug)" -->
        <div class="card" v-for="book in books" :key="book.id">
          <router-link :to="{ name: 'article' ,  params: {slug: book.slug}}">
              <img :src="book.image_path" >
          </router-link>
          <div class="content">
            <h1>{{book.name}}</h1>
          </div>
        </div>          


      </div>
    </div>
    
    <div class="map" @click="newx">
      <button class="button" ref="button-left" @click="buttonLeft">
        <span class="icon is-small">
          <font-awesome-icon icon="fa-solid fa-arrow-left" class="third" size="2x"/>
        </span>
      </button>

      <button class="button" ref="button-right" @click="buttonRight">
        <span class="icon is-small">
          <font-awesome-icon icon="fa-solid fa-arrow-right" class="third" size="2x"/>
        </span>
      </button>

    </div>
  </div>
    


</template> 




<style lang="scss">



@mixin circle($i) {
  border-radius: 100%;
  height: $i;
  width: $i;
}

$bgBlue: #001d38;
$cardBlue: #0a2640;
$font: "Poppins";


.center {
  align-items: center;
  display: flex;
  flex-direction: column;
  // height: 100%;
  // background-color: red;
  justify-content: center;
  // border:solid;
}

.wrapper-carousel {
  display: flex;
  grid-gap: 1em;
  overflow: hidden;
  // width: 92%;
  width: 79%;
  min-width: 630px;
  border: solid;

  // border:solid red;
  
  & > .inner {
    display: flex;
    grid-gap: 1em;
    transition: all 1s ease-in-out;
  }
}

.card {
  border-radius: 0.5em;
  box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.5);
  // border:solid pink;
  width:190px;

  & > img {
    border-top-right-radius: inherit;
    border-top-left-radius: inherit;
    // display: block;
    // width: 24em;
    height: 17em;
    // border: solid green;
    // width: 100%;
  }

  & > .content {
    background: $cardBlue;
    border-bottom-left-radius: inherit;
    border-bottom-right-radius: inherit;
    padding: 1em;
    text-align: center;
    // border:solid red;
    height: 120px;

    & > h1,
    & > h3 {
      margin: 0.35em 0;
    }

    & > h1 {
      color: #fff;
      font-size: 1.25rem;
      line-height: 1;
    }

    & > h3 {
      color: #ccc;
      font-size: 0.9rem;
      font-weight: 300;
    }
  }
}

.map{
  width: 100%;
  // border:solid;
  display: flex;
  justify-content: space-around;
}




@media only screen and (max-width: 1300px) {
@mixin circle($i) {
  border-radius: 100%;
  height: $i;
  width: $i;
}

$bgBlue: #001d38;
$cardBlue: #0a2640;
$font: "Poppins";


.center {
  align-items: center;
  display: flex;
  flex-direction: column;
  // height: 100%;
  // background-color: red;
  justify-content: center;
  // border:solid;
}

.wrapper-carousel {
  display: flex;
  grid-gap: 1em;
  overflow: hidden;
  // width: 92%;
  width: 79%;
  min-width: 430px;
  border: solid;

  // border:solid red;
  
  & > .inner {
    display: flex;
    grid-gap: 1em;
    transition: all 1s ease-in-out;
  }
}

.card {
  border-radius: 0.5em;
  box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.5);
  // border:solid pink;
  width:190px;

  & > img {
    border-top-right-radius: inherit;
    border-top-left-radius: inherit;
    // display: block;
    // width: 24em;
    height: 17em;
    // border: solid green;
    // width: 100%;
  }

  & > .content {
    background: $cardBlue;
    border-bottom-left-radius: inherit;
    border-bottom-right-radius: inherit;
    padding: 1em;
    text-align: center;
    // border:solid red;
    height: 120px;

    & > h1,
    & > h3 {
      margin: 0.35em 0;
    }

    & > h1 {
      color: #fff;
      font-size: 1.25rem;
      line-height: 1;
    }

    & > h3 {
      color: #ccc;
      font-size: 0.9rem;
      font-weight: 300;
    }
  }
}

.map{
  width: 100%;
  // border:solid;
  display: flex;
  justify-content: space-around;
}


}


</style>





<script>
import axios from 'axios'
export default {
    props: ['genres'],
    emits: ['carouselBook'],
    name: 'Carousel',

    data() {
        return {
          books:[],
          count: 0,
          screenWidth: 0
        }
    },

    mounted(){
      this.screenWidth = window.innerWidth

    },

    methods: {
      buttonRight(){
        if(window.innerWidth > 200 && window.innerWidth <= 800 ){
          this.count = this.count - 22    
          this.$refs['inner'].style.transform = "translateX(" + this.count + "%)";
        }
        else if(window.innerWidth > 800 <= 1299){
          this.count = this.count - 33
          this.$refs['inner'].style.transform = "translateX(" + this.count + "%)";
        }
        else{
          this.count = this.count - 33
          this.$refs['inner'].style.transform = "translateX(" + this.count + "%)";
        }


      },
      buttonLeft(){
        if(window.innerWidth > 1300){
          this.count = this.count + 33    
          console.log(this.count)
          this.$refs['inner'].style.transform = "translateX(" + this.count + "%)";
        }else{
          this.count = this.count + 22    
          this.$refs['inner'].style.transform = "translateX(" + this.count + "%)";
        }
      },
      getBooksForCarousel(carousel_genre){
        let data = new FormData()
        carousel_genre.forEach((item) => {
          data.append(item,item);
        });
        
        axios.post("articles/carousel-books/", data)
        .then(response => {this.books = response.data}).catch(error => {console.log(error)})
      },

    },

    watch: { 
        genres (value) {
          console.log(value)
          this.getBooksForCarousel(value)
        }

    }

}
</script>

