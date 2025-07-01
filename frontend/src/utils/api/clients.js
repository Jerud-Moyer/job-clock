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

const getClients = async() => {
    try{
        const res = await fetch('/api/clients/get-clients', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        console.log('Response from getClients:', res);
        return await res.json()
    }
    catch(err) {
        console.error('Error fetching clients:', err);
        throw err;
    }
}


const updateClient = async (id, client) => {
    try {
        console.log('HELLO???')
        const res = await fetch(`/api/clients/update-client/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(client),
        });

        return await res.json();
    } catch (err) {
        console.error('Error updating client: ', err);
        throw err;
    }
}

const getClientOptions = async() => {
    try{
        const res = await fetch('/api/clients/get-client-options')
        
        return await res.json()
    } catch(err) {
        console.error('Encountered problem fetcjhing options: ', err)
        throw err
    }
}
  
export default {
    getClients,
    addClient,
    updateClient,
    getClientOptions
}