import { FunctionComponent } from "react";
import Dropdown from "../Dropdown/Dropdown";
import { ISearchByViewProps } from "./SearchByView.types";

const SearchByView: FunctionComponent<ISearchByViewProps> = ({
  label,
  handleChange,
}) => {
  const minValue = 0;
  const maxValue = 10;
  const step = 1;

  return (
    <div>
      <label htmlFor={label}>{label}</label>
      <input
        id={label}
        type="text"
        placeholder={label}
        onChange={handleChange}
      ></input>
      <Dropdown label={label} options={[]} handleSelect={() => {}} />
      <label htmlFor={label}>{label}</label>
      <input
        type="range"
        id={label}
        name={label}
        min={minValue}
        max={maxValue}
        step={step}
        onChange={handleChange}
      ></input>
    </div>
  );
};

export default SearchByView;
