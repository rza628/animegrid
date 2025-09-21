<script>
  import { onMount, setContext } from "svelte";
  import Modal from "./Modal.svelte";
  import CategoryModal from "./CategoryModal.svelte";
  let errormessage = $state(null);

  let categoryInfo = $state(null);
  let showModal = $state(false);

  const dateTimeString = new Intl.DateTimeFormat("en-US", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  })
    .format(new Date())
    .replaceAll("/", "-");
  console.log(dateTimeString);
  let contextState = $state({ guessesLeft: 9, categories: [], imageUrls: [] });
  setContext("gameContext", contextState);
  onMount(async () => {
    try {
      const res2 = await fetch(
        `http://127.0.0.1:5000/api/categories/${dateTimeString}`
      );
      const data2 = await res2.json();

      contextState.categories = data2["categories"];
      // animeTitles = json["titles"]; // Jikan wraps the character in `data`
    } catch (e) {
      errormessage = e.message;
    }
  });

  function handleReset() {
    contextState.guessesLeft = 9;
    contextState.imageUrls = [];
  }

  function setCatModal(tile) {
    categoryInfo = contextState.categories[tile];
    showModal = true;
  }
</script>

{#snippet topCat(tile)}
  {#if contextState.categories.length >= 6}
    <button class="topTopic" onclick={() => setCatModal(tile)}
      >{contextState.categories[tile]["category"]}</button
    >
  {/if}
{/snippet}

{#snippet downCat(tile)}
  {#if contextState.categories.length >= 6}
    <button class="downTopic" onclick={() => setCatModal(tile)}
      >{contextState.categories[tile]["category"]}</button
    >
  {/if}
{/snippet}

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
  {/if}
</div>

<button class="reset" onclick={() => handleReset()}>Reset Game</button>

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
    font-size: 15px;
    padding: 0;
    border: none;
    outline: none;
    background: none;
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
    height: 75px;
    width: 150px;
  }
  p {
    font-size: xx-large;
  }
</style>
