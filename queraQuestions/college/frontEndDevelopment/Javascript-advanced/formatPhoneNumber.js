// https://quera.org/college/6092/chapter/43168/lesson/144505/?comments_page=1&comments_filter=ALL&submissions_page=1
export function formatPhoneNumber(phoneNumber) {
    const reg = /^09\d{9}$/;
    
    if (reg.test(phoneNumber)) {
        return "+98" + phoneNumber.slice(1);
    } else {
        return null;
    }
}
