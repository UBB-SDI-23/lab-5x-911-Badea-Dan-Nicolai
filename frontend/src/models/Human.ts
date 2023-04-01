import { Car } from "./Car";

export interface Human{
    id: number;
    cnp: string;
    dob: Date;
    email: string;
    name: string;
    cars: Car[];
}