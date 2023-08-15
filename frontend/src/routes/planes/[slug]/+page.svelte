<script>
	// @ts-nocheck
	import { page } from '$app/stores';
	import { onMount } from "svelte";
	import { configs } from '../../../config.js';
	import PlaneCard from '../PlaneCard.svelte';
	let planes = [];
	
	onMount( async () => {
		let data = await fetch(configs.baseURL+$page.url.pathname);
		let planeData = await data.json();
		planes = [...planeData];
	});
 
</script>

<svelte:head>
	<title>Planes</title>
	<meta name="description" content="Planes" />
</svelte:head>

  {#each planes as plane}
  <PlaneCard {plane} />
  {/each}