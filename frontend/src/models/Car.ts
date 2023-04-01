import { Human } from "./Human";
import { CanCompete } from "./CanCompete";

export interface Car{
    id: number;
    brand: string;
    make: string;
    year: Date;
    consumption: number;
    color: string;
    owner: Human;
    cancompete: CanCompete[];
}