<template>


<div class="stars-container-home-view">

    <div class="book-grade">
		<h1 class="title is-5 " @mouseover="showStarsDatails" @mouseleave="removeStarsDatails">{{bookAvergeRate}} </h1>
	</div>

    <div class="stars-home-view" @mouseover="showStarsDatails" @mouseleave="removeStarsDatails">

            <div class="no-star" v-show="bookAvergeRate  < 1">
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>

            <div class="one-star" v-show="bookAvergeRate == 1 && bookAvergeRate <= 1.2">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>


            <div class="one-half-star" v-show="bookAvergeRate > 1.3 && bookAvergeRate <= 1.7">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star-half-stroke" class="star-orange" size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>


            <div class="two-star" v-show="bookAvergeRate > 1.7 && bookAvergeRate <= 2.2">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>

            <div class="two-half-star" v-show="bookAvergeRate > 2.2 && bookAvergeRate <= 2.7">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star-half-stroke" class="star-orange" size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>    
            </div>

            <div class="three-star" v-show="bookAvergeRate > 2.7 && bookAvergeRate <= 3.2">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>

            <div class="three-half-star" v-show="bookAvergeRate > 3.2 && bookAvergeRate <= 3.7">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star-half-stroke" class="star-orange" size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>
            <div class="four-star" v-show="bookAvergeRate > 3.7 && bookAvergeRate <= 4.2">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>

            <div class="four-half-star" v-show="bookAvergeRate > 4.2 && bookAvergeRate <= 4.7">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star-half-stroke" class="star-orange" size="lg"/> 
            </div>

            <div class="five-star" v-show="bookAvergeRate >  4.7">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>  
            </div>

    </div>
    

</div>

<div class="ratings">
    <h1 class="title is-5 " @mouseover="showStarsDatails" @mouseleave="removeStarsDatails">{{totalReviews}} ratings </h1>
</div>


</template>



<style lang="scss">

.ratings{
	margin-top: 5px;
}

.ratings-grade-paragraf-box-home-view{
    margin-left:2px;
    margin-right:2px;
}

.arrow-down{
    margin-top: 7px;
}

.stars-home-view{
	margin-left: 3px;
}




.each-star-percentage-home-view{
    margin:auto;
    display: flex;
    justify-content: space-between;



}




.star-orange{
    color:orange;
}




.stars-container-home-view{
    
    display: flex;
    // padding-top: 19px;
    // padding-bottom: 5px;
    // width: 100%;
    // border: solid;

}

</style>





<script>
import axios from 'axios'
export default {
    props: ['slug'],
    name: 'ArticleStarsHome',
    data() {
        return {

           showPercentageEachStar:[],
           showStar:false,
           totalReviews:null,
           bookAvergeRate:null, 
        }
    },

    mounted(){
        this.showArticleStarsHomeView(this.slug)
    },

    methods: {

        async showArticleStarsHomeView(slug){
           await axios.get(`/articles/article-stars/${slug}/`)
           .then(response => {
                this.totalReviews = response.data.total[1], 
                this.bookAvergeRate = response.data.total[0].toFixed(1)
                }).catch(error => {console.log(error)})
           
        },

    }



}
</script>