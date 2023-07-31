<script>
	// @ts-nocheck
	import { onMount } from "svelte";
	import PlaneCard from './PlaneCard.svelte';
	let planes = [];

	onMount( async () => {
		let data = await fetch('http://localhost:8000/planes');
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