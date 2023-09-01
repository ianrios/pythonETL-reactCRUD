import axios from "axios";
import { API_URL } from "../constants.js";

export const axiosHelper = ({
  method = "get",
  url = "",
  successMethod = (r) => console.log(r),
  failureMethod = (e) => console.log(e),
}) => {
  return axios({
    method,
    url: `${API_URL}/${url}`,
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
  })
    .then(successMethod)
    .catch(failureMethod);
};
