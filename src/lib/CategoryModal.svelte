<script>
  let { categoryInfo, showModal = $bindable() } = $props();

  let dialog = $state(); // HTMLDialogElement

  $effect(() => {
    if (showModal) dialog.showModal();
  });
</script>

<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_noninteractive_element_interactions -->

{#snippet info()}
  {#if categoryInfo !== null}
    <div class="infoBox">
      <div>{categoryInfo["type"]}</div>
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
    width: 300px;
    height: 175px;
  }
  .image {
    width: 100px;
    height: 160px;
    text-align: center;
    border-radius: 8px;
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
