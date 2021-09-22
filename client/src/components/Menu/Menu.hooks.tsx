import { GoogleLogout, useGoogleLogout } from "react-google-login";
import { useHistory } from "react-router";
import useAuthUserContext from "../../context/Auth/useAuthUserContext";

const useLogout = () => {
  const [_, setUser] = useAuthUserContext();
  const history = useHistory();

  const dummyGoogleClientID =
    "420218048324-i18dme6ipl1mj6jbjcra2ft4v83v26d4.apps.googleusercontent.com";

  const { signOut } = useGoogleLogout({
    onFailure: () => console.error("fail"),
    clientId: dummyGoogleClientID,
    onLogoutSuccess: () => logOut(),
  });

  const logOut = () => {
    signOut();
    setUser(null);
    history.push("/");
  };

  const GoogleLogoutButton = () => (
    <GoogleLogout
      clientId={dummyGoogleClientID}
      buttonText="Logout"
      onLogoutSuccess={logOut}
    />
  );

  return GoogleLogoutButton;
};

export default useLogout;
