import { useReducer } from "react";
import { SearchWrapper } from "./Search.styles";

import SearchByView from "../SearchByView/SearchByView";

import reducer from "./Search.reducer";
import getConfig from "../../utils/getConfig";

const Search = () => {
  const [state, dispatch] = useReducer(reducer, {});

  const url = getConfig("REACT_APP_URL_USERS_REQUEST_users");

  const getUsers = async () => {
    try {
      const response = await fetch(url);
      const users = await response.json();
      console.log(users);
    } catch (err) {
      console.error(err);
    }
  };

  getUsers();

  return (
    <SearchWrapper>
      <p>Search for the users</p>
      <label htmlFor="searchType">Search Type</label>

      <label htmlFor="">User</label>
      <label htmlFor="">Repo</label>
      <input type="checkbox" name="searchType" id="searchType" />
      <SearchByView label={""} handleChange={() => {}} />
    </SearchWrapper>
  );
};

export default Search;
