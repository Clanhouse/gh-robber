import { GoogleLoginResponse, GoogleLoginResponseOffline } from "react-google-login";

export const isOffline = (
  response: GoogleLoginResponse | GoogleLoginResponseOffline
): response is GoogleLoginResponseOffline => {
  return typeof response.code === "object";
};
