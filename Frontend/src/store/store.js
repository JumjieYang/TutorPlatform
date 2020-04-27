import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios'
Vue.use(Vuex)


export const store = new Vuex.Store({
    state:{
        chatList: [''],
        isTutor: false,
        token: localStorage.getItem('token') || null,
        userId: localStorage.getItem('userId') || null,
        userName: localStorage.getItem('userName') || null,
        profileImage:'',
        info: {
            firstName: '',
            lastName: '',
            phone: '',
            age: ''
        }
    },
    getters:{
        loggedIn(state){
            return state.token != null;
        }
    },
    mutations:{
        addToChatList(state, chat){
            state.chatList.push(chat);
        },
        retrieveToken(state, token) {
            state.token = token;
        },
        destroyToken(state){
            state.token = null;
        },
        setUserId(state, userId){
            state.userId = userId;
        },
        setUserName(state, userName){
            state.userName = userName;
        },
        setIsTutor(state, isTutor){
            state.isTutor = isTutor
            console.log("store is tutor "+isTutor)        
        },
        setProfileImage(state, profileImage){
            state.profileImage = profileImage
        },
        setInfo(state, info){
            state.info = info
        }
    },
    actions: {
        signOut(context) {
            if (context.getters.loggedIn) {
                axios.get("/api-auth/logout/",{
                    headers: { 'Authorization' : 'Token '+ context.state.token}
                })
                localStorage.removeItem('token')
                console.log("signed out")
                context.commit('destroyToken')

            }
        },  
        retrieveToken (context, credentials) {
            return new Promise((resolve, reject) => {
                axios.post('/api-auth/login/', {
                    username: credentials.username,
                    password: credentials.password,
                })
                .then(response => {
                    //console.log(response)
                    const token = response.data.token
                    localStorage.setItem('token', token)
                    context.commit('retrieveToken', token)
                    localStorage.setItem('userName', response.data.username)
                    context.commit('setUserName', response.data.username)
                    localStorage.setItem('userId', response.data.user_id)
                    context.commit('setUserId', response.data.user_id)
                    resolve(response)
                })
                .catch(error => {
                    console.log(error)
                    reject(error)
                })
            })
        }
    }
})
