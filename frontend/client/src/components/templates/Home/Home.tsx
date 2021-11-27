import { FunctionComponent } from "react";
import { Link } from "react-router-dom";

const Home: FunctionComponent = () => {
  return (
    <div>
      <nav>
        <ul>
          <li>
            <Link to="/">GitHub Robber</Link>
          </li>
          <li>
            <Link to="/login">Sign up</Link>
          </li>
        </ul>
      </nav>
      <main>
        <h1>GitHub Robber</h1>
        <p>
          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quod optio et
          eligendi.
        </p>

        <section>
          <p>
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quibusdam et
            repellendus repellat illum numquam voluptatibus vel vero laboriosam id
            est, earum veritatis sed animi iure!
          </p>
        </section>
      </main>
    </div>
  );
};

export default Home;
