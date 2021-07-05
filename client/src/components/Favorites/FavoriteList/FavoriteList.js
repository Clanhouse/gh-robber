import React from 'react';
import { useFavorite } from '../../../Context/favoriteProvider';
import { FavoriteWrapper, FavoriteItem } from './FavoriteList.style';

const FavoriteList = () => {
    const { favorites } = useFavorite()
	
	return (
		<FavoriteWrapper>
            <h1>Favorities Users</h1>
			  <ul>
			    {favorites.map(user => 
				  <FavoriteItem key={ user.id }>
                    { user.username } 
				  </FavoriteItem>     
				)}
			  </ul>		
		</FavoriteWrapper>
	);
};

export default FavoriteList;