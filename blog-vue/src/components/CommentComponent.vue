<template>

    <div v-show="isVisible" class="notification is-primary is-light show-comment-succses-msg">
        <button @click="deleteMessageComment" class="delete"></button>
        <h3 class="title is-3">Comment published succesfully</h3>
    </div>

    <div class="comment-form">
        <form @submit.prevent="submitCommentForm" class="box">
            <div class="field title-field">
                <div class="control">
                    <input type="text" class="input" name="title" v-model="title" placeholder="Title of comment">
                </div>
            </div>

            <div class="field comment-field">
                <div class="control">
                    <textarea class="textarea is-primary" placeholder="Comment" name="comment" v-model="comment"></textarea>
                    <!-- <input type="text" class="input" name="comment" v-model="comment" placeholder="comment"> -->
                </div>
            </div>



            <br>

            <div class="field">
                <div class="control button-field">
                    <button class="button is-success is-fullwidth">Publish</button>
                </div>
            </div>
        </form>
    </div>
    <br>


</template>



<style lang="scss">

.strong-text{
    text-align: center;
}

.show-comment-succses-msg {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 50%;
    height: 15%;
    border: solid;
    opacity: 0.97;
    text-align: center;
}


.comment-form{
    width: 90%;
    margin: auto;
    // border: solid green;
}


</style>





<script>
import axios from 'axios'

export default {
    props: ['slugg'],
    emits: ["close","myComment"],
    name: 'CommentComponent',
    data() {
        return {
            errors: [],
            title: '',
            comment:'',
            num:'this is new data',
            userID: null,
            isVisible:false,
        }
    },
    methods: {
        submitCommentForm() {
            const data2 = new FormData()
            this.errors = []
            this.userID = this.$cookies.get("userID")
            if (!this.errors.length) {
                data2.append('title', this.title)
                data2.append('comment', this.comment)
                // this.slugg comes from props from parent component (ArticleView.vue)
                data2.append('slug', this.slugg)
                data2.append('userID', this.userID)                       
                axios.post("articles/comment/", data2).then(response =>{
                    if (response.data){
                        console.log(response.data),
                        // return data and pass it in publishComment(response.data) , to update coment without refresh page 
                        this.publishComment(response.data),
                        this.clearCommentFields(),
                        this.showMessageComment(),
                        this.$router.push('/samsung-s22')
                    }
                })
            }   
        },
        // dataa = response.data
        // emit will be executed in axios , i called this function over there
        // myComment is triger in parent component 
        publishComment(dataa){
            this.$emit('myComment', dataa)
        },
        clearCommentFields(){
            this.title = ''
            this.comment = ''
        },
        showMessageComment(){
            this.isVisible = true
            // after 5 sec this.isVisible will be set to false 
            setTimeout(() => this.isVisible = false, 5000);
        },
        deleteMessageComment(){
            this.isVisible = false
        }
    }

}
</script>