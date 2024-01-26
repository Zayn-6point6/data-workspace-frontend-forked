// @ts-nocheck
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';

import Button from '@govuk-react/button';
import Button from '@govuk-react/button';
import FormGroup from '@govuk-react/form-group';
import Label from '@govuk-react/label';
import LabelText from '@govuk-react/label-text';
import { TextAreaField } from '@govuk-react/text-area';
import { H1 } from 'govuk-react';
import { useStateMachine } from 'little-state-machine';
import styled from 'styled-components';

import Errors from '../components/Errors';
import updateAction from './updateAction';

const StyledFormGroup = styled(FormGroup)`
  ${(props) => {
    if (props.error) {
      return `
            span {
                color: rgb(212, 53, 28);
                font-weight: 700;
            }
        `;
    }
  }}
`;

const Feedback = () => {
  const storage = JSON.parse(sessionStorage.getItem('__LSM__'));

  const { actions } = useStateMachine({ updateAction });
  const navigate = useNavigate();
  const onSubmit = (data) => {
    actions.updateAction(data);
    navigate('/confirmation');
  };

  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    defaultValues: storage?.contact?.feedbackMessage
  });

  return (
    <>
      <H1>Feedback form</H1>
      <Errors errors={errors} />
      <form onSubmit={handleSubmit(onSubmit)}>
        <StyledFormGroup error={!!errors.feedbackMessage}>
          <Label>
            <LabelText>Please tell us what we could do better</LabelText>
            <TextAreaField
              {...register('feedbackMessage', {
                required: 'We need to know what we can do better'
              })}
              name="feedbackMessage"
              rows="5"
            />
          </Label>
        </StyledFormGroup>
        <Button as={Link} to="/">
          Go back
        </Button>
        &nbsp; &nbsp;
        <Button>Submit</Button>
      </form>
    </>
  );
};

export default Feedback;
