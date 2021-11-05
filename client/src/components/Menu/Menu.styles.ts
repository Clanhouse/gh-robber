import styled from 'styled-components';

export const MenuWrapper = styled.nav`
    background-color: ${({ theme }) => theme.colors.white};
    color: ${({ theme }) => theme.colors.orange};
    width: 15%;
    height: 100%;

    ${({ theme }) => theme.flex.column_start_center};

`;