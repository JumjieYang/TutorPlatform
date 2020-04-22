<template>
  <div class="block">
    <el-timeline>
      <el-timeline-item v-for="(item,index) of timeline" :key="index" :timestamp="item.timestamp" placement="top">
        <el-card>
          <h4>{{ item.title }}</h4>
          <p>{{ item.content }}</p>
        </el-card>
      </el-timeline-item>
    </el-timeline>
  </div>
</template>

<script>
export default {
  data() {
    return {
      timeline: [
        {
          timestamp: '2019/4/20',
          title: 'Comp 424',
          content: 'Midterm Prep'
        },
        {
          timestamp: '2019/4/21',
          title: 'Comp 535',
          content: 'Project help'
        },
        {
          timestamp: '2019/4/22',
          title: 'Comp 421',
          content: 'Assignment asistance'
        },
        {
          timestamp: '2019/4/23',
          title: 'Comp 360',
          content: 'Tutorial'
        }
      ]
    }
  }
}
</script>