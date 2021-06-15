import styled from 'styled-components';

export const Wrapper = styled.div`
    background-color: ${({ theme }) => theme.colors.black};
    color: ${({ theme }) => theme.colors.black};
    width: 100%;
    height: 100vh;

    ${({ theme }) => theme.flex.column_center_center}
`;

export const LoginWindow = styled.div`
    background-color: ${({ theme }) => theme.colors.white};
    width: 50%;
    height: 50%;
    border-radius: 4rem;
    box-shadow: inset 0 0 26px ${({ theme }) => theme.colors.black};

    ${({ theme }) => theme.flex.column_center_center}
`;