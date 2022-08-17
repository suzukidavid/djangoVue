import Api from './api'

export default {
  getCompanyStock () {
    return Api().get('/get_stock');
  },
  checkStock () {
    return Api().get('/check_stock');
  }
}
