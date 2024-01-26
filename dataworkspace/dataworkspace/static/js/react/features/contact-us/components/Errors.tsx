// @ts-nocheck
import ErrorSummary from '@govuk-react/error-summary';

const Errors = ({ errors }) => {
  const hasNoErrors = Object.keys(errors).length > 0;
  if (!hasNoErrors) {
    return null;
  }

  const errorMessages = Object.keys(errors).map((key) => {
    return {
      targetName: errors[key].ref,
      text: errors[key].message
    };
  });
  return (
    <ErrorSummary
      description="Please correct the following"
      errors={errorMessages}
      heading="Oops there seems to be some sort of issue"
      onHandleErrorClick={(ref) => ref.focus()}
    />
  );
};

export default Errors;
