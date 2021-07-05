import styled from 'styled-components';

export const FavoriteWrapper = styled.div`
    color: ${({ theme }) => theme.colors.white};
    width: 100%;
    height: 100%;
    text-align: center;
`;

export const FavoriteItem = styled.li`
    color: ${({ theme }) => theme.colors.white};
    ${({ theme }) => theme.flex.column_center_center};
`;