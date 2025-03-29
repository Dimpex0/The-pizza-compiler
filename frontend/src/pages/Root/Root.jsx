import {Outlet} from "react-router-dom";

export default function RootPage() {
    return <>
        <h1>Root</h1>
        <Outlet />
    </>
}