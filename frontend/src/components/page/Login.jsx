import { Link } from 'react-router-dom'

import FormEntranceInput from '../UI/inputs/FormEntranceInput'


const LoginPage = () => {
    return (
        <div className="form">
            <form action="/" className="form__content">
            <h1>Login Form</h1>
            <FormEntranceInput type='text' placeholder='Enter Name' text='ENTER NAME'/>
            <FormEntranceInput type='email' placeholder='Enter Email' text='ENTER EMAIL'/>
            <div className="form__button">
                <input type="Submit" className="form__submit" value="Sign Up" readOnly />
            </div>
            <p><Link to='/register'>Register</Link></p>
            </form>
        </div>
    )
}

export default LoginPage