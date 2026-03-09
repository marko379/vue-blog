<template> 


  <div class="center" id="app2">

    <h3 class="title is-3">Readers also enjoyed</h3>

    <div class="carousel-row">

      <button class="button" ref="button-left" @click="buttonLeft">
        <span class="icon is-small">
          <font-awesome-icon icon="fa-solid fa-circle-chevron-left" class="third" size="6x"/>
        </span>
      </button>

      <div class="carousel-viewport">
        <div class="wrapper-carousel" ref="carousel">
          <div class="card" v-for="book in books" :key="book.id" >
            <router-link :to="{ name: 'article' ,  params: {slug: book.slug}}">
                <img :src="book.image_path" >
            </router-link>
            <div class="content">
              <!-- <h1 class="title is-5">{{book.name}}</h1> -->
            </div>
          </div>      
        </div>
      </div>

        <button class="button" ref="button-right" @click="buttonRight">
          <span class="icon is-small">
            <font-awesome-icon icon="fa-solid fa-circle-chevron-right" class="third" size="6x"/>
          </span>
        </button>
    </div>

  </div>
    


</template> 





<style lang="scss">





.center {
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  //border:solid blue;

}

.carousel-row {
  display: flex;
  align-items: center;
  justify-content: space-between; 
  gap: 3rem;
}
.carousel-row button {
  flex-shrink: 0;   /* prevents buttons from being squished */
  display: flex;
  align-items: center;
  justify-content: center;
}

.carousel-viewport {
  width: 570px;
  max-width: 1060px;
  overflow: hidden;
  margin: 0 auto;
   flex-shrink: 0;
}

.wrapper-carousel {
  display: flex;
   width: max-content; 
  gap: 10px;
  background: #ffffff !important;
  transition: transform 0.5s ease-in-out;
  // border:solid blue;
  
}

.card {
  flex: 0 0 180px;          // your card width
  flex-shrink: 0;  


}

.card img {
  width: 180px;              // fill card width
  height: 250px;            // ← fixed height (change to what you want, e.g. 300px, 350px)

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

  justify-content: center;

}

.wrapper-carousel {
  display: flex;
  grid-gap: 1em;
  overflow: hidden;

  width: 79%;
  min-width: 430px;
  border: solid;

}

.card {
  flex: 0 0 190px;
  border-radius: 0.5em;
  box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.5);
  // border:solid pink;
  width:190px;

  & > img {
    border-top-right-radius: inherit;
    border-top-left-radius: inherit;

    height: 17em;

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
import { nextTick } from 'vue'
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

    // when u press right button and  if window page is bigger then 1300px 
    // div starts from  0px, when u press right button u will move everything in div to the back for -570px
    // 
    methods: {
      buttonRight(){
        const width = this.$refs.carousel.scrollWidth
        if(window.innerWidth > 1300 ){
          if((this.count >= -570)){
            this.count = this.count - 570  
            this.$refs['carousel'].style.transform = `translateX(${this.count}px)`;
          }

        }
        else if(window.innerWidth > 800 <= 1299){
          this.count = this.count - 33
          this.$refs['carousel'].style.transform = "translateX(" + this.count + "%)";

        }
        else{
          this.count = this.count - 33
          this.$refs['carousel'].style.transform = "translateX(" + this.count + "%)";
        }


      },
      buttonLeft(){

        if(window.innerWidth > 1300 ){
           
          if((this.count < 0)){
            this.count = this.count + 570   
            this.$refs['carousel'].style.transform = `translateX(${this.count}px)`;
          }
    
          console.log(this.count)

        }else{
          this.count = this.count + 22    
          this.$refs['carousel'].style.transform = "translateX(" + this.count + "%)";
        }
      },
      getBooksForCarousel(carousel_genre){
        let data_genres = []
        carousel_genre.forEach((item) => {
          data_genres.push(item);
        });
        
          axios.get("articles/carousel-books/", {
            params: {
              genre1: carousel_genre[0] || '',
              genre2: carousel_genre[1] || '',
              exclude_book_slug: this.$route.params.slug || ''
            }
          })
          .then(response => {this.books = response.data})
          .catch(error => console.log(error));


      },

    },

    watch: { 
        genres (value) {
          console.log(value,'lllllllll')
          this.getBooksForCarousel(value)
        }

    }

}
</script>

