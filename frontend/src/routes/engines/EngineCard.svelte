<script>
	  /**
	 * @type {{ id: any; make: any; model: any }}
	 */
	   export let engine;
</script>

<div class="ui segment">
	
		<p class="ui big header">
			<a href={`/engines/${engine.id}`}>{engine.make} {engine.model}</a>
		</p>

	<p>Planes:
		{#each engine.planes as plane}
		<a href={`/planes/${plane.id}`}> {plane.name} </a>
		{/each}
	</p>

</div>