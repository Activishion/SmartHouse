


const FormEntranceInput = ({ type, placeholder, text }) => {
    return (
        <div className="form__box">
            <input type={type} className="form__input" placeholder={placeholder} />
            <label htmlFor="" className="form__label">{text}</label>
            <div className="form__shadow"></div>
        </div>
    )
}

export default FormEntranceInput