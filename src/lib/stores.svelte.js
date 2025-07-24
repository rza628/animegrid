import { setContext } from "svelte";

let categories = $state({categories: []})
setContext('categoryContext', categories);

