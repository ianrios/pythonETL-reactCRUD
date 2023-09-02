import { createContext, useContext, useEffect, useState } from "react";

import { axiosHelper } from "../utils/axios-helper";

const AppContext = createContext(null);

const AppWorker = () => {
    const [rows, setRows] = useState(0);
    const [totalAvailablePages, setTotalAvailablePages] = useState(0);
    const limitsArr = [25, 50, 100]; // limit can only be one from the limitsArr to avoid any mistakes
    const [limit, setLimit] = useState(limitsArr[0]); // initially use the 0 index just to grab the correct limit
    const [page, setPage] = useState(0) // initially we are at the 0 page on load
    const [offset, setOffset] = useState(0); // can be 0, 25, 50, or 75
    const [columns, setColumns] = useState([]);
    const [currentPagedData, setCurrentPagedData] = useState([]);

    // get number of pages and rows for future use
    const getCurrPageSize = (newLimit = 0) => {
        const useLimit = newLimit ? newLimit : limit;
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
    const getPage = ({ page = 0 }) => {
        // with no params, returns very first page
        // otherwise you can configure as needed

        // calculate the new page using the current offsets and limit, comparing them to the previous page

        const url = `covid-stats/exact-page/${page}/limit/${limit}/offset/${offset}`;
        axiosHelper({
            url,
            successMethod: (d) => {
                setCurrentPagedData(JSON.parse(d.data.results));

                setPage(page)
                // setOffset(offset)
                // setNewLimit(limit)

                // const topRow = (page * limit) + offset
            },
        });
    };



    // reload page if limit changes
    useEffect(() => {
        getPage({ page })
    }, [limit]);


    // init first page on load of app
    useEffect(() => {
        if (currentPagedData.length === 0) getPage({})
    }, [currentPagedData]);

    // set new limit for future use
    const setNewLimit = (newLimit) => {
        setLimit(newLimit);
        getCurrPageSize(newLimit);
    };

    return {
        // for pagination
        rows,
        totalAvailablePages,
        limitsArr,
        limit,
        setNewLimit,
        offset,
        setOffset,
        page,
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
