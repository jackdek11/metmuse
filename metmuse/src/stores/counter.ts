import { defineStore } from 'pinia'

interface State {
  username: String | null
  email: String | null
  picture: URL | null
  token: String | null
}

export const useUserStore = defineStore('user', {
  state: (): State => {
    return {
      username: null,
      email: null,
      picture: null,
      token: null
    }
  },
  getters: {
    username(state): String | null {
      return state.username
    },
    email(): String | null {
      return this.email
    },
    picture(): URL | null {
      return this.picture
    },
    token(): String | null {
      return this.token
    }
  },
  actions: {
    async addUserDetails(details: State) {
      this.username = details.username;
      this.picture = details.picture;
      this.email = details.email;
    },
    async setToken(token: String | null) {
      this.token = token
    }
  },
})
