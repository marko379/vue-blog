<template>

<div class="my-div"  @mouseover="mouseAddColor" ref="divv"  @mouseleave="mouseRemoveColor">
    hdhdhddh
</div>

</template>


<style lang="scss">

.my-div{
    height: 100px;
    border: solid;
}

// .my-div:hover {
//   background-color: yellow;
// }

.red{
    background-color: red;
}

</style>




<script>
export default {

    mounted(){
        this.isTouchDevice()
    },


    methods: {
        isTouchDevice(){
            if('ontouchstart' in window){
                console.log('oooooooooooo')
            }
        },

        mouseAddColor(){
              this.$refs['divv'].classList.add('red')
        },


    }


}
</script>
