// @ts-nocheck
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';

import Button from '@govuk-react/button';
import Button from '@govuk-react/button';
import Fieldset from '@govuk-react/fieldset';
import FormGroup from '@govuk-react/form-group';
import Input from '@govuk-react/input';
import Label from '@govuk-react/label';
import LabelText from '@govuk-react/label-text';
import Radio from '@govuk-react/radio';
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

const SupportAndFeedback = () => {
  const storage = JSON.parse(sessionStorage.getItem('__LSM__'));

  const { actions } = useStateMachine({ updateAction });
  const navigate = useNavigate();
  const onSubmit = (data) => {
    const { feedback } = data;
    const hasFeedback = feedback == 'yes' ? true : false;
    actions.updateAction(data);
    hasFeedback ? navigate('/feedback') : navigate('/confirmation');
  };

  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm({
    defaultValues: storage?.contact
  });

  return (
    <>
      <H1>Contact us</H1>
      <Errors errors={errors} />
      <form onSubmit={handleSubmit(onSubmit)}>
        <StyledFormGroup error={!!errors.firstName}>
          <Label>
            <LabelText>First name</LabelText>
            <Input
              {...register('firstName', {
                required: 'You must have a first name'
              })}
              id="firstName"
            />
          </Label>
        </StyledFormGroup>
        <StyledFormGroup error={!!errors.lastName}>
          <Label>
            <LabelText>Last name</LabelText>
            <Input
              {...register('lastName', {
                required: 'You must have a last name'
              })}
              id="lastName"
            />
          </Label>
        </StyledFormGroup>
        <StyledFormGroup error={!!errors.contactMessage}>
          <Label>
            <LabelText>Let us know how we can help</LabelText>
            <TextAreaField
              {...register('message', {
                required: 'We need to know how we can help you'
              })}
              name="message"
              rows="5"
            />
          </Label>
        </StyledFormGroup>
        <StyledFormGroup error={!!errors.feedback}>
          <Fieldset>
            <Fieldset.Legend size="MEDIUM">
              Could you spare 2 mins for feedback?
            </Fieldset.Legend>
            <Radio
              {...register('feedback', {
                required: 'Please tell us if you could spare 2 mins'
              })}
              value="yes"
              name="feedback"
            >
              Yes
            </Radio>
            <Radio {...register('feedback')} value="no" name="feedback">
              No
            </Radio>
          </Fieldset>
        </StyledFormGroup>
        <Button>Submit</Button>
      </form>
    </>
  );
};

export default SupportAndFeedback;
