import {useState} from "react";

import {api} from "../../../utils/api.js";

export default function LoginPage() {
    const [formData, setFormData] = useState({
        'email': "",
        'password': '',
    })

    function handleInputChange(e) {
        setFormData(prevState => ({
            ...prevState,
            [e.target.name]: e.target.value
        }))
    }

    function handleSubmit() {
        api.post("account/login", formData)
            .then(res => console.log(res.data))
    }

    return <>
        <h1>Login</h1>
        <input onChange={handleInputChange} name="email" placeholder="Email..." value={formData.email} />
        <input onChange={handleInputChange} name="password" placeholder="Password..." value={formData.password} />
        <button onClick={handleSubmit}>Login</button>
    </>
}