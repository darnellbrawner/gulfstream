<script>

	 /**
	 * @type {{ id: any; name: any; }}
	 */
	  export let manufacturer;
</script>

<div class="ui segment">
 <a href={`/manufacturers/${manufacturer.id}`}>
	 <p class="ui big header">{manufacturer.name}</p>
 </a>

</div>