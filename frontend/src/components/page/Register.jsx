import { Link } from 'react-router-dom'

import FormEntranceInput from '../UI/inputs/FormEntranceInput'


const RegisterPage = () => {
    return (
        <div className="form">
            <form action="/" className="form__content">
            <h1>Register Form</h1>
            <FormEntranceInput type='text' placeholder='Enter Name' text='ENTER NAME'/>
            <FormEntranceInput type='email' placeholder='Enter Email' text='ENTER EMAIL'/>
            <div className="form__button">
                <input type="Submit" className="form__submit" value="Sign Up" readOnly />
            </div>
            <p><Link to='/login'>Login</Link></p>
            </form>
        </div>
    )
}

export default RegisterPage