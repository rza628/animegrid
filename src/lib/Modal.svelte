<script>
  import Search from "./Search.svelte";
  let {
    guessesLeft = $bindable(),
    imageUrl = $bindable(),
    categories,
    gridTile,
  } = $props();
  let showModal = $state(false);
  let searchTerm = $state("");
  let guessID = $state("");

  let dialog = $state(); // HTMLDialogElement

  const checkCat = $derived({
    1: [categories[0], categories[3]],
    2: [categories[1], categories[3]],
    3: [categories[2], categories[3]],
    4: [categories[0], categories[4]],
    5: [categories[1], categories[4]],
    6: [categories[2], categories[4]],
    7: [categories[0], categories[5]],
    8: [categories[1], categories[5]],
    9: [categories[2], categories[5]],
  });

  $effect(() => {
    if (showModal) dialog.showModal();
  });

  async function handleGuess() {
    //get image url from mal api
    try {
      const response = await fetch(
        `https://api.jikan.moe/v4/anime/${parseInt(guessID)}`
      );
      const data = await response.json();
      const guessGenres = [
        ...data["data"]["genres"],
        ...data["data"]["explicit_genres"],
        ...data["data"]["themes"],
        ...data["data"]["demographics"],
      ].map((genre) => genre["name"]);

      console.log("tile num", checkCat);
      const cat1 = checkCat[gridTile][0];
      const cat2 = checkCat[gridTile][1];

      console.log("guess genres", guessGenres);
      console.log("categories", cat1, cat2);
      //check the guess, correct, replace condition with true if want to test images
      if (guessGenres.includes(cat1) && guessGenres.includes(cat2)) {
        imageUrl = data["data"]["images"]["webp"]["image_url"];
        guessesLeft -= 1;
        searchTerm = "";
        dialog.close();
      } else {
        guessesLeft -= 1;
        searchTerm = "";
        dialog.close();
      }
    } catch (e) {
      console.log(e.message);
    }
  }
</script>

<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_noninteractive_element_interactions -->
{#if imageUrl !== ""}
  <img class="image" src={imageUrl} alt="Anime Thumbnail from myanimelist" />
{:else}
  <button
    class="gridTile"
    aria-label="Close"
    onclick={() => {
      {
        showModal = true;
      }
    }}
  ></button>
{/if}

<dialog
  class="dialogBox"
  bind:this={dialog}
  onclose={() => (showModal = false)}
  onclick={(e) => {
    if (e.target === dialog) dialog.close();
  }}
>
  <div>
    <div>
      <!-- svelte-ignore a11y_autofocus -->
      <Search bind:value={guessID} bind:searchTerm />
    </div>
    <div class="buttons">
      <button onclick={() => handleGuess()} class="submit">Submit Guess</button>
      <button onclick={() => dialog.close()} class="close">close modal</button>
    </div>
  </div>
</dialog>

<style>
  .gridTile {
    width: 100px;
    height: 160px;
    word-wrap: break-word;
  }
  .image {
    width: 100px;
    height: 160px;
    text-align: center;
    border-radius: 8px;
  }
  .buttons {
    display: flex;
    flex: 1;
    justify-content: space-between;
    align-content: center;
    gap: 20px;
    padding-top: 10px;
  }
  dialog {
    max-width: 40em;
    border-radius: 0.2em;
    border: none;
    padding: 0;
  }
  dialog::backdrop {
    background: rgba(0, 0, 0, 0.3);
  }
  dialog > div {
    padding: 1em;
  }
  dialog[open] {
    animation: zoom 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  }
  @keyframes zoom {
    from {
      transform: scale(0.95);
    }
    to {
      transform: scale(1);
    }
  }
  dialog[open]::backdrop {
    animation: fade 0.2s ease-out;
  }
  @keyframes fade {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
  button {
    display: block;
  }
</style>
