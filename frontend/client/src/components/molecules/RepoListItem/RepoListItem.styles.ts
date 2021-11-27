import styled from 'styled-components';

export const RepoListItemWrapper = styled.li`
    border-bottom: 1px solid ${({ theme }) => theme.colors.black};
    ${({ theme }) => theme.flex.row_start_center}
`;

export const RepoListItemItems = styled.p`
    margin-left: 5rem;
`;