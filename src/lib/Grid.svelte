<script>
  import { onMount, setContext } from "svelte";
  import Modal from "./Modal.svelte";
  import CategoryModal from "./CategoryModal.svelte";
  import EndModal from "./EndModal.svelte";
  let errormessage = $state(null);

  let categoryInfo = $state(null);
  let showModal = $state(false);
  let endShowModal = $state(false);
  let score = $state(0);

  const dateTimeString = new Intl.DateTimeFormat("en-US", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  })
    .format(new Date())
    .replaceAll("/", "-");
  console.log(dateTimeString);
  let contextState = $state({
    guessesLeft: 9,
    categories: [],
    imageUrls: [],
    score: 0,
  });
  setContext("gameContext", contextState);
  onMount(async () => {
    try {
      const res2 = await fetch(
        `https://animegrid-backend-1.onrender.com/api/categories/${dateTimeString}`
      );
      const data2 = await res2.json();

      contextState.categories = data2["categories"];
      // animeTitles = json["titles"]; // Jikan wraps the character in `data`
    } catch (e) {
      errormessage = e.message;
    }
  });

  function handleGiveUp() {
    contextState.guessesLeft = 9;
    contextState.imageUrls = [];
    contextState.score = 0;
    endShowModal = true;
  }

  function setCatModal(tile) {
    categoryInfo = contextState.categories[tile];
    showModal = true;
  }
</script>

{#snippet topCat(tile)}
  {#if contextState.categories.length >= 6}
    <button class="topTopic" onclick={() => setCatModal(tile)}>
      {#if contextState.categories[tile]["type"] === "genres"}
        {`Genre:
        `}
      {/if}
      {#if contextState.categories[tile]["type"] === "demographics"}
        Demographic:
      {/if}
      {#if contextState.categories[tile]["type"] === "source"}
        Source:
      {/if}

      {contextState.categories[tile]["category"]}
    </button>
  {/if}
{/snippet}

{#snippet downCat(tile)}
  {#if contextState.categories.length >= 6}
    <button class="downTopic" onclick={() => setCatModal(tile)}>
      {#if contextState.categories[tile]["type"] === "Episodes"}
        Number of Episodes:
      {/if}
      {#if contextState.categories[tile]["type"] === "Year"}
        {`Started Airing In:
        `}
      {/if}
      {#if contextState.categories[tile]["type"] === "Airing Status"}
        Airing Status:
      {/if}
      {#if contextState.categories[tile]["type"] === "Mal Score"}
        Mal Score:
      {/if}
      {contextState.categories[tile]["category"]}
    </button>
  {/if}
{/snippet}
<div class="row">
  <div class="container">
    {#if contextState.categories.length >= 6}
      <div class="guess">
        Guesses Left:
        <p>{contextState.guessesLeft}</p>
      </div>

      {@render topCat(0)}
      {@render topCat(1)}
      {@render topCat(2)}

      {@render downCat(3)}

      <Modal gridTile={1} />
      <Modal gridTile={2} />
      <Modal gridTile={3} />

      {@render downCat(4)}

      <Modal gridTile={4} />
      <Modal gridTile={5} />
      <Modal gridTile={6} />

      {@render downCat(5)}

      <Modal gridTile={7} />
      <Modal gridTile={8} />
      <Modal gridTile={9} />

      <CategoryModal bind:showModal {categoryInfo} />
      <EndModal bind:endShowModal />
    {/if}
  </div>
  <div class="score">
    Score:
    <p>{contextState.score}</p>
    <button class="reset" onclick={() => handleGiveUp()}>Give Up</button>
  </div>
</div>

<style>
  .row {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .score {
    width: 100px;
    margin-top: 160px;
    height: 160px;
  }
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
    font-size: 15px;
    padding: 0;
    border: none;
    outline: none;
    background: none;
    text-wrap: pretty;
    white-space: pre-line;
  }
  .downTopic {
    width: 100px;
    max-height: 160px;
    padding: 0;
    font-size: 15px;
    overflow: hidden;
    border: none;
    outline: none;
    background: none;
    align-self: center;
    justify-self: baseline;
    text-wrap: pretty;
    white-space: pre-line;
  }
  .image {
    width: 100px;
    height: 160px;
    text-align: center;
    border-radius: 8px;
  }
  .guess {
    width: 100px;
    padding: 0;
  }
  .reset {
    white-space: normal;
    max-height: 40px;
  }
  p {
    font-size: xx-large;
  }
</style>
