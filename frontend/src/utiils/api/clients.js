const addClient = async(client) => {
    try{
        const res = await fetch('/api/clients/add-client', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(client),
        })
    
        return await res.json()
    }
    catch(err) {
        console.error('Error adding client:', err);
        throw err;
    }
}

export default {
    addClient,
}