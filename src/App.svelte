<script>
  import Grid from "./lib/Grid.svelte";
</script>


<header>
    <h1 class = "Title">Anime Grid</h1>
</header>

<footer>
  <h1 class = "Footer">Ry Ly</h1>
</footer>


<main>
  <div>
    <Grid/>
  </div>
</main>


<style>
  .Title{
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    text-align: center;
  }
  .Footer{
    position: fixed;
    left: 0;
    bottom:0;
    width: 100%;
    text-align: center;
    font-size: small;
  }
</style>

