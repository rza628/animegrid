<script>
  import { onMount, setContext } from "svelte";
  import Modal from "./Modal.svelte";
  import CategoryModal from "./CategoryModal.svelte";
  import EndModal from "./EndModal.svelte";
  let errormessage = $state(null);

  let categoryInfo = $state(null);
  let showModal = $state(false);
  let endShowModal = $state(false);

  const dateTimeString = new Intl.DateTimeFormat("en-US", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  })
    .format(new Date())
    .replaceAll("/", "-");
  let contextState = $state({
    dateTimeString: dateTimeString,
    guessesLeft: 9,
    categories: [],
    imageUrls: [null, null, null, null, null, null, null, null, null],
    score: 0,
    end: false,
    validGuess: 0,
    wrongGuess: 0,
  });
  setContext("gameContext", contextState);
  onMount(async () => {
    try {
      // check local storage if data alr exist by using date
      // if yes, load local storage data into context state
      const localGameData = localStorage.getItem(dateTimeString);
      if (localGameData) {
        // console.log("exists");
        const parsedData = JSON.parse(localGameData);
        contextState.guessesLeft = parsedData["guessesLeft"];
        contextState.categories = parsedData["categories"];
        contextState.imageUrls = parsedData["imageUrls"];
        contextState.score = parsedData["score"];
        contextState.end = parsedData["end"];
        contextState.validGuess = parsedData["validGuess"];
        contextState.wrongGuess = parsedData["wrongGuess"];
      } else {
        // console.log("api call made");
        localStorage.clear();
        const res = await fetch(
          `${import.meta.env.VITE_FASTAPIBACKENDURL}/api/categories/${dateTimeString}`
        );
        const data = await res.json();
        contextState.categories = data["categories"];
        localStorage.setItem(dateTimeString, JSON.stringify(contextState));
      }
      //if no, do api fetch to get categories, make new localstorage and save to it, also clear localstorage to get rid of past game states

      // save to local storage and context state after every action : guessing,  give up, finish game etc

      // contextState.categories = data2["categories"];
      // animeTitles = json["titles"]; // Jikan wraps the character in `data`
      if (contextState.end === true) {
        endShowModal = true;
      }
    } catch (e) {
      errormessage = e.message;
    }
  });

  function handleGiveUp() {
    endShowModal = true;
    contextState.end = true;
    localStorage.setItem(dateTimeString, JSON.stringify(contextState));
  }

  function setCatModal(tile) {
    categoryInfo = contextState.categories[tile];
    showModal = true;
  }
  function viewStats() {
    endShowModal = true;
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
      {#if contextState.end}
        <button class="viewStats" onclick={() => viewStats()}
          >Game Done View Stats</button
        >
      {:else}
        <div class="guess">
          Guesses Left:
          <p>{contextState.guessesLeft}</p>
        </div>
      {/if}
      {@render topCat(0)}
      {@render topCat(1)}
      {@render topCat(2)}

      {@render downCat(3)}

      <Modal gridTile={1} bind:endShowModal />
      <Modal gridTile={2} bind:endShowModal />
      <Modal gridTile={3} bind:endShowModal />

      {@render downCat(4)}

      <Modal gridTile={4} bind:endShowModal />
      <Modal gridTile={5} bind:endShowModal />
      <Modal gridTile={6} bind:endShowModal />

      {@render downCat(5)}

      <Modal gridTile={7} bind:endShowModal />
      <Modal gridTile={8} bind:endShowModal />
      <Modal gridTile={9} bind:endShowModal />

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
  .viewStats {
    width: 100px;
    height: 160px;
    background-color: transparent;
    word-wrap: break-word;
    padding: 0;
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
