import styled from 'styled-components';

export const SearchWrapper = styled.div`
    color: ${({ theme }) => theme.colors.orange};
    width: 100%;
    height: 100%;

    ${({ theme }) => theme.flex.column_center_center}
`;
