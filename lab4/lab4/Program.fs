open System

// printfn "Podaj imie "
// let name = System.Console.ReadLine()

// printfn " Witaj %s" name

// let powitanie = "Witaj" + " Jan"
// //


// // if x > 0 then
// //     printfn "Liczba dodatnia"
// // else
// //     printfn "Ujemna"


// let lista = [1;2;3]
// let nowalista =  0 :: lista

// for i = 1 to 5 do
//     printfn "Wartosc %d" i

// for i = 5 downto 1 do
//     printfn "Wartosc %d" i

// let mutable x = 5

// while x<5 do
//     printfn "Wartosc %d" x
//     x <- x+1


// type Osoba = 
//     {
//         Imie: string
//         Wiek : int
//     }

// let osoba1 = {Imie = "Jan"; Wiek = 24}
// printfn "Imie = %s wiek = %d" osoba1.Imie osoba1.Wiek

// let str = "3.14"
// let liczba = System.Double.TryParse(str)

// printfn "Podaj liczbe calkowita "
// let input = System.Console.ReadLine()
// let liczba1 = Int32.Parse(input)

// let age = 20
// match age with
//     | x when x < 18 -> printfn "niepelno"
//     | x when x >=18 -> printfn "pelno"
//     | _ -> printfn "senior"

// let rec suma n =
//     if n <= 0 then 0
//     else n + suma(n-1)

// printfn "suma liczb od 1 do 5 = %d" (suma 5)

//rekurencja ogonowa

// let sumarekTail n = 
//     let rec loop n acc =
//         if n <= 0 then acc
//         else loop (n-1) (acc+n)//rek ogonowa
//     loop n 0 //wywol funk pomocniczej

