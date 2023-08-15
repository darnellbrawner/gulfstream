<script>

	 /**
	 * @type {{ id: any; name: any; }}
	 */
	  export let manufacturer;

	//   function removeBook(bookID) {
	// 	const path = `/books/${currentdb}/${bookID.book._id}`;
	// 	axios.delete(path)
	// 		.then(() => {
	// 			getBooks();
	// 		})
	// 		.catch((error) => {
	// 			console.error(error);
	// 			getBooks();
	// 		});
	// };
</script>

<div class="ui segment"> 
	<p class="ui big header">
 <a href={`/manufacturers/${manufacturer.id}`}>
	{manufacturer.name}
 </a>
</p>
<p>
	<button>Edit</button> <button>Delete</button>
</p>
</div>