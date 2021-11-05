export type IOptions = Array<React.OptionHTMLAttributes<HTMLOptionElement>["value"]>;
export type IDropdownProps = {
  label: string;
  options: IOptions;
  handleSelect: (event: React.ChangeEvent<HTMLSelectElement>) => void;
};
