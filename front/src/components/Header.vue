<template>
  <div class="row justify-content-center top-bar-background p-2">
    <div class="col-6 text-left align-self-center">
      <span class="text-white font-weight-bold align-middle">Stock Screener</span>
    </div>
    <div class="col-6 text-right">
      <button class="btn btn-success" @click="checkInvestingStock()">Update</button>
    </div>
  </div>
</template>

<script>
import Service from '../services/services.js'
export default {
  name: 'BlockHeader',
  methods: {
    checkInvestingStock() {
      Service.checkStock();
    }
  }
}
</script>
<style>
  .top-bar-background {
    background-color: #445A63;
  }
</style>