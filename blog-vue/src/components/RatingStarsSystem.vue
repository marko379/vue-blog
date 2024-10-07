<template>

<div>
    <!-- you implemented mouseover and mouseleave  -->
    <div class="rate-artical">
        <font-awesome-icon icon="fa-solid fa-star" ref="one"   @mouseover="mouseOverOneStar"   @mouseleave="removeStarsColor" @click="submitNum_1" size="2x"/>
        <font-awesome-icon icon="fa-solid fa-star" ref="two"   @mouseover="mouseOverTwoStar"   @mouseleave="removeStarsColor" @click="submitNum_2" size="2x"/>
        <font-awesome-icon icon="fa-solid fa-star" ref="three" @mouseover="mouseOverThreeStar" @mouseleave="removeStarsColor" @click="submitNum_3" size="2x"/>
        <font-awesome-icon icon="fa-solid fa-star" ref="four"  @mouseover="mouseOverFourStar"  @mouseleave="removeStarsColor" @click="submitNum_4" size="2x"/>
        <font-awesome-icon icon="fa-solid fa-star" ref="five"  @mouseover="mouseOverFiveStar"  @mouseleave="removeStarsColor" @click="submitNum_5" size="2x"/>
    </div>

    <div class="as">
        <h4 class="subtitle is-4">rate this book</h4>
    </div> 

    <!-- <button class="button is-medium is-fullwidth is-success is-rounded button-buy-this-book" @click="openModal">buy this book</button>  -->

</div>

</template>



<style lang="scss">

.your-rate-star{
    margin: 3px;
    color: orange;
}

.button-buy-this-book{
    margin-top: 15px;
}

.button-add-to-basket{
    margin-top: 15px;
}

.as{
    margin: 15px auto auto auto;
    // max-width: 137px;
    text-align: center;
    width: 100%;
    letter-spacing: 2px;
    // border: solid;
}

.rate-artical{
    display: flex;
    width: 100%;
    justify-content: space-between;
}

.star-orange{
    color:orange;
}



@media only screen and (max-width: 900px) {

}

</style>





<script>
import axios from 'axios'
import ArticleStars from '@/components/ArticleStars.vue'
export default {
    props: ['slug','price','title','bookPhoto'], // 'articalStarGrade', ,'showStarUser'
    emits: ["starsGrade","updateStarsOnComment",'modalOpen'],
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
           soldBooks:[]
        }
    },

    mounted(){
        // this method returns user's grade (if user rated book with grade 4 then num 4 will returned ),method is bellow 
        this.showUserStars(this.$cookies.get("userID"),this.$route.params.slug)
    },

    methods: {
        showMessagex(){
            this.$store.commit('showMsg','please login first')
        },
        // when you click on star 1 icon this method will activate
        // first will check if there is userID in cookies, coz only logged in user can rate a book
        // if user is logged in then data(num,slug,userID) will be send(posted) to  "articles/star/"
        // if conection was succsesful server(django-model/sql-table) will be updated with data and saved, also data(response) from server will be returned to here
        // from server it will be returned total_stars(total number of all users that rated article) and star_grade(avrage grade for this article)
        // then you will run new method dataStars with response and data(check down bellow method)

        // if userID not available all above will be skipped and metgod showMessagex() will be run, that means msg will pop up on screen saying something like please log in if u want to rate this book 
        submitNum_1() {
            if(this.$cookies.get("userID")){
                const data = new FormData()
                const value = '1'
                data.append('num', value)
                data.append('slug', this.slug)
                data.append('userID', this.userID = this.$cookies.get("userID"))
                this.userID = this.$cookies.get("userID")
                axios.post("articles/star/",data).then(response =>{
                    this.articalGradeToDecimalNum(response.data.star_grade),
                    this.updateCommentStars(), 
                    this.showRateMsg(response.data.user_grade),
                    this.$store.state.showArticleTotalStars = response.data.total_stars,
                    this.showUserStars(this.userID,this.$route.params.slug)})
                .catch(error => {console.log(error)})

            }
            else{
                console.log(this.$refs['one'].$el)
                // this.$refs['one'].$el.classList.remove('starr')
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
                axios.post("articles/star/",data).then(response =>{
                    this.articalGradeToDecimalNum(response.data.star_grade),
                    this.updateCommentStars(),
                    this.showRateMsg(response.data.user_grade), 
                    this.$store.state.showArticleTotalStars = response.data.total_stars,
                    this.showUserStars(this.userID,this.$route.params.slug)})
                .catch(error => {console.log(error)})

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
                axios.post("articles/star/",data).then(response =>{
                    console.log(response.data)
                    this.articalGradeToDecimalNum(response.data.star_grade),
                    this.updateCommentStars(),
                    this.showRateMsg(response.data.user_grade), 
                    this.$store.state.showArticleTotalStars = response.data.total_stars,
                    this.showUserStars(this.userID,this.$route.params.slug)})
                .catch(error => {console.log(error)})

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
                axios.post("articles/star/",data).then(response =>{
                    console.log(response.data)
                    this.articalGradeToDecimalNum(response.data.star_grade),
                    this.updateCommentStars(),
                    this.showRateMsg(response.data.user_grade), 
                    this.$store.state.showArticleTotalStars = response.data.total_stars,
                    this.showUserStars(this.userID,this.$route.params.slug)})
                .catch(error => {console.log(error)})

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
                axios.post("articles/star/",data).then(response =>{
                    console.log(response.data)
                    this.articalGradeToDecimalNum(response.data.star_grade),
                    this.updateCommentStars(),
                    this.showRateMsg(response.data.user_grade), 
                    this.$store.state.showArticleTotalStars = response.data.total_stars,
                    this.showUserStars(this.userID,this.$route.params.slug)})
                .catch(error => {console.log(error)})

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
        // this method is run by  mounted and updated and submitNum_ method
        // returns user's grade given for particular book
        // simple method to show what grade user has given to a book
        showUserStars(userID,get_slug){
            if(userID){
                axios.get(`/articles/user-stars/${userID}/${get_slug}/`).then(response => {
                    if(response.data == 'not rated'){
                        this.$store.state.userStars = 'no stars given'
                        this.$store.state.userStarsOnComment = 0
                    }else{
                       this.$store.state.userStars = response.data[0].stars
                       this.$store.state.userStarsOnComment = response.data[0].stars
                    }
                }).catch(error => {console.log(error)})
            }

        },
        articalGradeToDecimalNum(grade){
            this.$store.state.bookAvergeRating = grade.toFixed(1)
        },
        updateCommentStars(){
            this.$emit('updateStarsOnComment')
        },

        openModal(){
            this.$emit('modalOpen')   
        },

        showRateMsg(value){
            if(value == 'not exists'){
                this.$store.commit('showMsg','book unrated')
            }
            if(value === 1){
                this.$store.commit('showMsg','your rating: ' + value + ' star')
            }
            if(value > 1){
                this.$store.commit('showMsg','your rating: ' + value + ' star')
            }
        },



    }

}
</script>