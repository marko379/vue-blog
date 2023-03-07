<template>

<div class="main-article-container">


  <div class="imagee">
    <img :src="Article.image_path">
    <RatingStarsSystem  :showStarUser="showStarUser" :slug="slugg" @starsGrade="publishStar"/> 
  </div>

  <div class="main-container">

    <div class="main-container-2">


        <div class="article-title">
          <h1 class="title is-1 is-italic">{{Article.name}}</h1>
        </div>

        <h1 class="title is-4 ">Aldous Huxley</h1>

        <ArticleStars :datax="datax" :totalStars="totalStars" :numOfComments="Comments.length"/> 

        <h1 class="title is-6">Genres: crime horor sc-fi</h1>

        <p>{{Article.description_1st_part}}<span v-show="secondPart">{{Article.description_2nd_part}}</span></p>
        <button class="button is-text" @click="readMoreLess" ref="buttonReadMore">Read More</button>

        <hr>

        <button class="button is-medium is-fullwidth">Leave a comment</button>



        <div class="Comment-Component">
          <!-- remember u are passing props from here to CommentComponent (child component) -->
          <!-- remember u are triggering also emit over here  @myComment="publish" -->
          <!-- <div class="sticky"> -->
                <CommentComponent :slugg="slugg"  @close="toggleModel" @myComment="publish"/>
          <!-- </div> -->
        </div>



        <hr>


      <div class="comments-CommentComponent-container"> 
        <div class="comment-container">
            <div class="comment-div" v-for="comment in Comments">
              <div class="comment-div-2">
                <img :src="comment.user_photo" class="rounded-avatar">
                <h1 class="title is-4">{{ comment.username }}</h1>
                <h1 class="title is-4">{{ comment.title}}</h1>
                <h1 class="title is-5">{{ comment.comment }}</h1>
                <h1 class="title is-6">{{ comment.date_added }}</h1>
              </div>
            </div>
        </div>

      </div>
    </div>
  </div>


</div>

</template>

<!--  lang="scss" -->
<style lang="scss">

p{
  color:black;
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.55;
  font-size: 18px;
}

.main-container-2{
  width:90%;
  margin: auto;
}

.imagee{
  width:27%;
  // border:solid red;
}

.main-container{
  width:73%;
  // border: solid green;
}

.title-container{
  // display: flex;
  justify-content: space-between;


}

.article-title{
  text-align: center;
  margin: auto;
}
.title{
  // display: flex;
  // justify-content: space-between;


}

.starr{
  color:orange;
}


.grey {
  color:   grey;
}
.comment-div-2{
  margin-bottom: 25px;
}

.comment-container{
  // border: solid;
  margin: auto;
  // width: 75%;
}

.comments-CommentComponent-container{
  // border: solid;
  display: flex;
}

.main-article-container{
  // background-color: #ffffff;
  width: 70%;
  margin:auto;
  // box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
  display: flex;
  justify-content: space-around;
  // border:solid;
}

.Comment-Component{
  width: 90%;
  // border: solid red;
}

.sticky{
  position: sticky;
  top: 20px;

}

.comment-div{
  width: 90%;
  // border: solid red;
  margin: auto;
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;

}

.rounded-avatar {
  object-fit: cover;
  border-radius: 50%;
  height: 100px;
  width: 100px;
}

</style>


<script>
import { createApp } from 'vue'
// import App from './App.vue'

import axios from 'axios'
import CommentComponent from '@/components/CommentComponent.vue'
import RatingStarsSystem from '@/components/RatingStarsSystem.vue'
import ArticleStars from '@/components/ArticleStars.vue'
export default {
  name: 'ArticleView',
  components: {
      CommentComponent,
      RatingStarsSystem,
      ArticleStars,
  },
  data() {
    return {
      Article: [],
      Comments:[],
      name:'a',
      slugg: 'null',
      slug:'aaaa',
      newComment:'s',
      showStarUser:null,
      photo: null,
      x:null,
      articalStarGrade: null,
      datax:'0',
      totalStars:null,
      secondPart:false
      // userID:null
    }
  },

    mounted() {
      this.showArticle()
      // this.showUserStars(this.$cookies.get("userID"),this.$route.params.slug)
      // this.showArticleStars(this.$route.params.slug)
      this.showComments(this.$route.params.slug)
      


    },

    methods: {
      async showArticle(){
        // when is app mounted i can accsess this.$route.params.slug 
        // i am passing slug trough my HomeView..... name: 'article' ,  params: {slug: article.slug}
        const slug = this.$route.params.slug
        const userID = this.$cookies.get("userID")
        this.slugg = slug
          axios.get(`/articles/${slug}/`).then(response => {this.Article = response.data}).catch(error => {console.log(error)})

      },
      // slug = get_comments
      showComments(get_comments){
        axios.get(`/articles/comm/${get_comments}/`).then(response => {this.Comments = response.data}).catch(error => {console.log(error)})
      },

      toggleModel (value) {
        this.name = value
      },
      publish (publishComment) {
        this.newComment = this.Comments.push(publishComment)
      },
      publishStar(value1,value2){
        this.datax = value2
        this.totalStars = value1
      },
      readMoreLess(){
        this.secondPart = !this.secondPart
        this.$refs['buttonReadMore'].innerHTML = 'read less'
        if(this.secondPart == false){
          this.$refs['buttonReadMore'].innerHTML = 'read more'
        }        
      },



    }

}
</script>
