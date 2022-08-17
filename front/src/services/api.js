import axios from 'axios'

// const API_ROOT = `http://${document.domain}:8000`
const API_ROOT = `http://127.0.0.1:8000`
export default() => {
  return axios.create({
    baseURL: `${API_ROOT}`,
    method: 'post',
    withCredentials: false,
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }
  })
}
