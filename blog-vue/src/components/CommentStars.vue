<template>


<div class="stars-comment-container">



    <div class="zzz">

            <div class="one-star" v-show="s == 1">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>


            <div class="two-star" v-show="s == 2">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>



            <div class="three-star" v-show="s == 3">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>


            <div class="four-star" v-show="s == 4">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star"   size="lg"/>  
            </div>



            <div class="five-star" v-show="s == 5">
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>
                <font-awesome-icon icon="fa-solid fa-star" class="star-orange"  size="lg"/>  
            </div>


    </div>



</div>


</template>



<style lang="scss">


.star-orange{
    color:orange;
}


.stars-comment-container{
    
    display: flex;
    // justify-content: center;
    // background-color: #f2f2f2;
    max-width: 120px;
    width: 100%;

}

</style>





<script>
export default {
    props: ['s'],
    name: 'CommentStars',


}
</script>