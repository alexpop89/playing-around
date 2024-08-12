class User {
    constructor(firstName, lastName, email) {
        this.firstName = firstName
        this.lastName = lastName
        this.email = email
    }

    __getFullName() {
        return this.firstName + ' ' + this.lastName
    }
}

class UserWhoCanLogin extends User {
    constructor(firstName, lastName, email, password) {
        super(firstName, lastName, email);
        this.password = password;
    }

    login() {
        console.log('Logging in')
    }
}