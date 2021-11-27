import { Link, useRouteMatch } from "react-router-dom";

import { MenuWrapper } from "./Menu.styles";
import { LangMenu } from "../../i18n/ENG";
import useLogout from "./Menu.hooks";

const Menu = () => {
  const GoogleLogoutButton = useLogout();

  const { path } = useRouteMatch();
  const { link1, link2 } = LangMenu;

  return (
    <MenuWrapper>
      <Link to={`${path}`}>GitHub Robber</Link>
      <GoogleLogoutButton />
      <Link to={`${path}/search`}>{link1}</Link>
      <Link to={`${path}/favorites`}>{link2}</Link>
    </MenuWrapper>
  );
};

export default Menu;
