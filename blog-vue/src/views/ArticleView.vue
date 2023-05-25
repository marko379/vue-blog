<template>

<div class="main-article-container">
  <div class="imagee-2">
    <div class="imagee">
      <div class="pic">
        <img :src="Article.image_path">
      </div>
      <!-- @starsGrade="publishStar" recive emit method will activate/run publishStar method from  RatingStarsSystem component-->
      <!--  :slug="slugg" send slug as props -->
      <div class="zzz">
        <RatingStarsSystem   :slug="Article.slug" :title="Article.name" :bookPhoto="Article.image_path" :price="Article.price" @updateStarsOnComment="updateStarsComment" @modalOpen="showModal"/>
        <Basket :slug="Article.slug" :bookName="Article.name" :bookPhoto="Article.image_path" :bookPrice="Article.price"/>
      </div>
    </div>
  </div>


  <div class="main-container">

    <div class="main-container-2">
        <div class="article-title">
          <h1 class="title is-2 is-italic abc">{{Article.name}}</h1>
          <h1 class="title is-1 is-italic">{{Article.price}}</h1>
        </div>
        <h1 class="title is-4 ">Aldous Huxley</h1>
        <div class="vjezba">
          <ArticleStars :slug="$route.params.slug" :datax="datax" :totalStars="totalStars" :numOfComments="Comments.length"/>
        </div>

        <div class="genre">
          <h1 class="title is-6">Genres: </h1>
          <div v-for="category in Article.categories">
            <h1 class="title is-6 is-italic genre-category"> {{category}} , </h1>
          </div>
        </div>


        <div class="modal" ref="modal">
          <div class="modal-background"></div>
          <div class="modal-card">
            <header class="modal-card-head is-flex is-justify-content-space-between">
              <div><p class="modal-card-title">you are buying 1 book</p></div> 
              <div><p class="modal-card-title has-text-dark has-text-weight-bold">total: £{{Article.price}}</p></div> 
            </header>
            <section class="modal-card-body">
              <div class="is-flex">
                <img :src="Article.image_path" width="80">
                <h1 class="title is-5 is-italic ml-3">{{Article.name}}</h1>
              </div>
              
            </section>
            <footer class="modal-card-foot">
              <button class="button is-success">Confirm</button>
              <button class="button is-danger is-outlined" @click="removeModal">Cancel</button>
            </footer>
          </div>
        </div>



        <p>
          {{Article.description_1st_part}}
          <span @click="readMore" ref="readMoreLink" class="readxxx is-underlined">... read more</span>
          <span v-show="secondPart">{{Article.description_2nd_part}}
            <span @click="readLess" ref="readLessLink" class="readxxx is-underlined">... read less</span>
          </span>
        </p>

        <hr>
        <!-- @carouselBook="callback" -->
        <Carousel :genres="Article.categories" />  

        <h3 class="title is-3">Ratings & Reviews</h3>


        <hr>

        <div class="Comment-Component">
          <!-- remember u are passing props from here to CommentComponent (child component) -->
          <!-- remember u are triggering also emit over here  @myComment="publish" -->
                <CommentComponent :slugg="Article.slug"  @close="toggleModel" @myComment="publish"/>
        </div>

        <hr>

        <div class="comment-container">
          <div class="comment-div" v-for="(comment,index) in Comments" :key="comment.id">

            <div class="comment-first-container">
              <div>
                <img :src="comment.user_photo" class="rounded-avatar">
                <h1 class="title is-4">{{ comment.username }}</h1>                
              </div>
              <CommentStars class="comment-stars" v-show="comment.user_stars != 0" :s="comment.user_stars"/>

              <h1 class="title is-6">{{ comment.datepublished }}</h1>
            </div>

            <div class="comment-content">
              <h1 class="title is-5">{{ comment.title}}</h1>              
              <h1 class="subtitle is-5 comment-description">
                <span :ref="`readLessCommentRef${comment.id}`" style="white-space: pre-line">{{comment.comment_1st_part }}</span>
                <span :ref="`readMoreCommentRef${comment.id}`" class="aaa" style="white-space: pre-line">{{comment.comment_2nd_part }}</span>
              <button class="button is-ghost" @click="readMoreComment(comment.id)" :ref="`readMoreCommentSpanRef${comment.id}`">read more</button>
              <button class="button is-ghost aaa" @click="readLessComment(comment.id)" :ref="`readLessCommentSpanRef${comment.id}`">... read less</button>
              </h1>
            </div>

            <div class="thumbs-and-delete">
              <div class="thumbs">
                <h1 class="title is-4" :ref="`comment_likes_count${comment.id}`">{{comment.user_like_comment_count}}</h1>
                <div :ref="`thumbs_up_solid${comment.id}`" class="aaa">
                  <div class="tooltip">
                    <font-awesome-icon icon="fa-solid fa-thumbs-up"  @click="removeOneLike(comment.id,comment.user_like_comment_count); submitCommentLikeDislike(comment.username,Article.slug,comment.id,'like'); submit2(comment.id,'thumbs_up_solid');" size="2x"/>
                    <span class="tooltiptext">Take it back</span>
                  </div>
                </div>

                <div :ref="`thumbs_up_regular${comment.id}`" class="">
                  <div class="tooltip">
                    <font-awesome-icon icon="fa-regular fa-thumbs-up" class="tooltip" @click=" addOneLike(comment.id,comment.user_like_comment_count); submitCommentLikeDislike(comment.username,Article.slug,comment.id,'like'); submit2(comment.id,'thumbs_up_regular');" size="2x"/>
                  <span class="tooltiptext">I like it</span>
                  </div>
                </div>

                <div :ref="`thumbs_down_solid${comment.id}`" class="aaa">
                  <div class="tooltip">
                    <font-awesome-icon icon="fa-solid fa-thumbs-down" class="tooltip"  @click="removeOneDislike(comment.id,comment.user_dislike_comment_count); submitCommentLikeDislike(comment.username,Article.slug,comment.id,'dislike'); submit2(comment.id,'thumbs_down_solid');" size="2x"/>
                  <span class="tooltiptext">Take it back</span>
                  </div>  
                </div>

                <div :ref="`thumbs_down_regular${comment.id}`" class="">
                  <div class="tooltip">
                    <font-awesome-icon icon="fa-regular fa-thumbs-down" class="tooltip"  @click="addOneDislike(comment.id,comment.user_dislike_comment_count); submitCommentLikeDislike(comment.username,Article.slug,comment.id,'dislike'); submit2(comment.id,'thumbs_down_regular');" size="2x"/>
                  <span class="tooltiptext">I don't like it</span>
                  </div>
                </div>
                <h1 class="title is-4" :ref="`comment_dislikes_count${comment.id}`">{{comment.user_dislike_comment_count}}</h1>
              </div>
              <button class="button is-danger is-outlined" v-show="$store.state.userId == comment.userID && $store.state.userId != null" @click="deleteComment(index,comment.username,Article.slug,comment.id)">Delete</button>
            </div>
            <span>{{checkIfUserLikeComment(comment.user_like_comment,$store.state.userId,comment.id)}}</span>
            <span>{{checkIfUserDislikeComment(comment.user_dislike_comment,$store.state.userId,comment.id)}}</span>

            <hr>
          </div>
        </div>


    </div>
  </div>

