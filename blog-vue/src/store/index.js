import { createStore } from 'vuex'
export default createStore({
  state: {
    count: 0,
    basketList:[],
    totalPrice:0,
    popOutMsg:null,
    popOutMsgBasket:null,
    bookAvergeRating:null,
    showArticleTotalStars:null,
    userStars:null,
    userId:null,
    username:null,
    userImage: null,
    messageBasket:null,
    message:null,
    paymentMessage:false

  },
  getters: {
  },
  mutations: {    
    addBookToBasket(state,l){
      state.count++
      localStorage.setItem('count' , state.count)
      state.basketList.push({'book-name':l[0],'price':l[1],'book-photo':l[2],'slug':l[3]})
    },
    removeFromBasketStore(state,removeItemIndex){
      state.count--
      localStorage.setItem('count' , state.count)
      state.basketList.splice(removeItemIndex, 1);
    },
    addPriceStore(state,addPrice){
      state.totalPrice += parseFloat(addPrice)
    },
    subtractPriceStore(state,subtractPrice){
      state.totalPrice -= parseFloat(subtractPrice)
    },
    showMsg(state,msg){
      if(state.popOutMsg){
        clearTimeout(state.message)
      }
      state.popOutMsg = msg
      state.message = setTimeout(() => state.popOutMsg = null, 1900);        
    },
    showMsgBasket(state,msg){
      if(state.messageBasket){
        clearTimeout(state.messageBasket)
      }
      state.popOutMsgBasket = msg
      state.messageBasket = setTimeout(() => state.popOutMsgBasket = null, 1200);     
    },
    paymentMsg(state){
      state.paymentMessage = true
      setTimeout(() => state.paymentMessage = false, 4800);  
      // state.paymentMessage = setTimeout(() => state.paymentMessage = false, 1800);    
    },

  },

  actions: {

  },

  modules: {
  }

})

