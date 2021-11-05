import styled from "styled-components";

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
  > h1 {
    margin: 0px;
    box-sizing: border-box;
    border: 0px solid rgb(225, 228, 232);
    font-size: 2rem;
    font-family: "Candela Bold", sans-serif;
    --tw-shadow: 0 0 transparent;
    --tw-ring-inset: var(--tw-empty);
    --tw-ring-offset-width: 0px;
    --tw-ring-offset-color: #fff;
    --tw-ring-color: rgba(3, 102, 214, 0.5);
    --tw-ring-offset-shadow: 0 0 transparent;
    --tw-ring-shadow: 0 0 transparent;
    animation: 0s ease 0s 1 normal none running none !important;
    line-height: var(--typescale-1000-line-height) !important;
  }
`;
