import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios'
Vue.use(Vuex)


export const store = new Vuex.Store({
    state:{
        token: localStorage.getItem('token') || null,
        userId: localStorage.getItem('userId') || null,
        userName: localStorage.getItem('userName') || null,
    },
    getters:{
        loggedIn(state){
            return state.token != null;
        }
    },
    mutations:{
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

                // return new Promise((resolve, reject) => {
                //     axios.get("/api-auth/logout/",{
                //         headers: { 'Authorization' : 'Token '+ context.state.token}
                //     })
                //     .then((response) => {
                //         localStorage.removeItem('token')
                //         context.commit('destroyToken')
                //         resolve(response)
                //     })
                //     .catch((error) => {
                //         localStorage.removeItem('token')
                //         console.log("=====================action")
                //         context.commit('destroyToken')
                //         reject(error)
                //     })
                // })
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