import { UserButton } from "@clerk/nextjs";

export default function Navbar() {
    return (

        <nav className="flex justify-between p-4 border-b">

            <h1>

                AI Tourism RAG

            </h1>

            <UserButton/>

        </nav>

    )
}