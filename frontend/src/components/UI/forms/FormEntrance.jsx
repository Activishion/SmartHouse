import FormEntranceInput from '../inputs/FormEntranceInput'


const FormEntrance = () => {
    return (
        <div className="form">
            <form action="/" className="form__content">
            <h1>Register Form</h1>
            <FormEntranceInput type='text' placeholder='Enter Name' text='ENTER NAME'/>
            <FormEntranceInput type='email' placeholder='Enter Email' text='ENTER EMAIL'/>
            <div className="form__button">
                <input type="Submit" className="form__submit" value="Sign Up" readOnly />
            </div>
            </form>
        </div>
    )
}

export default FormEntrance