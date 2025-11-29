<script>
  import { getContext } from "svelte";

  let { endShowModal = $bindable() } = $props();

  let dialog = $state(); // HTMLDialogElement

  let right = "☑️";
  let wrong = "✖️";

  let header = $state("");
  let desc = $state("");
  let gameContext = getContext("gameContext");
  let statsGrid = $derived.by(() => {
    let string = "";
    for (let i = 0; i < gameContext.imageUrls.length; i++) {
      string += gameContext.imageUrls[i] === null ? wrong : right;
      if ((i + 1) % 3 === 0) {
        string += "\n";
      }
    }
    return string;
  });
  $effect(() => {
    if (endShowModal) dialog.showModal();
    if (gameContext !== null) {
      header = "Game Done";
    }
  });
  function copyToClipBoard() {
    let strLit = `${gameContext.dateTimeString} AnimeGrid
${statsGrid}Scored ${gameContext.score} points`;
    navigator.clipboard.writeText(strLit);
  }
</script>

<!--  consider adding links to sites explaining terms like Shounen -->
{#snippet info()}
  {#if gameContext !== null}
    <div class="infoBox">
      <div class="header">{header}</div>

      <div class="description">
        <!-- points on correct guess unused guesses -->
        You earned {gameContext.score} points!
        {statsGrid}
      </div>
    </div>
  {/if}
{/snippet}

<dialog
  class="dialogBox"
  bind:this={dialog}
  onclose={() => (endShowModal = false)}
  onclick={(e) => {
    if (e.target === dialog) dialog.close();
  }}
>
  <div>
    <div class="buttons">
      {@render info()}
      <button onclick={() => copyToClipBoard()} class="close"
        >Copy To Share</button
      >
      <button onclick={() => dialog.close()} class="close">Close</button>
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
