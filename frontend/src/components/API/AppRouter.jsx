import { Routes, Route } from "react-router-dom"

import Main from '../page/Main'
import LoginPage from '../page/Login'
import RegisterPage from '../page/Register'
import PageNotFound from "../page/Page_404"



const AppRouter = () => {
    return (
        <Routes>
            <Route exact path='/' element={<Main />} ></Route>
            <Route exact path='/login' element={<LoginPage />} ></Route>
            <Route exact path='/register' element={<RegisterPage />} ></Route>
            <Route path="*" element={<PageNotFound />}></Route>
        </Routes>
    )
}

export default AppRouter