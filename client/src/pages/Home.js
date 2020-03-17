import React from "react";
import Base from "../components/Base";
import "../style/Home.scss";

export default function Home(props) {

  return (
    <Base className="home-page" logout={props.logout} >
      kindred
    </Base>
  )
}