<script>
  let searchTerm = $state("");
  let { animeTitles } = $props();

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
</script>

<form method="post" onsubmit={handleSearch} id="searchbar">
  <input bind:value={searchTerm} placeholder="Search Player" />
</form>
{#if searchTerm !== ""}
  {#each filteredTitles as title}
    <div>
      <button> {title["title"]}</button>
    </div>
  {/each}
{/if}
