const getConfig = (key: string): string => {
  const envVar = process.env[key];
  if (!envVar) {
    throw new Error("This key is not defined.");
  }

  return envVar;
};

export default getConfig;
