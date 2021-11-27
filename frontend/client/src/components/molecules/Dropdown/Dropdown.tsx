import { FunctionComponent } from "react";

import { LangDropdown } from "../../i18n/ENG";
import { IDropdownProps } from "./Dropdown.types";
import { generateOptions } from "./Dropdown.utils";

const Dropdown: FunctionComponent<IDropdownProps> = ({
  label,
  options,
  handleSelect,
}) => {
  const { mainLabel } = LangDropdown;

  return (
    <>
      <label htmlFor={label}>
        {mainLabel}
        {label}:
      </label>
      <select name={label} id={label} form={label} onChange={handleSelect}>
        {generateOptions(options)}
      </select>
    </>
  );
};

export default Dropdown;
