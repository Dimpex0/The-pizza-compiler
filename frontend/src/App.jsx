import {createBrowserRouter, RouterProvider} from "react-router-dom";
import RootPage from "./pages/Root/Root.jsx";
import LoginPage from "./pages/auth/Login/Login.jsx";
import HomePage from "./pages/Home/Home.jsx";
import RegisterPage from "./pages/auth/Register/Register.jsx";

export default function App() {

  const router = createBrowserRouter([
    {path: '/', element: <RootPage />,
      children: [
        {path: '', element: <HomePage />},
        {path: 'login', element: <LoginPage />},
        {path: 'register', element: <RegisterPage />}
      ]
    }
  ])

  return (
    <RouterProvider router={router} />
  )
}
