import styled from 'styled-components';

export const Container = styled.nav`
    background-color: ${({ theme }) => theme.colors.black};
    width: 100%;
    height: 100vh;

    display: flex;
    justify-content: space-between;
    align-items: center;
`;