// TODO file for generic CRUD actions

import { 
    addData,
    deleteData, 
    getData, 
    updateData } from './api_calls.js'

export let updateopen = false;
export let addopen = false;

export let addManufacturerForm = { id: null, name: '' };
export let editForm = {_id: '', name: '' };

/**
 * @type {never[]}
 */
export let turers = [];

export function initForm() {
    addManufacturerForm.id = null;
    addManufacturerForm.name = '';
    editForm._id = '';
    editForm.name = '';
};

export function addtoggle() {
    initForm();
    addopen = !addopen;
};

export function updatetoggle() {
    initForm();
    updateopen = !updateopen;
};

//READ
/**
 * @param {string} msg
 * @param {string} path
 */
export function reload(path, msg) {
    getData(path)
    .then(function (data) { manufacturers = data } )
    .then(() => { console.log(msg)} )
    .then(()=>{console.log(manufacturers)})
    .catch((reason) => console.log("Message: " + reason.message ));
}

//UPDATE
/**
 * @param {string} path
 * @param {JSON} payload
 */
export function update(path, payload) {
   // const patchPath = getPath+"/"+editForm.id;
    updateData(path, payload)
    .then(() => { reload(path, 'update') });
    updatetoggle();
}

//ADD
/**
 * @param {string} path
 * @param {any} form
 */
export function add(path, form) {
    form.id = null;
    addData(path, form)
    .then(()=>{ reload(path, 'add') });
    addtoggle();
 }

//DELETE
 /**
 * @param {string} path
 * @param {string} id
 */
 export function remove(path, id) {
    deleteData(path+"/"+id)
    .then(() => { reload(path, 'remove') });
 }

