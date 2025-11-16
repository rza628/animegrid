<script>
  import { getContext } from "svelte";

  let { endShowModal = $bindable() } = $props();

  let dialog = $state(); // HTMLDialogElement

  let header = $state("");
  let desc = $state("");
  let gameContext = getContext("gameContext");

  $effect(() => {
    if (endShowModal) dialog.showModal();
    if (gameContext !== null) {
      header = "Game Done";
      desc = "Yeaaa";
    }
  });
</script>

<!--  consider adding links to sites explaining terms like Shounen -->
{#snippet info()}
  {#if gameContext !== null}
    <div class="infoBox">
      <div class="header">{header}</div>

      <div class="description">{desc}</div>
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
