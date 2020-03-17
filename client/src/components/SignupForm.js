import React, { useState } from "react";
import { withRouter } from "react-router-dom";
import { getApiLocation } from "../api";
import "../style/SignupForm.scss";

function SignupForm(props) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleEmailChange = event => {
    setEmail(event.target.value);
  }

  const handlePasswordChange = event => {
    setPassword(event.target.value);
  }

  const signup = (event) => {
    event.preventDefault();
    fetch(`${getApiLocation()}signup/`, {
      method: "POST",
      headers: {"Content-Type": "text/plain"},
      body: JSON.stringify({email, password})
    }).then((response) => {
      if (response.status === 200) {
        response.json().then(json => {
          props.login(json.message, props.history);
        })
      } else {
        response.json().then(json => {
          for (let key in json.error) {
            setError(json.error[key]);
          }
        });
      }
    }).catch(() => {
      setError("Could not connect - please try again shortly.");
    });
  }

  return (
    <form className="signup-form" onSubmit={signup} >
      {error && <div className="error">{error}</div>}
      <label>Email</label>
      <input
        id="email"
        name="email"
        autoComplete="off"
        value={email}
        onChange={handleEmailChange}
        required 
      />
      <label>Password</label>
      <input
        id="password"
        name="password"
        type="password"
        autoComplete="off"
        value={password}
        onChange={handlePasswordChange}
        required
      />
      <input type="submit" value="Sign Up" />
    </form>
  )
}

export default withRouter(SignupForm);