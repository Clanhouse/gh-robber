import React, {createContext, useState, useContext} from 'react';

export const FavoriteContext = createContext()
export const useFavorite = () => useContext(FavoriteContext)

const FavoriteProvider = ({ children }) => {
  const [favorites, setFavorites] = useState([])

  const addFavorite = (githubUser) => {
    setFavorites([...favorites, githubUser])
  }
 
  const removeFavorite = (githubUser) => {
    const updatedFavorites =favorites.filter(fav => fav.id !== githubUser.id)
    setFavorites(updatedFavorites)
  }   

  return (
      <FavoriteContext.Provider value={{ favorites, addFavorite, removeFavorite }}>
          { children }
      </FavoriteContext.Provider>
  )
}

export default FavoriteProvider;