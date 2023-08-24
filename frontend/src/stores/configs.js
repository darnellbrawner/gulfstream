import { readable } from "svelte/store";

const configs = readable(
    { baseURL:'http://localhost:8000/api/v1' }
)
export default configs;