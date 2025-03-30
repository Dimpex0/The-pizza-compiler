import axios from "axios";

export const regularApi = axios.create({
    baseURL: import.meta.env.VITE_SERVER_URL,
    withCredentials: true,
})

export const api = axios.create({
    baseURL: import.meta.env.VITE_SERVER_URL,
    withCredentials: true,
})

api.interceptors.response.use(
    (response) => response,
    async function (error){
    const originalRequest = error.config;

    if (error.response && error.response.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true;

        api.post('account/token/refresh')
            .then(() => {
                return api(originalRequest)
            })
            .catch(() => {
                console.log("Token refresh failed. Login required.")
                window.location.href = '/login'
            })
    }
    return Promise.reject(error)
})