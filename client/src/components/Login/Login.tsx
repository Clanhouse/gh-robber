import { useLoginGoogle } from "./Login.hooks";

const Login = () => {
  const { GoogleLoginButton, GoogleErrorMessage } = useLoginGoogle();

  return (
    <div>
      <form>
        <h1>Login to your account.</h1>
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          name="email"
          id="email"
          placeholder="johndoe@example.com"
          required
          aria-required
        />
        <label htmlFor="password">Password:</label>
        <input
          type="password"
          name="password"
          id="password"
          placeholder="At least 6 characters long."
          required
          aria-required
        />
        <input type="checkbox" name="rememberPassword" id="rememberPassword" />
        <label htmlFor="rememberPassword">Remember me</label>
        <button>Forgot password?</button>
        <button type="submit">Login</button>
      </form>
      <GoogleLoginButton label={"Sign in with Google"} />
      <GoogleErrorMessage />
    </div>
  );
};

export default Login;
