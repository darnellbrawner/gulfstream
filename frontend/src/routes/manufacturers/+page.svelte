<script>
	// @ts-nocheck
	import { page } from '$app/stores';
	import { onMount } from "svelte";
	import { fly } from 'svelte/transition';
	import { configs } from '../../config.js';
	import ManufacturerCard from './ManufacturerCard.svelte';
	import {Button, ButtonGroup, Offcanvas, Modal,
		 ModalBody, ModalFooter, ModalHeader, Input, Label, Table} from 'sveltestrap';

	let manufacturers = [];
	
	var addManufacturerForm = {
		id: '',
		name: '',
	};
	var editForm = {
		_id: '',
		name: '',
	};
	function editManufacturer(manufacturer) {
		updatetoggle();
		editForm = manufacturer; //manufacturer.manufacturer;
	};
	
	function updateManufacturer() {
		const payload = {
			id: editForm.id,
			name: editForm.name,
		};
		const path = configs.baseURL+$page.url.pathname+"/"+editForm.id;
		console.log(payload);
		fetch(path, {
			method: 'PATCH',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(payload)
		})
		.then(() => {
			getManufacturers();
		})
		.catch(error => {
			console.error('Error updating manufacturer:', error);
			getManufacturers();
		});
		updatetoggle();
	}

	 async function addManufacturer() {
		const payload = {
			id: null,
			name: addManufacturerForm.name,
		};
		const path = configs.baseURL+$page.url.pathname
		console.log(path)
		const response = await fetch(path,
		 {
			method: 'POST',
			headers: {'Content-Type': 'application/json', 'accept': 'application/json'},
			body: JSON.stringify(payload)
		})
		.then(() => {
			getManufacturers();
		})
		.catch(error => {
			console.log('Error adding manufacturer:', error);
			getManufacturers();
		});
		addtoggle();
	 }

	 function removeManufacturer(manufacturerID) {
		const path = configs.baseURL+$page.url.pathname+"/"+manufacturerID;
		console.log(path);
		fetch(path, {method: 'DELETE'})
		.then(() => {
			getManufacturers();
		})
		.catch(error => {
			console.error('Error deleting manufacturer:', error);
			getManufacturers();
		});
	 }

	function initForm() {
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

	onMount( async () => {
		let data = await fetch(configs.baseURL+$page.url.pathname);
		let manufacturerData = await data.json();
		manufacturers = [...manufacturerData];
	});
	
	function getManufacturers() {
		fetch(configs.baseURL+$page.url.pathname)
		.then(response => response.json())
		.then(data => {manufacturers = data;
		}).catch(error => console.error('Error fetching books:', error));

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
			<Button color="success" on:click={addtoggle}>Add Manufacturer</Button>
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
						<Button color="warning" on:click={editManufacturer(manufacturer)}>Update</Button>
						<Button color="danger" on:click={removeManufacturer(manufacturer.id)}>Delete</Button>
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
			<Button color="primary" on:click={addManufacturer}>
				Add manufacturer
			</Button>
			<Button color="secondary" on:click={addtoggle}>
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
			<Button color="primary" on:click={updateManufacturer}>
				Update
			</Button>
			<Button color="secondary" on:click={updatetoggle}>
				Cancel
			</Button>
		</ModalFooter>
	</Offcanvas>
</div>