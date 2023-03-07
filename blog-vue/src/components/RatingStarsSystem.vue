<template>

<div v-show="isVisible" class="notification is-primary is-light">
    <h3 class="title is-3">Please login first</h3>
</div>

<div class="rate-artical">
    <h4>rate this article</h4>
    <font-awesome-icon icon="fa-solid fa-star" ref="one"   @mouseover="mouseOverOneStar"   @mouseleave="removeStarsColor" @click="submitNum_1" size="lg"/>
    <font-awesome-icon icon="fa-solid fa-star" ref="two"   @mouseover="mouseOverTwoStar"   @mouseleave="removeStarsColor" @click="submitNum_2" size="lg"/>
    <font-awesome-icon icon="fa-solid fa-star" ref="three" @mouseover="mouseOverThreeStar" @mouseleave="removeStarsColor" @click="submitNum_3" size="lg"/>
    <font-awesome-icon icon="fa-solid fa-star" ref="four"  @mouseover="mouseOverFourStar"  @mouseleave="removeStarsColor" @click="submitNum_4" size="lg"/>
    <font-awesome-icon icon="fa-solid fa-star" ref="five"  @mouseover="mouseOverFiveStar"  @mouseleave="removeStarsColor" @click="submitNum_5" size="lg"/> 
</div>


<div><h1 class="title is-3">user star grade  : {{showUsersStars}}</h1></div>


<!-- <ArticleStars :articalStarGrade="showArticleAvargeStars"/> -->



</template>



<style lang="scss">

.rate-artical{
    display: flex;
}

.star-orange{
    color:orange;
}

</style>





<script>
import axios from 'axios'
import ArticleStars from '@/components/ArticleStars.vue'
export default {
    props: ['slug','showStarUser'], // 'articalStarGrade'
    emits: ["starsGrade"],
    name: 'RatingStarsSystem',
      components: {
          // CommentComponent,
          // RatingStarsSystem,
          // ArticleStars,
      },
    data() {
        return {
           userID:'',
           showStars:[],
           showUsersStars:null,
           showArticleTotalStars:null,
           showArticleAvargeStars:null,
           user:null,
           isVisible:false,
        }
    },
    updated(){
       this.showUserStarsx(this.$cookies.get("userID"),this.slug) 
    },
    mounted(){
        
        this.showUserStarsx(this.$cookies.get("userID"),this.$route.params.slug)
    },

    methods: {
        showMessagex(){
            this.isVisible = true
            // after 5 sec this.isVisible will be set to false 
            setTimeout(() => this.isVisible = false, 5000);
        },
        submitNum_1() {
            if(this.$cookies.get("userID")){
                const data = new FormData()
                const value = '1'
                data.append('num', value)
                data.append('slug', this.slug)
                data.append('userID', this.userID = this.$cookies.get("userID"))
                this.userID = this.$cookies.get("userID")
                axios.post("articles/star/",data).then(response =>{this.dataStars(response.data.total_stars,response.data.star_grade,this.showUserStarsx(this.userID,this.$route.params.slug))}).catch(error => {console.log(error)})

            }
            else{
                this.showMessagex()
            }

        },
        submitNum_2() {
            if(this.$cookies.get("userID")){
                const data = new FormData()
                const value = '2'
                data.append('num', value)
                data.append('slug', this.slug)
                data.append('userID', this.userID = this.$cookies.get("userID"))
                this.userID = this.$cookies.get("userID")
                axios.post("articles/star/",data).then(response =>{this.dataStars(response.data.total_stars,response.data.star_grade,this.showUserStarsx(this.userID,this.$route.params.slug))}).catch(error => {console.log(error)})

            }
            else{
                this.showMessagex()
            }
        },
        submitNum_3() {
            if(this.$cookies.get("userID")){
                const data = new FormData()
                const value = '3'
                data.append('num', value)
                data.append('slug', this.slug)
                data.append('userID', this.userID = this.$cookies.get("userID"))
                this.userID = this.$cookies.get("userID")
                axios.post("articles/star/",data).then(response =>{this.dataStars(response.data.total_stars,response.data.star_grade,this.showUserStarsx(this.userID,this.$route.params.slug))}).catch(error => {console.log(error)})

            }
            else{
                this.showMessagex()
            }
        },
        submitNum_4() {
            if(this.$cookies.get("userID")){
                const data = new FormData()
                const value = '4'
                data.append('num', value)
                data.append('slug', this.slug)
                data.append('userID', this.userID = this.$cookies.get("userID"))
                this.userID = this.$cookies.get("userID")
                axios.post("articles/star/",data).then(response =>{this.dataStars(response.data.total_stars,response.data.star_grade,this.showUserStarsx(this.userID,this.$route.params.slug))}).catch(error => {console.log(error)})

            }
            else{
                this.showMessagex()
            }
        },
        submitNum_5() {
            if(this.$cookies.get("userID")){
                const data = new FormData()
                const value = '5'
                data.append('num', value)
                data.append('slug', this.slug)
                data.append('userID', this.userID = this.$cookies.get("userID"))
                this.userID = this.$cookies.get("userID")
                axios.post("articles/star/",data).then(response =>{this.dataStars(response.data.total_stars,response.data.star_grade,this.showUserStarsx(this.userID,this.$route.params.slug))}).catch(error => {console.log(error)})

            }
            else{
                this.showMessagex()
            }
        },
        mouseOverOneStar(){
              this.$refs['one'].$el.classList.add('starr')
        },
        mouseOverTwoStar(){
              this.$refs['one'].$el.classList.add('starr')
              this.$refs['two'].$el.classList.add('starr')
        },
        mouseOverThreeStar(){
              this.$refs['one'].$el.classList.add('starr')
              this.$refs['two'].$el.classList.add('starr')
              this.$refs['three'].$el.classList.add('starr')
        },
        mouseOverFourStar(){
              this.$refs['one'].$el.classList.add('starr')
              this.$refs['two'].$el.classList.add('starr')
              this.$refs['three'].$el.classList.add('starr')
              this.$refs['four'].$el.classList.add('starr')
        },
        mouseOverFiveStar(){
              this.$refs['one'].$el.classList.add('starr')
              this.$refs['two'].$el.classList.add('starr')
              this.$refs['three'].$el.classList.add('starr')
              this.$refs['four'].$el.classList.add('starr')
              this.$refs['five'].$el.classList.add('starr')

        },
        removeStarsColor(){
              this.$refs['one'].$el.classList.remove('starr')
              this.$refs['two'].$el.classList.remove('starr')
              this.$refs['three'].$el.classList.remove('starr')
              this.$refs['four'].$el.classList.remove('starr')
              this.$refs['five'].$el.classList.remove('starr')
        },
        showUserStarsx(userID,get_slug){
            console.log('000000000000')
            if(userID){
                axios.get(`/articles/user-stars/${userID}/${get_slug}/`).then(response => {
                    if(response.data == 'not rated'){
                        this.showUsersStars = 'no stars given'
                    }else{
                       this.showUsersStars = response.data[0].stars 
                    }
                }).catch(error => {console.log(error)})
            }

        },

       dataStars(value1,value2){
            this.$emit('starsGrade', value1,value2)
        },

    }

}
</script>