import { FunctionComponent } from "react";
import { Redirect, Route, useRouteMatch } from "react-router-dom";
import { Container } from "./Dashboard.styles";
import Menu from "../Menu/Menu";
import { dashboardRoutes } from "../../router/routes";
import useAuthUserContext from "../../context/Auth/useAuthUserContext";

const Dashboard: FunctionComponent = () => {
  const { repolist, search, favorites } = dashboardRoutes;

  const { path } = useRouteMatch();
  const [user] = useAuthUserContext();

  console.log("context dashboard", user);

  if (!user) {
    return <Redirect to="/login" />;
  }

  return (
    <Container>
      <Menu />
      <Route exact path={`${path}`} component={repolist} />
      <Route path={`${path}/search`} component={search} />
      <Route exact path={`${path}/favorites`} component={favorites} />
    </Container>
  );
};

export default Dashboard;
