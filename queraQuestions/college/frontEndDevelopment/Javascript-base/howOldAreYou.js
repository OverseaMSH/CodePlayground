// https://quera.org/college/6092/chapter/20016/lesson/248157/?comments_page=1&comments_filter=ALL&submissions_page=1
function calculateAge(birthDateString, currentDateString) {
    const birthDate = new Date(birthDateString);
    const currentDate = new Date(currentDateString);

    let age = currentDate.getFullYear() - birthDate.getFullYear();

    const hasHadBirthdayThisYear =
        currentDate.getMonth() > birthDate.getMonth() ||
        (currentDate.getMonth() === birthDate.getMonth() &&
        currentDate.getDate() >= birthDate.getDate());

    if (!hasHadBirthdayThisYear) {
        age--;
    }

    return age;
}

module.exports = { calculateAge };
