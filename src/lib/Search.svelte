<script>
  let { value = $bindable(), searchTerm = $bindable() } = $props();
  let typingAgain = $state(true);
  let filteredTitles = $state([]);

  function handleSearch(e) {
    e.preventDefault();
  }

  function selectedAnime(title) {
    searchTerm = title["title"];
    value = title["id"];
    typingAgain = false;
  }
  let timer;
  function debounce() {
    typingAgain = true;
    clearTimeout(timer);
    timer = setTimeout(async () => {
      const res = await fetch(
        `https://animegrid-backend-1.onrender.com/api/search/${searchTerm.toLowerCase()}`
      );
      const data = await res.json();
      filteredTitles = data["data"];
    }, 300);
  }
</script>

<form method="post" onsubmit={handleSearch} id="searchbar">
  <input
    id="searchbar"
    bind:value={searchTerm}
    placeholder="Search Anime"
    oninput={() => debounce()}
    autocomplete="off"
  />
</form>
<div class="suggestions">
  {#if searchTerm !== ""}
    {#each filteredTitles as title}
      {#if typingAgain}
        <div>
          <button onclick={() => selectedAnime(title)} class="suggestion">
            {title["title"]}</button
          >
        </div>
      {/if}
    {/each}
  {/if}
</div>

<style>
  .suggestion {
    max-width: 200px;
  }
  input::placeholder {
    text-align: center;
  }
  #searchbar {
    display: flex;
    flex: 1;
  }
  .suggestions {
    overflow-y: auto;
    max-height: 15em;
  }
</style>
