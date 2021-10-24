import {of} from 'rxjs';
import {delay} from 'rxjs/operators';

const apiRoot = process.env.VUE_APP_API_URL

class UsersService {
    listUser() {
        console.info("List user")
        // return [
        //     {
        //         note: "Nhan Le Thanh (RBVH/ETM2)",
        //         login: "udo1hc",
        //         pass: "7jj9u2y4qQ3>ZD",
        //         isAdmin: true,
        //         apps: [
        //             "/dee"
        //         ]
        //     },
        //     {
        //         note: "Phong Tran Loi (RBVH/ETM24)",
        //         login: "rph2hc",
        //         pass: ">kT9BUKz4qQ3>ZD",
        //         isAdmin: false,
        //         apps: [
        //             "/translators"
        //         ]
        //     },
        //     {
        //         note: "Huy Le Quang (RBVH/ETM2)",
        //         login: "qu1hc",
        //         pass: "PUj7jj9u2yKmtGfS",
        //         isAdmin: false,
        //         apps: [
        //             "/apex",
        //             "/mc2"
        //         ]
        //     }];
        const apiPath = "/users"
        return fetch(apiRoot + apiPath)
    }

    searchUser(query) {
        //TODO
        console.info("Search user " + query)
    }

    saveUser(user) {
        //TODO
        console.info("Save user " + JSON.stringify(user))
        return of({})
            .pipe(delay(1000))
    }

    deleteUser(user) {
        //TODO
        console.info("Delete user " + JSON.stringify(user))
        return of({})
            .pipe(delay(1000))
    }
}


export default new UsersService()
