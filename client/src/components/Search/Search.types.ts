export type ISearchState = {
  values?: unknown;
  error?: unknown;
  isLoading?: boolean;
};

export type ISearchAction =
  | {
      type: "LOADING";
    }
  | {
      type: "LOADED";
      payload: unknown;
    }
  | {
      type: "ERROR";
      payload: unknown;
    };
