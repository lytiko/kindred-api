import React from "react";
import { Link } from "react-router-dom";
import SignupForm from "../components/SignupForm";
import "../style/Landing.scss";


export default function Landing(props) {
  return (
    <div className="landing-page">
      <h2>Violent checklists.</h2>
      <SignupForm login={props.login}/>
      <p>Or <Link to="/login/">sign in</Link>.</p>
    </div>
  )
}