<script>
	 /**
	 * @type {{ id: any; name: any; max_range: any; max_range_unit: any; high_speed_cruise: any; cruising_unit: any; long_range_cruise: any; living_areas_max: any; window_count: any; window: { size: any; shape: any; }; avionic: { name: any; }; engine_count: any; engine: { make: any; model: any; }; }}
	 */
	  export let plane;
</script>

<div class="ui segment">
	<a href={`/planes/${plane.id}`}>
		<p class="ui big header">
			<a href={`/planes/${plane.id}`}>{plane.name}</a>
		</p>
	</a>
	<div class="row">
		<div class="column">
			<p class="ui big header">Performance</p>
			<p>{ plane.max_range} { plane.max_range_unit}: Max Range</p>
			<p>{ plane.high_speed_cruise } { plane.cruising_unit }: High Speed Cruise</p>
			<p>{ plane.long_range_cruise } { plane.cruising_unit }: Long Range Cruise</p>
		</div>
		<div class="column">
			<p class="ui big header">Cabin</p>
			<p>Up to { plane.living_areas_max }: Living Area</p>
			<p>{ plane.window_count}: {plane.window.size } { plane.window.shape } Window</p>
		</div>
		<div class="column">
			<p class="ui big header">Systems</p>
			<p><a href={`/avionics/${plane.avionic.id}`}>{ plane.avionic.name}</a> : Avionics</p>
			<p>
					{ plane.engine_count} x 
					<a href={`/engines/${plane.engine.id}`}>
						{ plane.engine.make } { plane.engine.model }
					</a> : Engines
			</p>

		</div>
	</div>
	<div class="row">
        <!-- <button on:click={(e) => deletePlane(plane)}>Delete</button> -->
	</div>
</div>