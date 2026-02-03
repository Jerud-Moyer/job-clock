export const getLocalDateTime = (isoDate) => {
    return new Date(`${isoDate}Z`) // add the Z so JS knows it's UTC
}

export const getReadableDate = (isoDate) => {
    const localDateTime = getLocalDateTime(isoDate)
    const dateHere = localDateTime.toLocaleDateString()
    const timeHere = localDateTime.toLocaleTimeString()
    return `${dateHere} - ${timeHere}`
}