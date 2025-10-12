<script>
  let { categoryInfo, showModal = $bindable() } = $props();

  let dialog = $state(); // HTMLDialogElement

  let header = $state("");
  let desc = $state("");

  $effect(() => {
    if (showModal) dialog.showModal();
    if (categoryInfo !== null) {
      if (categoryInfo["type"] === "genres") {
        header = "Genre";
        desc = "This is the genre of the anime as labeled on myanimelist.net";
      } else if (categoryInfo["type"] === "demographics") {
        header = "Demographic";
        desc = `This is the audience the anime is made for as labeled  on myanimelist.net 
        The choices are: Shounen, Seinen, Shoujo, Josei, and Kids`;
      } else if (categoryInfo["type"] === "source") {
        header = "Source";
        desc = `The source material the anime was adapted from.
        The options are: 
        Manga, Visual Novel, Light Novel, Novel, Original, Music, Web Manga, 4-koma Manga, Web Novel, Game, Other, Book, Mixed Media, or Picture Book. `;
      } else if (categoryInfo["type"] === "Episodes") {
        header = "Episodes";
        desc = `The total number of episodes the anime has when it ended.
      Note: myanimelist.net has different seasons of anime listed with their own episode count. Also, currently airing anime have an episode count of Unknown on the site, so only choose anime/anime seasons that have finished airing!`;
      } else if (categoryInfo["type"] === "Year") {
        header = "Year";
        desc = `This is the year the anime STARTED airing, not when it started and completed it's run in this range. Also, the range includes both the start and end years
      Example: If the range is 2000 - 2005, an anime that started airing in 2000, in between, or in 2005 is valid.`;
      } else if (categoryInfo["type"] === "Airing Status") {
        header = "Airing Status";
        desc = `If an anime is currently airing or it has finished airing.`;
      } else if (categoryInfo["type"] === "Mal Score") {
        header = "Mal Score";
        desc = `The Mal Score is the average rating of the users of that anime on myanimelist.net`;
      }
    }
  });
</script>

<!--  consider adding links to sites explaining terms like Shounen -->
{#snippet info()}
  {#if categoryInfo !== null}
    <div class="infoBox">
      <div class="header">{header}</div>

      <div class="description">{desc}</div>
    </div>
  {/if}
{/snippet}

<dialog
  class="dialogBox"
  bind:this={dialog}
  onclose={() => (showModal = false)}
  onclick={(e) => {
    if (e.target === dialog) dialog.close();
  }}
>
  <div>
    <div class="buttons">
      {@render info()}
      <button onclick={() => dialog.close()} class="close">close modal</button>
    </div>
  </div>
</dialog>

<style>
  .infoBox {
    width: 450px;
    height: 175px;
  }
  .description {
    white-space: pre-line;
  }
  .header {
    border-bottom-width: 1px;
    border-color: grey;
    border-bottom-style: dashed;
  }

  .buttons {
    display: flex;
    flex-direction: column;
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
