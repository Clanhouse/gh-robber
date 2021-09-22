export type IGoogleError = {
  error: string;
  details: string;
};

export type IErrorGoogleLogin = IGoogleError | null;

export type IGoogleLoginButtonProps = {
  label?: string;
};
