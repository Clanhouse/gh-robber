import { FunctionComponent, useState } from "react";
import GoogleLogin, {
  GoogleLoginResponse,
  GoogleLoginResponseOffline,
} from "react-google-login";
import { useHistory } from "react-router-dom";
import {
  IErrorGoogleLogin,
  IGoogleError,
  IGoogleLoginButtonProps,
} from "./Login.types";
import { isOffline } from "./Login.utils";
import useAuthUserContext from "../../context/Auth/useAuthUserContext";

export const useLoginGoogle = () => {
  const [error, setError] = useState<IErrorGoogleLogin>(null);

  const [_, setUser] = useAuthUserContext();
  const history = useHistory();

  const dummyClientID =
    "420218048324-i18dme6ipl1mj6jbjcra2ft4v83v26d4.apps.googleusercontent.com";

  const onSuccess = (response: GoogleLoginResponse | GoogleLoginResponseOffline) => {
    if (isOffline(response)) {
      throw new Error("Your device is currently offline. Please try again later.");
    }

    const {
      profileObj: { email, name },
      googleId,
      accessToken,
    } = response;

    setUser({
      userEmail: email,
      userID: googleId,
      userName: name,
      accessToken: accessToken,
    });
    history.push("/dashboard");
  };

  const onFailure = (error: IGoogleError) => {
    setError(error);
  };

  const GoogleLoginButton: FunctionComponent<IGoogleLoginButtonProps> = ({
    label,
  }) => {
    return (
      <>
        <GoogleLogin
          clientId={dummyClientID}
          buttonText={label ?? "Login with Google"}
          onSuccess={onSuccess}
          onFailure={onFailure}
          onRequest={() => setError(null)}
          isSignedIn={true}
        />
      </>
    );
  };

  const GoogleErrorMessage: FunctionComponent = () => error && <p>{error.error}</p>;

  return { GoogleLoginButton, GoogleErrorMessage };
};
