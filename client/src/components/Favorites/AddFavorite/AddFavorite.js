import React from 'react';
import FavoriteIcon from '@material-ui/icons/Favorite'; 
import FavoriteBorderIcon from '@material-ui/icons/FavoriteBorder';
import { useFavorite } from '../../../Context/favoriteProvider';


const AddFavorite = ({ githubUser }) => {

	const { addFavorite, removeFavorite, favorites } = useFavorite()
	const isFavorite = favorites.map(fav => fav.id).includes(githubUser.id)
    
	const toggleFavorites = githubUser => {
      if (isFavorite) {
		  removeFavorite(githubUser)
	  } else {
		  addFavorite(githubUser)
	  }
	}

	return (
           <div onClick={() => toggleFavorites(githubUser)}>
           {isFavorite ? <FavoriteIcon /> : <FavoriteBorderIcon />} 
          </div>
	);
};

export default AddFavorite;