import { createContext, useContext, useEffect, useState } from "react";
import { axiosHelper } from "../utils/axios-helper";

const AppContext = createContext(null)

const AppWorker = () => {
    const [rows, setRows] = useState(0)
    const [pages, setPages] = useState(0)
    const [columns, setColumns] = useState([])
    const [currentPagedData, setCurrentPagedData] = useState([])

    // get number of pages and rows for future use
    useEffect(() => {
        const url = 'covid-stats/pages'
        axiosHelper({
            url, successMethod: d => {
                setRows(d.data.row_count)
                setPages(d.data.max_pages)
            }
        })
    }, [])

    // get columns
    useEffect(() => {
        const url = 'covid-stats/columns'
        axiosHelper({ url, successMethod: d => setColumns(d.data) })
    }, [])


    const getPage = (page) => {
        const url = `covid-stats/page/${page}`
        axiosHelper({
            url, successMethod: d => {
                console.log({ d })
                setCurrentPagedData(JSON.parse(d.data.results))
            }
        })
    }
    useEffect(() => {
        if (currentPagedData.length === 0) {
            getPage(0)
        }
    }, [currentPagedData])

    console.log(currentPagedData)


    return {
        rows, pages, columns, getPage, currentPagedData
    }
}

export const AppProvider = ({ children }) => {
    const initialContext = AppWorker()
    return (<AppContext.Provider value={initialContext}>{children}</AppContext.Provider>)
}

export const useAppContext = () => useContext(AppContext)

export default AppContext