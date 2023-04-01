import { Car } from "./Car";
import { Competiton } from "./Competition";

export interface CanCompete{
    id: number;
    buy_in: number;
    sponsor: string;
    car: Car;
    competition: Competiton;
}