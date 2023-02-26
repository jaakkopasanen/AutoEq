import { useRef, useState } from 'react';

const useStateRef = (initialValue) => {
  const [state, setState] = useState(initialValue);
  const ref = useRef(initialValue);

  const update = (newValue) => {
    ref.current = newValue;
    setState(newValue);
  };

  return [state, update, ref];
};

export default useStateRef;
