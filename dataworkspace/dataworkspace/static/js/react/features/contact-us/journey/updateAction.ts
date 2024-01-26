// @ts-nocheck
export default function updateAction(state, payload) {
  return {
    ...state,
    contact: {
      ...state.contact,
      ...payload
    }
  };
}
