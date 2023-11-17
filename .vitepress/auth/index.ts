import config from "./auth_config";
import { createAuth0Client } from "@auth0/auth0-spa-js";

let createClient = async () => {
  let auth0Client = await createAuth0Client({
    domain: config.domain,
    clientId: config.cliendId,
  });
  return auth0Client;
};

let loginWithPopup = async (client, options) => {
  try {
    await client.loginWithPopup(options);
  } catch (e) {
    console.error(e);
  }
};

let logout = (client) => {
  return client.logout();
};

const auth = {
  createClient,
  loginWithPopup,
  logout,
};

export default auth;
