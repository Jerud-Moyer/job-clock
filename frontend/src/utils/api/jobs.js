const addJob = async (job) => {
    try {
        console.log('GET YER JOB HERE => ', job)
        const res = await fetch('/api/jobs/add-job', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(job),
        });

        return await res.json();
    } catch (err) {
        console.error('Error adding job:', err);
        throw err;
    }
}

const getJobs = async () => {
    try {
        const res = await fetch('/api/jobs/get-jobs');
        console.log('Response from getJobs:', res);
        return await res.json();
    } catch (err) {
        console.error('Error fetching jobs:', err);
        throw err;
    }
}

const updateJob = async (id, job) => { 
    try {
        const res = await fetch(`/api/jobs/update-job/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(job),
        });

        return await res.json();
    } catch (err) {
        console.error('Error updating job:', err);
        throw err;
    }
}

export default {
    getJobs,
    addJob,
    updateJob
}