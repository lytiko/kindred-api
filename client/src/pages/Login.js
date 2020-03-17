import React, { useState } from "react";
import { Link, withRouter } from "react-router-dom";
import { getApiLocation } from "../api";
import "../style/Login.scss";

function Login(props) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleEmailChange = event => {
    setEmail(event.target.value);
  }

  const handlePasswordChange = event => {
    setPassword(event.target.value);
  }

  const login = (event) => {
    event.preventDefault();
    fetch(`${getApiLocation()}login/`, {
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
    <div className="login-page">
      <Link to="/" className="logo">Kindred</Link>
      {error && <div className="error">{error}</div>}
      <form className="login-form" onSubmit={login}>
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
        <input type="submit" value="Log In" />
      </form>
    </div>
  )
}

export default withRouter(Login);