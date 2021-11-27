import { ISearchState, ISearchAction } from "./Search.types";

const reducer = (state: ISearchState, action: ISearchAction) => {
  switch (action.type) {
    case "LOADING": {
      return {
        ...state,
        isLoading: true,
      };
    }
    case "LOADED": {
      return {
        ...state,
        values: action.payload,
        isLoading: false,
      };
    }
    case "ERROR": {
      return {
        ...state,
        error: action.payload,
        isLoading: false,
      };
    }
    default: {
      return state;
    }
  }
};

export default reducer;
