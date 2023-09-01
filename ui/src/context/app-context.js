import { createContext, useContext, useEffect, useState } from "react";

import { axiosHelper } from "../utils/axios-helper";

const AppContext = createContext(null);

const AppWorker = () => {
  const [rows, setRows] = useState(0);
  const [totalAvailablePages, setTotalAvailablePages] = useState(0);
  const limitsArr = [25, 50, 100]; // limit can only be one from the limitsArr to avoid any mistakes
  const [limitIndex, setLimitIndex] = useState(0);
  const [currentLimit, setCurrentLimit] = useState(limitsArr[limitIndex]);
  const [offset, setOffset] = useState(0); // can be 0, 25, 50, or 75
  const [columns, setColumns] = useState([]);
  const [currentPagedData, setCurrentPagedData] = useState([]);

  // get number of pages and rows for future use
  const getCurrPageSize = (newLimit = 0) => {
    const useLimit = newLimit ? newLimit : currentLimit;
    const url = `covid-stats/pages/${useLimit}`;
    axiosHelper({
      url,
      successMethod: (d) => {
        setRows(d.data.row_count);
        setTotalAvailablePages(d.data.max_pages);
      },
    });
  };
  // init page size and total number rows
  useEffect(() => {
    getCurrPageSize();
  }, []);

  // get columns
  useEffect(() => {
    const url = "covid-stats/columns";
    axiosHelper({ url, successMethod: (d) => setColumns(d.data) });
  }, []);

  // get a page from the db
  const getPage = (page = 0) => {
    // with no params, returns very first page
    // otherwise you can configure as needed
    const url = `covid-stats/exact-page/${page}/limit/${currentLimit}/offset/${offset}`;
    axiosHelper({
      url,
      successMethod: (d) => {
        console.log({ d });
        setCurrentPagedData(JSON.parse(d.data.results));
      },
    });
  };

  // init first page on load of app
  useEffect(() => {
    if (currentPagedData.length === 0) {
      getPage();
    }
  }, [currentPagedData]);

  // set new limit for future use
  const setNewLimit = (newIndex) => {
    setLimitIndex(newIndex);
    setCurrentLimit(limitsArr[newIndex]);
    getCurrPageSize(limitsArr[newIndex]);
  };

  return {
    // for pagination
    rows,
    totalAvailablePages,
    limitsArr,
    currentLimit,
    setNewLimit,
    offset,
    setOffset,
    getPage,

    // for displaying correctly
    columns,

    // data to use on table
    currentPagedData,
  };
};

export const AppProvider = ({ children }) => {
  const initialContext = AppWorker();
  return (
    <AppContext.Provider value={initialContext}>{children}</AppContext.Provider>
  );
};

export const useAppContext = () => useContext(AppContext);

export default AppContext;
