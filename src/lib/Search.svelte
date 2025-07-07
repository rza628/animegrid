<script>
  let guess = $state("");
  let { animeTitles, value = $bindable(), searchTerm = $bindable() } = $props();
  let typingAgain = $state(true);

  let filteredTitles = $derived(
    animeTitles.filter((title) =>
      title["title"]
        .normalize("NFD")
        .replace(/\p{Diacritic}/gu, "")
        .toLowerCase()
        .includes(
          searchTerm
            .normalize("NFD")
            .replace(/\p{Diacritic}/gu, "")
            .toLowerCase()
        )
    )
  );

  function handleSearch(e) {
    e.preventDefault();
  }

  function selectedAnime(title) {
    searchTerm = title["title"];
    value = title["id"];
    typingAgain = false;
  }
  function handleTyping() {
    typingAgain = true;
  }
</script>

<form method="post" onsubmit={handleSearch} id="searchbar">
  <input
    bind:value={searchTerm}
    placeholder="Search Player"
    oninput={() => handleTyping()}
  />
</form>
<div class="suggestions">
  {#if searchTerm !== ""}
    {#each filteredTitles as title}
      {#if typingAgain}
        <div>
          <button onclick={() => selectedAnime(title)}>
            {title["title"]}</button
          >
        </div>
      {/if}
    {/each}
  {/if}
</div>

<style>
  .suggestions {
    overflow-y: auto;
    max-height: 15em;
  }
</style>
