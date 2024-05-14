import axios from 'axios'
import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('article', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const createArticle = function ({ title, content}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title,
        content
      }
    })
    .then(res => console.log(res))
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload
    
    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((response) => {
        console.log('회원가입 성공!')
        // 회원가입 성공 후 자동으로 로그인까지 진행
        const password = password1
        logIn({ username, password })
      })
      .catch((error) => {
        console.log(error)
      })
  }
  

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
    .then((response) => {
      token.value = response.data.key
      router.push({ name : 'ArticleView' })
    })
    .catch((error) => {
      console.log(error)
    })
  }

  return { articles, API_URL, getArticles, createArticle, signUp, logIn, token, isLogin }
}, {persist: true})