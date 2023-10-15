import AppRouter from "../API/AppRouter"
import Header from './Header'
import Footer from './Footer'


const Body = () => {
    const currentUrl = window.location.href

    return (
        <>
            {currentUrl !== 'http://localhost:3000/login'
                ? <Header />
                : null
            }
            
            <AppRouter />
            {currentUrl !== 'http://localhost:3000/login'
                ? <Footer />
                : null
            }
        </>
    )
}

export default Body