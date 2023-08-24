<script>
	// @ts-nocheck
	import { page } from '$app/stores';
	import { onMount } from "svelte";
	import { fly } from 'svelte/transition';
	import { configs } from '../../config.js';
	import { addData, deleteData, getData, updateData } from '../../stores/api_calls.js'
	//import ManufacturerCard from './ManufacturerCard.svelte';
	import {Button, ButtonGroup, Offcanvas,
		 ModalBody, ModalFooter, ModalHeader, Input, Label, Table} from 'sveltestrap';

	export let manufacturers = []

	$: onDataChange(manufacturers);

	const getPath = configs.baseURL+$page.url.pathname;

	var addManufacturerForm = { id: null, name: '' };
	var editForm = {_id: '', name: '' };

	function onDataChange(manufacturers){
		console.log('onDataChange:', manufacturers);
	}

	onMount( async () => {
		getData(getPath)
		.then((data) => manufacturers = data)
		.catch((reason) => console.log("Message: " + reason.message ));
	});

	function refreshData(msg) {
		getData(getPath)
		.then(function (data) { manufacturers = data } )
		.then(console.log(msg))
		.catch((reason) => console.log("Message: " + reason.message ));
	}

	function editManufacturer(manufacturer) {
		updatetoggle();
		editForm = manufacturer; 
	};
	
	function updateManufacturer() {
		const payload = { 
			id: editForm.id,
			name: editForm.name
		};
		const patchPath = getPath+"/"+editForm.id;
		updateData(patchPath, payload)
		.then(() => { refreshData('update') });
		updatetoggle();
	}

	function  addManufacturer() {
		addManufacturerForm.id = null;
		addData(getPath, addManufacturerForm)
		.then(()=>{ refreshData('add') });
		addtoggle();
	 }

	 function removeManufacturer(manufacturerID) {
		let removePath = getPath+"/"+manufacturerID
		deleteData(removePath)
		.then(() => { refreshData('remove') });
	 }

	function initForm() {
		addManufacturerForm.id = '';
		addManufacturerForm.name = '';
		editForm._id = '';
		editForm.name = '';
	};

	let addopen = false;

	function addtoggle() {
		initForm();
		addopen = !addopen;
	};

	let updateopen = false;

	function updatetoggle() {
		initForm();
		updateopen = !updateopen;
	};

</script>

<svelte:head>
	<title>Planes</title>
	<meta name="description" content="manufacturers" />
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">

</svelte:head>
<div>
	<div class="row">
		<div class="col-sm-12">
			<h1>Manufacturers</h1>
			<hr><br>
			<Button color="success" outline on:click = {() => addtoggle()}> Add Manufacturer</Button>
			<Button color="success" outline on:click = {() => refreshData('refresh')} > Refresh Manufacturer</Button>
			<br><br>
			<Table hover>
				<thead>
					<tr>
						<th scope="col">Name</th>
						<th></th>
					</tr>
				</thead>
				<tbody>
				{#each manufacturers as manufacturer}
				<tr transition:fly="{{ y: 48, duration: 200 }}">
					<td>{ manufacturer.name }</td>
					<td>{ manufacturer.id }</td>
					<td><span style="float: right;">
						<Button color="warning" on:click={() => editManufacturer(manufacturer)}>Update</Button>
						<Button color="danger" on:click={() =>  removeManufacturer(manufacturer.id)}>Delete</Button>
						</span>
					</td>
				</tr>
				{/each}
        </tbody>
      </Table>
    </div>
  </div>
	<Offcanvas isOpen={addopen} {addtoggle}>
		<ModalHeader {addtoggle}>Add a new manufacturer</ModalHeader>
		<ModalBody>
		  <Label for="newTitle">Name:</Label>
		  <Input type="text" bind:value={addManufacturerForm.name} placeholder="manufacturer name"/>
			<p></p>
		</ModalBody>
		<ModalFooter>
			<Button color="primary" on:click={() => addManufacturer()}>
				Add manufacturer
			</Button>
			<Button color="secondary" on:click={() => addtoggle()}>
				Cancel
			</Button>
		</ModalFooter>
	</Offcanvas>
	<Offcanvas isOpen={updateopen} {updatetoggle}>
		<ModalHeader {updatetoggle}>Update Manufacturer</ModalHeader>
		<ModalBody>
			<Label for="newTitle">Name:</Label>
			<Input type="text" bind:value={editForm.name} placeholder="manufacturer name"/>
			<p></p>
		</ModalBody>
		<ModalFooter>
			<Button color="primary" on:click={() => updateManufacturer()}>
				Update
			</Button>
			<Button color="secondary" on:click={() => updatetoggle()}>
				Cancel
			</Button>
		</ModalFooter>
	</Offcanvas>
</div>