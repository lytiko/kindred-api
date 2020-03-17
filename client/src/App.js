import React, { useState } from "react";
import { BrowserRouter } from "react-router-dom";
import { Route } from "react-router";
import { ApolloLink } from "apollo-link";
import { InMemoryCache } from "apollo-cache-inmemory";
import { createHttpLink } from "apollo-link-http";
import ApolloClient from "apollo-client";
import { ApolloProvider } from "react-apollo";
import { getApiLocation } from "./api";
import Landing from "./pages/Landing";
import Login from "./pages/Login";
import Home from "./pages/Home";

export default function App() {
  const [loggedIn, setLoggedIn] = useState(Boolean(localStorage.getItem("token")));

  const authLink = new ApolloLink((operation, forward) => {
    operation.setContext(({ headers }) => ({ headers: {
      authorization: localStorage.getItem("token"), ...headers
    }}));
    return forward(operation);
  });
  const httpLink = createHttpLink({ uri: getApiLocation() });
  const link = ApolloLink.from([authLink, httpLink]);
  const client = new ApolloClient({
    cache: new InMemoryCache(), link: link
  });

  const login = (token, history) => {
    localStorage.setItem("token", token);
    history.push("/");
    setLoggedIn(true);
  }
  
  const logout = () => {
    localStorage.removeItem("token");
    client.resetStore();
    setLoggedIn(false);
  }

  return (
    <ApolloProvider client={client}>
      <BrowserRouter>
        <Route path="/" exact>
          {loggedIn ? <Home logout={logout} /> : <Landing login={login}/>}
        </Route>
        <Route path="/login/" exact>
          <Login login={login} />
        </Route>
      </BrowserRouter>
    </ApolloProvider>
  );
}