// @ts-nocheck
import { typography } from '@govuk-react/lib';
import { H1, H2, ListItem, UnorderedList } from 'govuk-react';
import { useStateMachine } from 'little-state-machine';
import styled from 'styled-components';

const StyledParagraph = styled('p')`
  ${typography.font({ size: 19 })};
`;

const Confirmation = () => {
  const { state } = useStateMachine();
  const hasFeedback = state.contact.feedback == 'yes' ? true : false;
  return (
    <>
      <H1>Confirmation</H1>
      <StyledParagraph>
        Thank you for contacting us and we will be in touch shortly. Below is a
        summary of what you sent us.
      </StyledParagraph>
      <H2 size="M">Contact details</H2>
      <UnorderedList listStyleType="bullet">
        <ListItem>
          Name: {state.contact.firstName} {state.contact.lastName}{' '}
        </ListItem>
        <ListItem>Message: {state.contact.message}</ListItem>
      </UnorderedList>
      {hasFeedback ? (
        <>
          <H2 size="M">Feedback details</H2>
          <StyledParagraph>
            Legend thanks for the feedback! Below is summary of the feedback you
            sent us.
          </StyledParagraph>
          <UnorderedList listStyleType="bullet">
            <ListItem>
              Feedback message: {state.contact.feedbackMessage}
            </ListItem>
          </UnorderedList>
        </>
      ) : (
        <StyledParagraph>
          Next time please leave us some feedback!
        </StyledParagraph>
      )}
    </>
  );
};

export default Confirmation;
