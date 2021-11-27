import { IOptions } from "./Dropdown.types";

export const generateOptions = (options: IOptions) => {
  return options.map((option) => (
    <option key={option?.toString()} value={option}>
      {option}
    </option>
  ));
};
