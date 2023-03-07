<template>


<div class="stars-container">

    <div class="aa">

        <div class="box-2 box" v-show="showStar">
            <div class="each-star-percentage">
                <p class="subtitle is-6 ratings-grade-paragraf-box">5 star</p>
                <progress class="progress is-large is-success" v-bind:value="showPercentageEachStar[4]" max="100"></progress>
                <p class="subtitle is-6 ratings-grade-paragraf-box">{{showPercentageEachStar[4]}} %</p>
            </div>
            <div class="each-star-percentage">
                <p class="subtitle is-6 ratings-grade-paragraf-box">4 star</p>
                <progress class="progress is-large is-success" v-bind:value="showPercentageEachStar[3]" max="100"></progress>
                <p class="subtitle is-6 ratings-grade-paragraf-box">{{showPercentageEachStar[3]}} %</p>
            </div>
            <div class="each-star-percentage">
                <p class="subtitle is-6 ratings-grade-paragraf-box">3 star</p>
                <progress class="progress is-large is-success" v-bind:value="showPercentageEachStar[2]" max="100"></progress>
                <p class="subtitle is-6 ratings-grade-paragraf-box">{{showPercentageEachStar[2]}} %</p>
            </div>
            <div class="each-star-percentage">
                <p class="subtitle is-6 ratings-grade-paragraf-box">2 star</p>
                <progress class="progress is-large is-success" v-bind:value="showPercentageEachStar[1]" max="100"></progress>
                <p class="subtitle is-6 ratings-grade-paragraf-box">{{showPercentageEachStar[1]}} %</p>
            </div>
            <div class="each-star-percentage">
                <p class="subtitle is-6 ratings-grade-paragraf-box">1 star</p>
                <progress class="progress is-large is-success" v-bind:value="showPercentageEachStar[0]" max="100"></progress>
                <p class="subtitle is-6 ratings-grade-paragraf-box">{{showPercentageEachStar[0]}} %</p>
            </div>
           

        </div>
    </div>

    <div class="aa" @mouseover="showStarsDatails" @mouseleave="removeStarsDatails">
        <h1 class="title is-5 show-article-avarge-stars ratings-grade-paragraf">{{showArticleAvargeStars}}</h1>
    </div>

    <div class="zz" @mouseover="showStarsDatails" @mouseleave="removeStarsDatails">

            <div class="one-star" v-show="showArticleAvargeStars <= 1.2">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>


            <div class="one-half-star" v-show="showArticleAvargeStars > 1.3 && showArticleAvargeStars <= 1.7">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star-half-stroke" class="star-orange" size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>


            <div class="two-star" v-show="showArticleAvargeStars > 1.7 && showArticleAvargeStars <= 2.2">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>

            <div class="two-half-star" v-show="showArticleAvargeStars > 2.2 && showArticleAvargeStars <= 2.7">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star-half-stroke" class="star-orange" size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>    
            </div>

            <div class="three-star" v-show="showArticleAvargeStars > 2.7 && showArticleAvargeStars <= 3.2">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>

            <div class="three-half-star" v-show="showArticleAvargeStars > 3.2 && showArticleAvargeStars <= 3.7">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star-half-stroke" class="star-orange" size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>
            <div class="four-star" v-show="showArticleAvargeStars  > 3.7 && showArticleAvargeStars <= 4.2">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>

            <div class="four-half-star" v-show="showArticleAvargeStars > 4.2 && showArticleAvargeStars <= 4.7">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star-half-stroke" class="star-orange" size="lg"/> 
            </div>

            <div class="five-star" v-show="showArticleAvargeStars > 4.7">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>  
            </div>


    </div>

    <font-awesome-icon icon="fa-solid fa-arrow-down" @mouseover="showStarsDatails" @mouseleave="removeStarsDatails" size="lg" class="arrow-down" bounce/>

    <h1 class="title is-6 ratings-grade-paragraf-2" @mouseover="showStarsDatails" @mouseleave="removeStarsDatails">{{showArticleTotalStars}} ratings </h1>

    <h1 class="title is-6 ratings-grade-paragraf-2" @mouseover="showStarsDatails" @mouseleave="removeStarsDatails">{{numOfComments}} reviews </h1>








</div>


</template>



<style lang="scss">

.content h1:not(:first-child) {
    // margin-top: 0em;
}

.ratings-grade-paragraf-box{
    margin-left:2px;
    margin-right:2px;
}

.arrow-down{
    margin-top: 7px;
}


.ratings-grade-paragraf{
    // margin-top: 5px;
    // margin-top: 0em;
        // margin-top: 10px;
    // text-align: center;
}

.ratings-grade-paragraf-2{
    margin-top: 3px;
    // margin-top: -17px;
    margin-left: 1em;
    // border: solid;
    
}

.each-star-percentage{
    margin:auto;
    display: flex;
    justify-content: space-between;



}

.box-2{
    position: absolute;
    // position: fixed;
    margin-top: 40px;
    border: solid green;
    // width: 350px;
    // z-index: 2;

}

.progress{
    width: 170px;
    // margin-top: 2px;
    // border:solid;
}

.zz{
    margin-right: 5px;
    margin-left: 5px;
  // background-color: #ffffff;
  // width: 80%;
  // margin: 0px;
  // box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
  // border: solid;
}
.aa{
    // border:solid;
    margin-left:5px;

}
.star-orange{
    color:orange;
}

.subtitle{
    color: #0066ff;
    // border:solid;

}

.show-article-avarge-stars{
    color: #0066ff;
    // margin-top: 10px;
    // margin-left: 5px;
    // border: solid;
}

.stars-container{
    
    display: flex;
    padding-top: 10px;
    padding-bottom: 2px;
    // align-items: center;
    // border: solid;

}

.stars-container:hover{
    
    background-color: #f2f2f2;
    transition-delay:0.1s;

}

</style>





<script>
import axios from 'axios'
export default {
    props: ['datax','totalStars','numOfComments'],
    name: 'ArticleStars',
    data() {
        return {
           showArticleAvargeStars:null,
           showArticleTotalStars:null,
           showPercentageEachStar:[],
           showStar:false,
        }
    },
    mounted(){
        this.showArticleStars(this.$route.params.slug)
    },

    updated(){
        if(!(this.datax == 0) )
            this.showArticleAvargeStars = this.datax
        if(this.totalStars){
            this.showArticleTotalStars = this.totalStars
        }
    },

    methods: {

        async showArticleStars(slug){
           await axios.get(`/articles/article-stars/${slug}/`)
           .then(response => {
                this.showPercentageEachStar = response.data.each_star_procentage,
                this.showArticleAvargeStars = response.data.total[0],
                this.showArticleTotalStars = response.data.total[1]}).catch(error => {console.log(error)})
           
        },


        showStarsDatails(){
            this.showStar = true
        },
        removeStarsDatails(){
            this.showStar = false
        }

    }



}
</script>