import React from "react";
import Nav from "./Nav";
import "../style/Base.scss";

export default function Base(props) {
  return (
    <div className="kindred-base">
      <Nav logout={props.logout} />
      <main className={props.className}>
        {props.children}
      </main>
    </div>
  )
}