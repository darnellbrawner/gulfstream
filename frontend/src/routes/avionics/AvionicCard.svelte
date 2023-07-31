<script>

	   /**
	 * @type {{ id: any; name: any; planes: any; }}
	 */
	    export let avionic;
</script>

<div class="ui segment">
	<a href={`/avionics/${avionic.id}`}>
		<p class="ui big header">{avionic.name}</p>
	</a>
	<p>Planes:
		{#each avionic.planes as plane}
		<a href={`/planes/${plane.id}`}> {plane.name} </a>
		{/each}
	</p>

</div>