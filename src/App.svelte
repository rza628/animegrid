<script>
  import Grid from "./lib/GridOld.svelte";
  import Grid2 from "./lib/Grid2.svelte";
  import Header from "./lib/Header.svelte";
</script>

<!-- <header>
  <h1 class="Title">Anime Grid</h1>
</header> -->

<!-- <footer>
  <h1 class="Footer">Ry Ly</h1>
</footer> -->

<div>
  <div class="top">
    <Header />
  </div>
  <div>
    <!-- <Grid /> -->
    <Grid2 />
  </div>
</div>

<style>
  .top {
    position: absolute;
    top: 0;
    left: 10px;
  }
  .character-card {
    max-width: 300px;
    border: 1px solid #eee;
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
  }
  .character-card img {
    max-width: 100%;
    border-radius: 4px;
  }
  .Title {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    text-align: center;
  }
  .Footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    text-align: center;
    font-size: small;
  }
</style>
