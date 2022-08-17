<template>
  <div class="container">
    <block-header></block-header>
    <block-table></block-table>
    <block-footer></block-footer>
  </div>
</template>

<script>
import BlockHeader from './Header.vue';
import BlockTable from './Table.vue';
import BlockFooter from './Footer.vue';
export default {
  name: 'Home',
  components: {
    'block-header': BlockHeader,
    'block-table': BlockTable,
    'block-footer': BlockFooter
  },
  data () {
    return {}
  }
}
</script>
