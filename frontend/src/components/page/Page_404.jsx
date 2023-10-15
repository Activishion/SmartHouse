import { gsap, Linear } from 'gsap'
import { useEffect, useRef } from "react"


const PageNotFound = () => {
    const cog1 = useRef()
    const cog2 = useRef()
    const wrong = useRef()

    useEffect(() => {
        gsap.to(cog1.current, {
            transformOrigin:"50% 50%",
            rotation:"+=360",
            repeat:-1,
            ease: Linear.easeNone,
            duration:8
        })

        gsap.to(cog2.current, {
            transformOrigin:"50% 50%",
            rotation:"-=360",
            repeat:-1,
            ease: Linear.easeNone,
            duration:8
        })

        gsap.fromTo(wrong.current, {
                opacity:0
            },
            {
                opacity:1,
                duration:1,
                stagger:{
                    repeat:-1,
                    yoyo:true
            }
        })
    })

    return (
        <>
        <div class="container">
            <h1 class="first-four">4</h1>
            <div class="cog-wheel1">
                <div class="cog1" ref={cog1}>
                    <div class="top"></div>
                    <div class="down"></div>
                    <div class="left-top"></div>
                    <div class="left-down"></div>
                    <div class="right-top"></div>
                    <div class="right-down"></div>
                    <div class="left"></div>
                    <div class="right"></div>
                </div>
            </div>
            
            <div class="cog-wheel2"> 
                <div class="cog2" ref={cog2}>
                    <div class="top"></div>
                    <div class="down"></div>
                    <div class="left-top"></div>
                    <div class="left-down"></div>
                    <div class="right-top"></div>
                    <div class="right-down"></div>
                    <div class="left"></div>
                    <div class="right"></div>
                </div>
            </div>
            <h2 class="second-four">4</h2>
            <p class="wrong-para" ref={wrong}>Page not found!</p>
        </div>
        </>
    )
}

export default PageNotFound