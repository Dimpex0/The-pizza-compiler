import {useState} from "react";

import {regularApi} from "../../../utils/api.js";

export default function LoginPage() {
    const [formData, setFormData] = useState({
        'email': "",
        'password': '',
    });
    const [errorMessage, setErrorMessage] = useState("");

    function handleInputChange(e) {
        setFormData(prevState => ({
            ...prevState,
            [e.target.name]: e.target.value
        }))
    }

    function handleSubmit() {
        regularApi.post("account/login", formData)
            .then(() => setErrorMessage(""))
            .catch(error => {
                const message = error.response?.data?.message || undefined;

                if (message) {
                    setErrorMessage(message);
                    return;
                }
                setErrorMessage("Server error. Please try again.");
            })
    }

    return <>
        <h1>Login</h1>
        <p>{errorMessage}</p>
        <input onChange={handleInputChange} name="email" placeholder="Email..." value={formData.email} />
        <input onChange={handleInputChange} name="password" placeholder="Password..." value={formData.password} />
        <button onClick={handleSubmit}>Login</button>
    </>
}