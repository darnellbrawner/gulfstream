<script>
	// @ts-nocheck
	import { page } from '$app/stores';
	import { onMount } from "svelte";
	import { configs } from '../../../config.js';
	import ManufacturerCard from '../ManufacturerCard.svelte';
	let manufacturers = [];

	onMount( async () => {
		let data = await fetch(configs.baseURL+$page.url.pathname);
		let manufacturerData = await data.json();
		manufacturers = [...manufacturerData];
	});
 
</script>

<svelte:head>
	<title>Planes</title>
	<meta name="description" content="manufacturers" />
</svelte:head>

  {#each manufacturers as manufacturer}
  <ManufacturerCard {manufacturer} />
  {/each}