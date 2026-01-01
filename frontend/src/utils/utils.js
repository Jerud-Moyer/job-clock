export const getLocalDateTime = (isoDate) => {
    return new Date(`${isoDate}Z`) // add the Z so JS knows it's UTC
}