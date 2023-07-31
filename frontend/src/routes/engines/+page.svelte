<script>
	// @ts-nocheck
	import { onMount } from "svelte";
	import EngineCard from './EngineCard.svelte';
	let engines = [];

	onMount( async () => {
		let data = await fetch('http://localhost:8000/engines');
		let engineData = await data.json();
		engines = [...engineData];
	});

</script>

<svelte:head>
	<title>Engines</title>
	<meta name="description" content="Engines" />
</svelte:head>

<!-- <button on:click="{updateCost}" class="my-4 bg-pink-500 p-2 text-white">
	Change Price
  </button> -->
  {#each engines as engine}
  <EngineCard {engine} />
  {/each}