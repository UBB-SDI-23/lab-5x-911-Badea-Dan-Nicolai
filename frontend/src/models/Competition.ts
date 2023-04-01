import { CanCompete } from "./CanCompete";

export interface Competiton{
    id: number;
    name: string;
    region: string;
    date: Date;
    prize: number;
    category: string;
    cancompete: CanCompete[];
}