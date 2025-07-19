<script>
  import { onMount } from "svelte";
  import Modal from "./Modal.svelte";
  let guessesLeft = $state(9);
  let errormessage = $state(null);
  let animeTitles = $state([]);
  let categories = $state([]);

  let showModal1 = $state(false);
  let showModal2 = $state(false);
  let showModal3 = $state(false);
  let showModal4 = $state(false);
  let showModal5 = $state(false);
  let showModal6 = $state(false);
  let showModal7 = $state(false);
  let showModal8 = $state(false);
  let showModal9 = $state(false);

  let selectedTile = $state(0);

  let tile1 = $state(false);
  let tile2 = $state(false);
  let tile3 = $state(false);
  let tile4 = $state(false);
  let tile5 = $state(false);
  let tile6 = $state(false);
  let tile7 = $state(false);
  let tile8 = $state(false);
  let tile9 = $state(false);

  let imageURL1 = $state("");
  let imageURL2 = $state("");
  let imageURL3 = $state("");
  let imageURL4 = $state("");
  let imageURL5 = $state("");
  let imageURL6 = $state("");
  let imageURL7 = $state("");
  let imageURL8 = $state("");
  let imageURL9 = $state("");
  onMount(async () => {
    try {
      // Don’t call jikanjs.loadCharacter(...)—just use the raw URL:
      const res = await fetch("http://127.0.0.1:5000/api/animetitles");
      const data = await res.json();

      animeTitles = data["titles"];

      const res2 = await fetch("http://127.0.0.1:5000/api/categories");
      const data2 = await res2.json();
      categories = data2["categories"];
      // animeTitles = json["titles"]; // Jikan wraps the character in `data`
    } catch (e) {
      errormessage = e.message;
    }
  });

  function handleReset() {
    tile1 =
      tile2 =
      tile3 =
      tile4 =
      tile5 =
      tile6 =
      tile7 =
      tile8 =
      tile9 =
        false;
    imageURL1 =
      imageURL2 =
      imageURL3 =
      imageURL4 =
      imageURL5 =
      imageURL6 =
      imageURL7 =
      imageURL8 =
      imageURL9 =
        "";
    guessesLeft = 9;
  }
</script>

<div class="container">
  <div></div>
  <button class="topTopic">{categories[0]}</button>
  <button class="topTopic">{categories[1]}</button>
  <button class="topTopic">{categories[2]}</button>
  <button class="downTopic">{categories[3]}</button>
  {#if tile1}
    <img class="image" src={imageURL1} alt="Anime Thumbnail from myanimelist" />
  {:else}
    <button
      class="cell1"
      aria-label="Close"
      onclick={() => {
        {
          selectedTile = 1;
          showModal1 = true;
        }
      }}
    ></button>
  {/if}
  {#if tile2}
    <img class="image" src={imageURL2} alt="Anime Thumbnail from myanimelist" />
  {:else}
    <button
      class="cell2"
      aria-label="Close"
      onclick={() => {
        {
          selectedTile = 2;
          showModal2 = true;
        }
      }}
    ></button>
  {/if}
  {#if tile3}
    <img class="image" src={imageURL3} alt="Anime Thumbnail from myanimelist" />
  {:else}
    <button
      class="cell3"
      aria-label="Close"
      onclick={() => {
        {
          selectedTile = 3;
          showModal3 = true;
        }
      }}
    ></button>
  {/if}
  <button class="downTopic">{categories[4]}</button>
  {#if tile4}
    <img class="image" src={imageURL4} alt="Anime Thumbnail from myanimelist" />
  {:else}
    <button
      class="cell4"
      aria-label="Close"
      onclick={() => {
        {
          selectedTile = 4;
          showModal4 = true;
        }
      }}
    ></button>
  {/if}
  {#if tile5}
    <img class="image" src={imageURL5} alt="Anime Thumbnail from myanimelist" />
  {:else}
    <button
      class="cell5"
      aria-label="Close"
      onclick={() => {
        {
          selectedTile = 5;
          showModal5 = true;
        }
      }}
    ></button>
  {/if}
  {#if tile6}
    <img class="image" src={imageURL6} alt="Anime Thumbnail from myanimelist" />
  {:else}
    <button
      class="cell6"
      aria-label="Close"
      onclick={() => {
        {
          selectedTile = 6;
          showModal6 = true;
        }
      }}
    ></button>
  {/if}
  <button class="downTopic">{categories[5]}</button>
  {#if tile7}
    <img class="image" src={imageURL7} alt="Anime Thumbnail from myanimelist" />
  {:else}
    <button
      class="cell7"
      aria-label="Close"
      onclick={() => {
        {
          selectedTile = 7;
          showModal7 = true;
        }
      }}
    ></button>
  {/if}
  {#if tile8}
    <img class="image" src={imageURL8} alt="Anime Thumbnail from myanimelist" />
  {:else}
    <button
      class="cell8"
      aria-label="Close"
      onclick={() => {
        {
          selectedTile = 8;
          showModal8 = true;
        }
      }}
    ></button>
  {/if}
  {#if tile9}
    <img class="image" src={imageURL9} alt="Anime Thumbnail from myanimelist" />
  {:else}
    <button
      class="cell9"
      aria-label="Close"
      onclick={() => {
        {
          selectedTile = 9;
          showModal9 = true;
        }
      }}
    ></button>
  {/if}
  <!-- MODALS -->
  <Modal
    bind:showModal={showModal1}
    {animeTitles}
    {selectedTile}
    {categories}
    bind:value={imageURL1}
    bind:tile={tile1}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal2}
    {animeTitles}
    {selectedTile}
    {categories}
    bind:value={imageURL2}
    bind:tile={tile2}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal3}
    {animeTitles}
    {selectedTile}
    {categories}
    bind:value={imageURL3}
    bind:tile={tile3}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal4}
    {animeTitles}
    {selectedTile}
    {categories}
    bind:value={imageURL4}
    bind:tile={tile4}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal5}
    {animeTitles}
    {selectedTile}
    {categories}
    bind:value={imageURL5}
    bind:tile={tile5}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal6}
    {animeTitles}
    {selectedTile}
    {categories}
    bind:value={imageURL6}
    bind:tile={tile6}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal7}
    {animeTitles}
    {selectedTile}
    {categories}
    bind:value={imageURL7}
    bind:tile={tile7}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal8}
    {animeTitles}
    {selectedTile}
    {categories}
    bind:value={imageURL8}
    bind:tile={tile8}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal9}
    {animeTitles}
    {selectedTile}
    {categories}
    bind:value={imageURL9}
    bind:tile={tile9}
    bind:guessesLeft
  ></Modal>
</div>

<style>
  .container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(4, 1fr);
    align-items: end;
    justify-items: center;
    gap: 1px;
  }
  button {
    width: 100px;
    height: 160px;
    word-wrap: break-word;
  }
  .topTopic {
    width: 100px;
    height: 100px;
    padding: 0;
    border: none;
    outline: none;
    background: none;
  }
  .downTopic {
    width: 100px;
    max-height: 160px;
    padding: 0;
    overflow: hidden;
    border: none;
    outline: none;
    background: none;
    align-self: center;
    justify-self: baseline;
  }
  .image {
    width: 100px;
    height: 160px;
    text-align: center;
    border-radius: 8px;
  }
</style>
