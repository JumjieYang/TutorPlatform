import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios'
axios.defaults.baseURL = 'http://localhost:8000/'

Vue.use(Vuex)


export const store = new Vuex.Store({
    state:{
        token: localStorage.getItem('token') || null,
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
    },
    actions: {
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