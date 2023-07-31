<script>
	// @ts-nocheck
	import { onMount } from "svelte";
	import ManufacturerCard from './ManufacturerCard.svelte';
	let manufacturers = [];

	onMount( async () => {
		let data = await fetch('http://localhost:8000/manufacturers');
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