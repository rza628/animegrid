<script>
  import { onMount, setContext, getContext } from "svelte";
  import Modal from "./Modal.svelte";
  let errormessage = $state(null);

  let contextState = $state({ guessesLeft: 9, categories: [], imageUrls: [] });
  setContext("gameContext", contextState);
  let gameContext = getContext("gameContext");
  onMount(async () => {
    try {
      const res2 = await fetch("http://127.0.0.1:5000/api/categories");
      const data2 = await res2.json();

      contextState.categories = data2["categories"];
      // animeTitles = json["titles"]; // Jikan wraps the character in `data`
    } catch (e) {
      errormessage = e.message;
    }
  });

  function handleReset() {
    gameContext.guessesLeft = 9;
    gameContext.imageUrls = [];
  }
</script>

<div class="container">
  <div class="guess">
    Guesses Left:
    <p>{gameContext.guessesLeft}</p>
  </div>
  <button class="topTopic">{gameContext.categories[0]}</button>
  <button class="topTopic">{gameContext.categories[1]}</button>
  <button class="topTopic">{gameContext.categories[2]}</button>
  <button class="downTopic">{gameContext.categories[3]}</button>

  <Modal gridTile={1} />
  <Modal gridTile={2} />
  <Modal gridTile={3} />

  <button class="downTopic">{gameContext.categories[4]}</button>
  <Modal gridTile={4} />
  <Modal gridTile={5} />
  <Modal gridTile={6} />
  <button class="downTopic">{gameContext.categories[5]}</button>
  <Modal gridTile={7} />
  <Modal gridTile={8} />
  <Modal gridTile={9} />
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
