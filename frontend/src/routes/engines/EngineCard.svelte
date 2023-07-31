<script>
	  /**
	 * @type {{ id: any; make: any; model: any }}
	 */
	   export let engine;
</script>

<div class="ui segment">
	<a href={`/engines/${engine.id}`}>
		<p class="ui big header">{engine.make} {engine.model}</p>
	</a>
	<p>Planes:
		{#each engine.planes as plane}
		<a href={`/planes/${plane.id}`}> {plane.name} </a>
		{/each}
	</p>

</div>