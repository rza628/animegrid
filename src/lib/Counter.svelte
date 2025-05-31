<script>
  let count = $state(10);
  const increment = () => {
    count += 1;
  };
</script>

<button onclick={increment}>
  count is {count}
</button>
