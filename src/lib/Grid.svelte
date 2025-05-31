<div class="grid">
  <div class="cell1"></div>
  <div class="cell2"></div>
  <div class="cell3"></div>
  <div class="cell4"></div>
  <div class="cell5"></div>
  <div class="cell6"></div>
  <div class="cell7"></div>
  <div class="cell8"></div>
  <div class="cell9"></div>
</div>

<style>
.grid {
  display: grid;
  gap: 1px;
  grid-template-columns: repeat(3, 1fr);
}

div > div {
  padding: 100px;
  background-color: #ccc;
}
</style>