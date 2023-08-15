<script>
	// @ts-nocheck
	import { page } from '$app/stores';
	import { onMount } from "svelte";
	import { configs } from '../../config.js';
	import AvionicCard from './AvionicCard.svelte';
	let avionics = [];

	onMount( async () => {
		let data = await fetch(configs.baseURL+$page.url.pathname);
		let avionicData = await data.json();
		avionics = [...avionicData];
	});
 
</script>

<svelte:head>
	<title>Avionics</title>
	<meta name="description" content="Avionics" />
</svelte:head>

<!-- <button on:click="{updateCost}" class="my-4 bg-pink-500 p-2 text-white">
	Change Price
  </button> -->
  {#each avionics as avionic}
  <AvionicCard {avionic} />
  {/each}