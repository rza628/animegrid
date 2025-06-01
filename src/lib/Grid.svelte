<script>
  let width = window.innerWidth;
  let height = window.innerHeight;
  let guessesLeft = $state(9);
</script>

<div class="main">
  <div class="acrossGrid">
    <div class="empty"></div>
    <button class="acrossTopic" aria-label="Close">topic 1</button>
    <button class="acrossTopic" aria-label="Close">topic 1</button>
    <button class="acrossTopic" aria-label="Close">topic 1</button>
  </div>
  <div class="rows">
    <div>
      <div class="grid">
        <button class="downTopic" aria-label="Close">topic 1</button>
        <button class="cell1" aria-label="Close"></button>
        <button class="cell2" aria-label="Close"></button>
        <button class="cell3" aria-label="Close"></button>
      </div>
      <div class="grid">
        <button class="downTopic" aria-label="Close">topic 1</button>
        <button class="cell4" aria-label="Close"></button>
        <button class="cell5" aria-label="Close"></button>
        <button class="cell6" aria-label="Close"></button>
      </div>
      <div class="grid">
        <button class="downTopic" aria-label="Close">topic 1</button>
        <button class="cell7" aria-label="Close"></button>
        <button class="cell8" aria-label="Close"></button>
        <button class="cell9" aria-label="Close"></button>
      </div>
    </div>
    <div class="guess">Guesses Left: {guessesLeft}</div>
  </div>
</div>

<style>
  .grid {
    display: grid;
    gap: 1px;
    grid-template-columns: repeat(4, 1fr);
    align-items: center;
  }

  .rows {
    display: flex;
    flex-direction: row;
  }

  button {
    width: 100px;
    height: 160px;
  }
  .acrossTopic {
    width: 100px;
    height: 50px;
    border: none;
    outline: none;
    background: none;
  }
  .downTopic {
    width: 100px;
    height: 50px;

    border: none;
    outline: none;
    background: none;
  }
  .empty {
    width: 100px;
    height: 50px;
    border: none;
    outline: none;
    background: none;
  }
  .main {
    margin: 0 auto;
  }
  .guess {
    width: 100px;
    height: 50px;
    align-self: center;
  }
</style>
