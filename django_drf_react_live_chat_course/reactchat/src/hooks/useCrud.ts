import { useState } from "react";
import { BASE_URL } from "../config";
import useAxiosWithInterceptor from "../helpers/jwtinterceptor";
interface useCrudInterface<T> {
  dataCRUD: T[];
  fetchData: () => Promise<void>;
  error: Error | null;
  isloading: boolean;
}

const useCrud = <T>(intialData: T[] ,API_URL: string): useCrudInterface<T> => {
  const jwtAxios = useAxiosWithInterceptor();
  const [dataCRUD, setDataCRUD] = useState<T[]>(intialData);
  const [error, setError] = useState<Error | null>(null);
  const [isloading, setIsloading] = useState<boolean>(false);

  const fetchData = async () => {
    setIsloading(true);
    try {        
      const response = await jwtAxios.get(`${BASE_URL}/${API_URL}`);
      const data = response.data;
      setDataCRUD(data);
      setError(null);
      setIsloading(false);
      return data;
    }
    catch (error: any) {
        console.log(error)
      if (error.response && error.response.status == 400) {
        setError(new Error("400"));
      }
      setIsloading(false);
      throw error;
    }
  }
  return { dataCRUD, fetchData, error, isloading};
}


export default useCrud;