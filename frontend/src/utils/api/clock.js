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

const checkForOpenEntry = async() => {
    try {
        const res = await fetch('/api/clock/check-for-open-entry')

        return await res.json()
    } catch(err) {
        console.error('There was a problem checking for an open entry: ', err)
        throw err
    }
}

export default {
    addEntry,
    clockOut,
    checkForOpenEntry
}