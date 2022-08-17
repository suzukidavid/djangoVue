<template>
    <div class="row p-3">
        <div class="col-12">
            <table class="table">
                <thead class="">
                    <tr>
                        <th>Symbol</th>
                        <th>Name</th>
                        <th>Last Price</th>
                        <th>%Change</th>
                        <th>Volume</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(row, idx) in parseData" :key="idx">
                        <td>{{row.symbol}}</td>
                        <td>{{row.name}}</td>
                        <td>{{row.last_price}}</td>
                        <td :class="[parseFloat(row.changed_value) < 0 ? 'font-red' : 'font-green']">{{row.changed_value}}</td>
                        <td>{{row.volume}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import Service from '../services/services.js';
export default {
    name: 'BlockTable',
    data:() => ({
        parseData: []
    }),
    methods: {
        async getInvestingInfo() {
            var info = await Service.getCompanyStock();
            this.parseData = info.data;
        }
    },
    mounted () {
        this.getInvestingInfo()
    }
}
</script>
<style>
  .font-red {
      color: red;
  }
  .font-green {
      color: green;
  }
</style>