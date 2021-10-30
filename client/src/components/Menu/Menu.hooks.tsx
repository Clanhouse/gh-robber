import { GoogleLogout, useGoogleLogout } from "react-google-login";
import useAuthUserContext from "../../context/Auth/useAuthUserContext";

const useLogout = () => {
  const [user, setUser] = useAuthUserContext();

  const userToken = user?.accessToken ?? "";

  useGoogleLogout({
    onFailure: () => console.error("fail"),
    clientId: userToken,
    onLogoutSuccess: () => logout(),
  });

  const logout = () => {
    setUser(null);
  };

  const GoogleLogoutButton = () => (
    <GoogleLogout
      clientId={userToken}
      buttonText="Logout"
      onLogoutSuccess={logout}
    />
  );

  return GoogleLogoutButton;
};

export default useLogout;
