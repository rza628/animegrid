<script>
  import { getContext } from "svelte";
  import Search from "./Search.svelte";
  let { gridTile } = $props();
  let showModal = $state(false);
  let searchTerm = $state("");
  let guessID = $state("");

  let dialog = $state(); // HTMLDialogElement
  let gameContext = getContext("gameContext");

  const checkCat = $derived({
    1: [gameContext.categories[0], gameContext.categories[3]],
    2: [gameContext.categories[1], gameContext.categories[3]],
    3: [gameContext.categories[2], gameContext.categories[3]],
    4: [gameContext.categories[0], gameContext.categories[4]],
    5: [gameContext.categories[1], gameContext.categories[4]],
    6: [gameContext.categories[2], gameContext.categories[4]],
    7: [gameContext.categories[0], gameContext.categories[5]],
    8: [gameContext.categories[1], gameContext.categories[5]],
    9: [gameContext.categories[2], gameContext.categories[5]],
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
      /* const guessGenres = [
        ...data["data"]["genres"],
        ...data["data"]["explicit_genres"],
        ...data["data"]["themes"],
        ...data["data"]["demographics"],
      ].map((genre) => genre["name"]); */

      /* console.log("tile num", checkCat); */
      const cat1 = checkCat[gridTile][0];
      const cat2 = checkCat[gridTile][1];

      console.log("categories", cat1, cat2);
      console.log(data);
      //check the guess, correct, replace condition with true if want to test images
      const check1 = await checkValid(cat1, data);
      const check2 = await checkValid(cat2, data);
      console.log(check1, check2);
      if (check1 && check2) {
        gameContext.imageUrls[gridTile - 1] =
          data["data"]["images"]["webp"]["image_url"];
        gameContext.guessesLeft -= 1;
        searchTerm = "";
        dialog.close();
      } else {
        gameContext.guessesLeft -= 1;
        searchTerm = "";
        dialog.close();
      }
    } catch (e) {
      console.log(e.message);
    }
  }

  async function checkValid(category, data) {
    try {
      const type = category["type"];
      const catString = category["category"];
      if (type === "genre") {
        return data["data"]["genres"].some(
          (entry) => entry["name"] === catString
        );
      } else if (type === "demographics") {
        return data["data"]["demographics"].some(
          (entry) => entry["name"] === catString
        );
      } else if (type === "studios") {
        return data["data"]["demographics"].some(
          (entry) => entry["name"] === catString
        );
      } else if (type === "source") {
        return data["data"]["studios"].some(
          (entry) => entry["name"] === catString
        );
      } else if (type === "Episodes") {
        if (catString === "50+") {
          const num = parseInt(catString.slice(0, 2));
          return data["data"]["episodes"] >= num;
        } else if (catString === "<=13") {
          const num = parseInt(catString.slice(2, 4));
          return data["data"]["episodes"] <= num;
        } else if (catString === ">=13") {
          const num = parseInt(catString.slice(2, 4));
          return data["data"]["episodes"] >= num;
        } else if (catString === ">=20") {
          const num = parseInt(catString.slice(2, 4));
          return data["data"]["episodes"] >= num;
        }
      } else if (type === "Year") {
        const split = catString.split(" - ");
        const year1 = split[0];
        const year2 = split[1];
        const startYear = data["data"]["prop"]["prop"]["year"];
        return year1 <= startYear && startYear <= year2;
      } else if (type === "Airing Status") {
        return catString === data["data"]["status"];
      } else if (type === "Mal Score") {
        const score = parseFloat(catString.slice(2, catString.length));
        return data["data"]["score"] >= score;
      } else if (type === "Mal Rank") {
        const split = catString.split(" - ");
        const rank1 = split[0];
        const rank2 = split[1];
        const guessRank = data["data"]["rank"];
        return rank1 <= guessRank && guessRank <= rank2;
      }

      return false;
    } catch (e) {
      console.error(e);
    }
  }
</script>

<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_noninteractive_element_interactions -->
{#if gameContext.imageUrls[gridTile - 1]}
  <img
    class="image"
    src={gameContext.imageUrls[gridTile - 1]}
    alt="Anime Thumbnail from myanimelist"
  />
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
