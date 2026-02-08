const addEntry = async(entry) => {
    try {
        const res = await fetch('/api/clock/add-entry', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(entry)
        })

        return await res.json()
    } catch(err) {
        console.error('Problem adding time entry: ', err)
        throw err
    }
}

const clockOut = async(entryId) => {
    try {
        const res = await fetch(`/api/clock/clock-out/${entryId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                end_time: new Date().toISOString()
            })
        })

        return await res.json()
    } catch(err) {
        console.error('There was a problem clocking out: ', err)
        throw err
    }
}

const updateEntry = async(entry) => {
    try {
        const res = await fetch(`/api/clock/update-entry/${entry.id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(entry)
        })

        return await res.json()
    } catch(err) {
        console.error('There was a problem updating that entry: ', err)
        throw err
    }
}

const deleteEntry = async(id) => {
    try {
        const res = await fetch(`/api/clock/delete-entry/${id}`, {
            method: 'DELETE'
        })

        return await res.json()
    } catch(err) {
        console.error('There was a problem deleting that entry: ', err)
        throw err
    }
}

const checkForOpenEntry = async() => {
    try {
        const res = await fetch('/api/clock/check-for-open-entry')

        return await res.json()
    } catch(err) {
        console.error('There was a problem checking for an open entry: ', err)
        throw err
    }
}

const getEntryById = async(id) => {
    try {
        const res = await fetch(`/api/clock/get-entry-by-id/${id}`)

        return await res.json()
    } catch(err) {
        console.error('Could not find that entry')
        throw err
    }
}

const getEntriesByDateRange = async(dates) => {
    // datesType: {
    //     start_time: ISODate,
    //     end_time: ISODate
    // }
    try {
        const res = await fetch('api/clock/get-entries-by-date', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dates)
        })
        return await res.json()
    } catch(err) {
        console.error('There was a problem fetching time-entries ', err)
    }
}

export default {
    addEntry,
    clockOut,
    updateEntry,
    deleteEntry,
    checkForOpenEntry,
    getEntryById,
    getEntriesByDateRange
}