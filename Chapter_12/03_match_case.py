def https_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"


print(https_status(200))
print(https_status(404))
print(https_status(500))
print(https_status(43))
