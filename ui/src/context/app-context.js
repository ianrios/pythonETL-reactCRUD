import { createContext, useContext, useEffect, useState } from "react";
import { axiosHelper } from "../utils/axios-helper";

const AppContext = createContext(null)

const AppWorker = () => {
    const [rows, setRows] = useState(0)
    const [pages, setPages] = useState(0)

    // get pages and rows for future use
    useEffect(() => {
        const url = 'covid-stats/pages'
        axiosHelper({
            url, successMethod: d => {
                setRows(d.data.row_count)
                setPages(d.data.max_pages)
            }
        })
    }, [])

    return {
        rows, pages
    }
}

export const AppProvider = ({ children }) => {
    const initialContext = AppWorker()
    return (<AppContext.Provider value={initialContext}>{children}</AppContext.Provider>)
}

export const useAppContext = () => useContext(AppContext)

export default AppContext