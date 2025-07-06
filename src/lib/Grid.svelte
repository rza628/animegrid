<script>
  import { onMount } from "svelte";
  import Modal from "./Modal.svelte";
  let guessesLeft = $state(9);
  let errormessage = $state(null);
  let animeTitles = $state([]);

  let showModal1 = $state(false);
  let showModal2 = $state(false);
  let showModal3 = $state(false);
  let showModal4 = $state(false);
  let showModal5 = $state(false);
  let showModal6 = $state(false);
  let showModal7 = $state(false);
  let showModal8 = $state(false);
  let showModal9 = $state(false);

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
      const res = await fetch("src/assets/anime_titles_nodupes.csv")
        .then((res) => res.text())
        .then((text) => {
          const list = text.split("\r\n");
          list.map((entry) => {
            const split = entry.split(",");
            const title = split[0],
              id = split[1];
            if (title && id) {
              animeTitles.push({ title: title, id: id });
            }
          });
        });

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

<!-- {#if errormessage}
  <p style="color: red">{errormessage}</p>
{:else if character}
    <div class="character-card">
      <img src="{character.images.jpg.image_url}" alt="{character.name}" />
      <h2>{character.name}</h2>
      <p>{@html character.about}</p>
    </div>
{:else}
  <p>Loading character…</p>
{/if} -->
<div class="main">
  <div class="acrossGrid">
    <div class="empty"></div>
    <button class="acrossTopic" aria-label="Close">topic 1</button>
    <button class="acrossTopic" aria-label="Close">topic 2</button>
    <button class="acrossTopic" aria-label="Close">topic 3</button>
  </div>
  <div class="rows">
    <div>
      <div class="grid">
        <button class="downTopic" aria-label="Close">topic 4</button>
        <!-- TILE 1 -->
        {#if tile1}
          <img
            class="image"
            src={imageURL1}
            alt="Anime Thumbnail from myanimelist"
          />
        {:else}
          <button
            class="cell1"
            aria-label="Close"
            onclick={() => {
              showModal1 = true;
            }}
          ></button>
        {/if}
        <!--    TILE 2 -->
        {#if tile2}
          <img
            class="image"
            src={imageURL2}
            alt="Anime Thumbnail from myanimelist"
          />
        {:else}
          <button
            class="cell2"
            aria-label="Close"
            onclick={() => {
              showModal2 = true;
            }}
          ></button>
        {/if}
        <!--   TILE 3 -->
        {#if tile3}
          <img
            class="image"
            src={imageURL3}
            alt="Anime Thumbnail from myanimelist"
          />
        {:else}
          <button
            class="cell3"
            aria-label="Close"
            onclick={() => {
              showModal3 = true;
            }}
          ></button>
        {/if}
      </div>
      <div class="grid">
        <button class="downTopic" aria-label="Close">topic 5</button>
        <!-- TILE 4 -->
        {#if tile4}
          <img
            class="image"
            src={imageURL4}
            alt="Anime Thumbnail from myanimelist"
          />
        {:else}
          <button
            class="cell4"
            aria-label="Close"
            onclick={() => {
              showModal4 = true;
            }}
          ></button>
        {/if}
        <!--  TILE 5 -->
        {#if tile5}
          <img
            class="image"
            src={imageURL5}
            alt="Anime Thumbnail from myanimelist"
          />
        {:else}
          <button
            class="cell5"
            aria-label="Close"
            onclick={() => {
              showModal5 = true;
            }}
          ></button>
        {/if}
        <!--  TILE 6 -->
        {#if tile6}
          <img
            class="image"
            src={imageURL6}
            alt="Anime Thumbnail from myanimelist"
          />
        {:else}
          <button
            class="cell6"
            aria-label="Close"
            onclick={() => {
              showModal6 = true;
            }}
          ></button>
        {/if}
      </div>
      <div class="grid">
        <button class="downTopic" aria-label="Close">topic 6</button>
        <!-- TILE 7 -->
        {#if tile7}
          <img
            class="image"
            src={imageURL7}
            alt="Anime Thumbnail from myanimelist"
          />
        {:else}
          <button
            class="cell7"
            aria-label="Close"
            onclick={() => {
              showModal7 = true;
            }}
          ></button>
        {/if}

        <!-- TILE 8 -->
        {#if tile8}
          <img
            class="image"
            src={imageURL8}
            alt="Anime Thumbnail from myanimelist"
          />
        {:else}
          <button
            class="cell8"
            aria-label="Close"
            onclick={() => {
              showModal8 = true;
            }}
          ></button>
        {/if}
        <!-- TILE 9 -->
        {#if tile9}
          <img
            class="image"
            src={imageURL9}
            alt="Anime Thumbnail from myanimelist"
          />
        {:else}
          <button
            class="cell9"
            aria-label="Close"
            onclick={() => {
              showModal9 = true;
            }}
          ></button>
        {/if}
      </div>
    </div>
    <div class="guess">Guesses Left: {guessesLeft}</div>
  </div>
  <button class="reset" onclick={() => handleReset()}>Reset Game</button>

  <Modal
    bind:showModal={showModal1}
    {animeTitles}
    bind:value={imageURL1}
    bind:tile={tile1}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal2}
    {animeTitles}
    bind:value={imageURL2}
    bind:tile={tile2}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal3}
    {animeTitles}
    bind:value={imageURL3}
    bind:tile={tile3}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal4}
    {animeTitles}
    bind:value={imageURL4}
    bind:tile={tile4}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal5}
    {animeTitles}
    bind:value={imageURL5}
    bind:tile={tile5}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal6}
    {animeTitles}
    bind:value={imageURL6}
    bind:tile={tile6}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal7}
    {animeTitles}
    bind:value={imageURL7}
    bind:tile={tile7}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal8}
    {animeTitles}
    bind:value={imageURL8}
    bind:tile={tile8}
    bind:guessesLeft
  ></Modal>
  <Modal
    bind:showModal={showModal9}
    {animeTitles}
    bind:value={imageURL9}
    bind:tile={tile9}
    bind:guessesLeft
  ></Modal>
</div>

<style>
  .image {
    width: 100px;
    height: 160px;
    text-align: center;
    border-radius: 8px;
  }
  .grid {
    display: grid;
    gap: 1px;
    grid-template-columns: repeat(4, 1fr);
    align-items: center;
  }

  .rows {
    display: flex;
    flex-direction: row;
  }

  button {
    width: 100px;
    height: 160px;
  }
  .acrossTopic {
    width: 100px;
    height: 50px;
    border: none;
    outline: none;
    background: none;
  }
  .downTopic {
    width: 100px;
    height: 50px;

    border: none;
    outline: none;
    background: none;
  }
  .empty {
    width: 100px;
    height: 50px;
    border: none;
    outline: none;
    background: none;
  }
  .main {
    margin: 0 auto;
  }
  .guess {
    width: 100px;
    height: 50px;
    align-self: center;
  }
  .reset {
    width: auto;
    height: auto;
  }
</style>
