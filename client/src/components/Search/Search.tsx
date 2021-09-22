import React, { useReducer } from "react";
import { SearchWrapper } from "./Search.styles";

import SearchByView from "../SearchByView/SearchByView";

import {
  LangSearch,
  LangSearchByRepoView,
  LangSearchByUserView,
} from "../../i18n/ENG";
import reducer from "./Search.reducer";

const Search = () => {
  const [state, dispatch] = useReducer(reducer, {});

  const url = process.env.REACT_APP_URL_USERS_REQUEST_users as string;

  const { searchBy, toggleSwitchLabelFirst, toggleSwitchLabelSecond, submitButton } =
    LangSearch;
  const { repositoryName, technology, minStarsCount, maxStarsCount } =
    LangSearchByRepoView;
  const { githubNick, minRepoCount, maxRepoCount } = LangSearchByUserView;

  return (
    <SearchWrapper>
      <p>{searchBy}</p>
      <label htmlFor="searchType">Search Type</label>

      <label htmlFor="">User</label>
      <label htmlFor="">Repo</label>
      <input type="checkbox" name="searchType" id="searchType" />
      {<SearchByView label={""} handleChange={() => {}} />}
    </SearchWrapper>
  );
};

export default Search;
