import { createStore } from 'vuex';

const store = createStore({
    state: {
        userId: null, 
        userEmail: null
    },
    mutations: {
        setUserId(state, userId) {
            state.userId = userId; // Set userId
        },
        clearUserId(state) {
            state.userId = null; // Clear userId on logout
        },
        setUserEmail(state, userEmail) {
            state.userEmail = userEmail; // Set userEmail
        },
        clearUserEmail(state) {
            state.userEmail = null; // Clear userEmail on logout
        }
    },
    actions: {
        login({ commit }, {userId, userEmail}) {
            commit('setUserId', userId); // Commit userId on login
            commit('setUserEmail', userEmail); // Commit userEmail on login
        },
        logout({ commit }) {
            commit('clearUserId'); // Clear userId on logout
            commit('clearUserEmail'); // Clear userEmail on logout
        }
    }
});

export default store;