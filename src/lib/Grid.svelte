<script>
  import { onMount } from "svelte";
  import Modal from "./Modal.svelte";
  let guessesLeft = $state(9);
  let errormessage = $state(null);
  let categories = $state([]);

  let imageUrl1 = $state("");
  let imageUrl2 = $state("");
  let imageUrl3 = $state("");
  let imageUrl4 = $state("");
  let imageUrl5 = $state("");
  let imageUrl6 = $state("");
  let imageUrl7 = $state("");
  let imageUrl8 = $state("");
  let imageUrl9 = $state("");

  onMount(async () => {
    try {
      const res2 = await fetch("http://127.0.0.1:5000/api/categories");
      const data2 = await res2.json();
      categories = data2["categories"];
      // animeTitles = json["titles"]; // Jikan wraps the character in `data`
    } catch (e) {
      errormessage = e.message;
    }
  });

  function handleReset() {
    guessesLeft = 9;
    imageUrl1 =
      imageUrl2 =
      imageUrl3 =
      imageUrl4 =
      imageUrl5 =
      imageUrl6 =
      imageUrl7 =
      imageUrl8 =
      imageUrl9 =
        "";
  }
</script>

<div class="container">
  <div class="guess">
    Guesses Left:
    <p>{guessesLeft}</p>
  </div>
  <button class="topTopic">{categories[0]}</button>
  <button class="topTopic">{categories[1]}</button>
  <button class="topTopic">{categories[2]}</button>
  <button class="downTopic">{categories[3]}</button>

  <Modal gridTile={1} {categories} bind:guessesLeft bind:imageUrl={imageUrl1} />
  <Modal gridTile={2} {categories} bind:guessesLeft bind:imageUrl={imageUrl2} />
  <Modal gridTile={3} {categories} bind:guessesLeft bind:imageUrl={imageUrl3} />

  <button class="downTopic">{categories[4]}</button>
  <Modal gridTile={4} {categories} bind:guessesLeft bind:imageUrl={imageUrl4} />
  <Modal gridTile={5} {categories} bind:guessesLeft bind:imageUrl={imageUrl5} />
  <Modal gridTile={6} {categories} bind:guessesLeft bind:imageUrl={imageUrl6} />
  <button class="downTopic">{categories[5]}</button>
  <Modal gridTile={7} {categories} bind:guessesLeft bind:imageUrl={imageUrl7} />
  <Modal gridTile={8} {categories} bind:guessesLeft bind:imageUrl={imageUrl8} />
  <Modal gridTile={9} {categories} bind:guessesLeft bind:imageUrl={imageUrl9} />
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
