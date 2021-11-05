import styled from 'styled-components';

export const RepoListWrapper = styled.div`
    color: ${({ theme }) => theme.colors.orange};
    width: 100%;
    height: 100%;

    ${({ theme }) => theme.flex.column_center_center}
`;

export const RepoListView = styled.ul`
    background-color: ${({ theme }) => theme.colors.white};
    width: 50%;
    height: 50%;
    padding: 0;

    overflow: scroll;
`;