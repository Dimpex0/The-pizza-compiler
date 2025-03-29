import {createBrowserRouter, RouterProvider} from "react-router-dom";
import RootPage from "./pages/Root/Root.jsx";
import LoginPage from "./pages/auth/Login/Login.jsx";
import HomePage from "./pages/Home/Home.jsx";

export default function App() {

  const router = createBrowserRouter([
    {path: '/', element: <RootPage />,
      children: [
        {path: '', element: <HomePage />},
        {path: 'login', element: <LoginPage />},
      ]
    }
  ])

  return (
    <RouterProvider router={router} />
  )
}