</div>

</template>

<style lang="scss">

@import '@/assets/css/ArticleViewCss.css';


</style>


<script>
import { createApp } from 'vue'
import axios from 'axios'
import CommentComponent from '@/components/CommentComponent.vue'
import Basket from '@/components/Basket.vue'
import Carousel from '@/components/Carousel.vue'
import RatingStarsSystem from '@/components/RatingStarsSystem.vue'
import ArticleStars from '@/components/ArticleStars.vue'
import CommentStars from '@/components/CommentStars.vue'

export default {
  name: 'ArticleView',
  components: {
      Basket,
      RatingStarsSystem,
      ArticleStars,
      Carousel,
      CommentComponent,
      CommentStars
  },
  data() {
    return {
      Article: [],
      soldBooks:[],
      Comments:[],
      showStarUser:null,
      photo: null,
      articalStarGrade: null,
      datax:null,
      totalStars:null,
      secondPart:false,
      userLikeComment:'',
      userDislikeComment:null,
      comment_id: null,
      isActive:false,

    }
  },

  mounted() {
    this.showArticle()
    this.showComments(this.$route.params.slug)
  
  },
  methods: {
    async showArticle(){
      // when is app mounted i can accsess this.$route.params.slug 
      // i am passing slug trough my HomeView..... name: 'article' ,  params: {slug: article.slug}
      const userID = this.$cookies.get("userID")
        axios.get(`/articles/${this.$route.params.slug}/`).then(response => {this.Article = response.data}).catch(error => {console.log(error)})

    },
    // slug = get_comments
    showComments(get_comments){
      axios.get(`/articles/comm/${get_comments}/`).then(response => {this.Comments = response.data}).catch(error => {console.log(error)})
    },

    toggleModel (value) {
      this.name = value
    },

    publish (publishComment) {
      this.Comments.push(publishComment)
    },

    updateStarsComment(){
      this.showComments(this.$route.params.slug)
    },
    readMore(){
      this.secondPart = !this.secondPart
      this.$refs['readMoreLink'].innerHTML = ""
      this.$refs['readLessLink'].innerHTML = " read less"     
    },
    readLess(){
      this.secondPart = !this.secondPart
      this.$refs['readMoreLink'].innerHTML = "... read more"
      this.$refs['readLessLink'].innerHTML = ""
    },
    readMoreComment(comm_id){
      let comm_ref_read_more_span = this.$refs['readMoreCommentSpanRef'+ comm_id.toString()][0]
      // comm_ref_read_more_span.innerHTML = ''
      comm_ref_read_more_span.classList.add('aaa')

      let comm_ref_read_less_span = this.$refs['readLessCommentSpanRef'+ comm_id.toString()][0]
      comm_ref_read_less_span.classList.remove('aaa')
      // comm_ref_read_less_span.innerHTML = '... read less'

      let comm_ref = this.$refs['readMoreCommentRef'+ comm_id.toString()][0]
      comm_ref.classList.remove('aaa')

    },
    readLessComment(comm_id){
      let comm_ref_read_less_span = this.$refs['readLessCommentSpanRef'+ comm_id.toString()][0]
      // comm_ref_read_less_span.innerHTML = ''
      comm_ref_read_less_span.classList.add('aaa')

      let comm_ref_read_more_span = this.$refs['readMoreCommentSpanRef'+ comm_id.toString()][0]
      comm_ref_read_more_span.classList.remove('aaa')
      // comm_ref_read_more_span.innerHTML = '... read more'


      let comm_ref = this.$refs['readMoreCommentRef'+ comm_id.toString()][0]
      comm_ref.classList.add('aaa')
    },

    addOneLike(comm_id,like_comment_count){
      let add_like = parseInt(this.$refs['comment_likes_count' + comm_id.toString()][0].innerHTML) + 1
      this.$refs['comment_likes_count' + comm_id.toString()][0].innerHTML = add_like      
      if(this.$refs['thumbs_down_solid' + comm_id.toString()][0].classList.contains('red')){
        this.removeOneDislike(comm_id,like_comment_count)
      }

    },
    removeOneLike(comm_id,like_comment_count){
      let removeLike =  parseInt(this.$refs['comment_likes_count' + comm_id.toString()][0].innerHTML) - 1
      this.$refs['comment_likes_count' + comm_id.toString()][0].innerHTML = removeLike
    },
    addOneDislike(comm_id,like_comment_count){
      let addDislike =  parseInt(this.$refs['comment_dislikes_count' + comm_id.toString()][0].innerHTML) + 1
      this.$refs['comment_dislikes_count' + comm_id.toString()][0].innerHTML = addDislike
      if(this.$refs['thumbs_up_solid' + comm_id.toString()][0].classList.contains('green')){
        this.removeOneLike(comm_id,like_comment_count)
      }
    },
    removeOneDislike(comm_id,like_comment_count){
      let removeDislike =  parseInt(this.$refs['comment_dislikes_count' + comm_id.toString()][0].innerHTML) - 1
      this.$refs['comment_dislikes_count' + comm_id.toString()][0].innerHTML = removeDislike
    },


    submitCommentLikeDislike(username,slug,comment_id,like_dislike){
      if(this.$cookies.get("userID")){
        const data = new FormData()
        data.append('user_id', this.$cookies.get("userID"))
        data.append('slug', slug)
        data.append('like_dislike', like_dislike)
        data.append('comment_id', comment_id)
        axios.post("articles/like-dislike-comment/",data).
        then(response =>{this.comment_id =  response.data.comment_id,this.userLikeComment = response.data.user_like_comment,
                this.userDislikeComment = response.data.user_dislike_comment,console.log(response .data)}).catch(error => {console.log(error)})
      }
      else{
        this.$store.commit('showMsg','Please login first')
      }
    },

    checkIfUserLikeComment(user_list,user_id,comm_id){
      if(user_id){
        if (user_list.includes(parseInt(user_id))){
          setTimeout(() => {
              this.$refs['thumbs_up_solid' + comm_id.toString()][0].classList.add('green')
              this.$refs['thumbs_up_solid' + comm_id.toString()][0].classList.remove('aaa')
              this.$refs['thumbs_up_regular' + comm_id.toString()][0].classList.add('aaa')
          }, 800);
        }
      }
    },

    checkIfUserDislikeComment(user_list,user_id,comm_id){
      if(user_id){
        if (user_list.includes(parseInt(user_id))){
          setTimeout(() => {
            this.$refs['thumbs_down_regular' + comm_id.toString()][0].classList.add('aaa')
            this.$refs['thumbs_down_solid' + comm_id.toString()][0].classList.add('red')
            this.$refs['thumbs_down_solid' + comm_id.toString()][0].classList.remove('aaa')
          }, 800);
        }
      }
    },

    submit2(comm_id,t){
      let q = this.$refs[t + comm_id.toString()]

      if(t == 'thumbs_up_regular'){
        if (q[0].classList.length == 0){
            this.$refs['thumbs_up_solid' + comm_id.toString()][0].classList.remove('aaa')
            this.$refs['thumbs_up_solid' + comm_id.toString()][0].classList.add('green')
            this.$refs['thumbs_up_regular' + comm_id.toString()][0].classList.add('aaa')

            this.$refs['thumbs_down_solid' + comm_id.toString()][0].classList.remove('red')
            this.$refs['thumbs_down_solid' + comm_id.toString()][0].classList.add('aaa')

            this.$refs['thumbs_down_regular' + comm_id.toString()][0].classList.remove('aaa')
        }
      }
      else if (t == 'thumbs_up_solid'){
        if (q[0].classList.length > 0){
            this.$refs['thumbs_up_solid' + comm_id.toString()][0].classList.remove('green')
            this.$refs['thumbs_up_solid' + comm_id.toString()][0].classList.add('aaa')
            this.$refs['thumbs_up_regular' + comm_id.toString()][0].classList.remove('aaa')

            this.$refs['thumbs_down_solid' + comm_id.toString()][0].classList.add('aaa')
            this.$refs['thumbs_down_solid' + comm_id.toString()][0].classList.remove('red')
        }   
      }
      else if (t == 'thumbs_down_regular'){
        if (q[0].classList.length == 0){
            this.$refs['thumbs_down_solid' + comm_id.toString()][0].classList.remove('aaa')
            this.$refs['thumbs_down_solid' + comm_id.toString()][0].classList.add('red')
            this.$refs['thumbs_down_regular' + comm_id.toString()][0].classList.add('aaa')

            this.$refs['thumbs_up_solid' + comm_id.toString()][0].classList.remove('green')
            this.$refs['thumbs_up_solid' + comm_id.toString()][0].classList.add('aaa')

            this.$refs['thumbs_up_regular' + comm_id.toString()][0].classList.remove('aaa')
        }  
      }
      else if (t == 'thumbs_down_solid'){
        if (q[0].classList.length > 0){
            this.$refs['thumbs_down_solid' + comm_id.toString()][0].classList.remove('red')
            this.$refs['thumbs_down_solid' + comm_id.toString()][0].classList.add('aaa')
            this.$refs['thumbs_down_regular' + comm_id.toString()][0].classList.remove('aaa')

            this.$refs['thumbs_up_solid' + comm_id.toString()][0].classList.add('aaa')
            this.$refs['thumbs_up_solid' + comm_id.toString()][0].classList.remove('green')
        }  
      }
    },

    deleteComment(index,username,slug,comment_id){
      if(this.$store.state.userId){
        this.Comments.splice(index, 1); 
        const data = new FormData()
        data.append('user_id', this.$cookies.get("userID"))
        data.append('slug', slug)
        data.append('comment_id', comment_id)
        axios.post("articles/delete-comment/",data).
        then(response =>{console.log('succsess')}).catch(error => {console.log(error)})
      }
    },
    showModal(){
      this.$refs.modal.classList.add('is-active')
    },
    removeModal(){
      this.$refs.modal.classList.remove('is-active')
    }

  }


}
</script>
