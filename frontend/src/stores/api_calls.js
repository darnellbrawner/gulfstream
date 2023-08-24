/**
 * @param {RequestInfo | URL} getPath
 */
 //function getData(path, target_name) {
//READ
export const getData = async (getPath) => {
		var response = await fetch(getPath, 
            {  method: 'GET' }
            );
		let result = await response.json();
		return result;
	}
/**
 * 
 * @param {string} patchPath 
 * @param {JSON} payload 
 */    
// UPDATE
export const updateData = async (patchPath, payload) => {
    let response = await fetch(patchPath, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
    return response;
}
/**
 * 
 * @param {string} path 
 * @param {JSON} payload 
 */
// CREATE
export async function addData(path, payload) {
     await fetch(path, {
        method: 'POST',
        headers: {'Content-Type': 'application/json', 'accept': 'application/json'},
        body: JSON.stringify(payload)
       });
}
/**
 * 
 * @param {string} deletePath 
 */
// DELETE
export const deleteData = async (deletePath) => {
    let response = await fetch(deletePath, {method: 'DELETE' });
    return response 
}

