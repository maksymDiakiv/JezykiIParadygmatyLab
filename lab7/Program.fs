// // For more information see https://aka.ms/fsharp-console-apps
// type Person(name: string, age: int) = 
//     //pola prywatne
//     let mutable privateAge = age

//     //wlasciwosci
//     member this.Name = name

//     //get i set
//     member this.Age
//         with get() = privateAge
//         and set(value) = 
//             if value > 0 then
//                 privateAge <- value
//             else
//             printfn "Wiek pusi musi byc liczba dodantia"

//     //metody
//     member this.View() = 
//         printfn "witaj %s twoj wiek %d lat" this.Name, this.Age


// type Student(name: string, age: int, nr: string) = 
//     inherit Person(name, age)

//     member this.Nr = nr

//     override this.View() = 
//         printfn "witaj %s masz %d twoj numer %s" this.Name, this.Age, this.Nr



// //obiekt klasy
// let person = Person("Jan", 23)
// person.View()


type Book(title: string, author: string, lstr: int) =
    member this.Title = title
    member this.Author = author
    member this.Lstr = lstr

    member this.GetInfo() =
        printfn "name %s author %s pages %d" this.Title, this.Author, this.Lstr

type User(name: string) =
    let borrowedBooks = System.Collections.Generic.List<Book>()
    member this.Name = name
    
    

    member this.BorrowBook(book: Book) = 
        borrowedBooks.Add(book)
        printfn "%s wypozyczyl \"%s\"" this.Name, book.Title