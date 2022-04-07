/* 
 This kata was unbeliavably annoying. So annoying that
 I decided to save it for further reference.

 Constraints were: 
    - Blank spaces ("" on ip)
    - leading zeroes on ip
    - numbers out of range (0 to 255)
    - negative numbers
    - /n on ip address ("/n" on a ip address? ..what?)
    - letters on ip addres
    - '' as ip address
    - and ip address of this format: '127.0.0.' or '126..1.1'.

 It was solved in javascript.
*/

function isValidIP(str) {
    let ipSplt = str.split('.')

    if (str == "" || ipSplt.length != 4 || str.includes(",") || str.includes(" ") || str.includes('\n')) {
        return false
    } else {
        for (let ips of ipSplt) {
            if (ips > 255 || ips < 0) {
                return false
            } else if (ips.length > 1 && ips[0] == '0' || ips === "") {
                return false
            }


            for (let elem of ips) {
                if (!splitnum.includes(elem)) {
                    return false
                }
            }
        }
        return true
    }
}