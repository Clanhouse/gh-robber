import { Wrapper, LoginWindow } from "./LogIn.styles";
import { LangLoggIn } from "../../i18n/ENG";
import { useLoginGoogle } from "./Login.hooks";

const Login = () => {
  const { mainLabel, secondLabel, googleButtonLabel } = LangLoggIn;

  const { GoogleLoginButton, GoogleErrorMessage } = useLoginGoogle();

  return (
    <Wrapper>
      <LoginWindow>
        <h1>{mainLabel}</h1>
        <p>{secondLabel}</p>
        <GoogleLoginButton label={googleButtonLabel} />
        <GoogleErrorMessage />
      </LoginWindow>
    </Wrapper>
  );
};

export default Login;
