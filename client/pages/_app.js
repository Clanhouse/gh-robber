import ContextProvider from '../context/contextProvider'
import '../styles/globals.scss'

function MyApp({ Component, pageProps }) {
  return(
    <ContextProvider>
      <Component {...pageProps} />
    </ContextProvider>
  );
}

export default MyApp
