import React from "react";
import { Link } from "react-router-dom";
import "../style/Nav.scss";

export default function Nav(props) {
  return (
    <nav>
      <Link to="/" className="logo">kindred</Link>
      <div className="logout" onClick={props.logout} >Log Out</div>
    </nav>
  )
}