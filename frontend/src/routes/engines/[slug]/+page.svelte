<script>
	// @ts-nocheck
	import { page } from '$app/stores';
	import { onMount } from "svelte";
	import { configs } from '../../../config.js';
	import EngineCard from '../EngineCard.svelte';
	let engines = [];

	onMount( async () => {
		let data = await fetch(configs.baseURL+$page.url.pathname);
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