import { ClerkProvider } from "@clerk/nextjs";
import "./globals.css";
import { Geist } from "next/font/google";
import { cn } from "@/lib/utils";
import Navbar from "@/components/navbar/Navbar";
const geist = Geist({subsets:['latin'],variable:'--font-sans'});

export const metadata = {
  title: "AI Tourism RAG",
  description: "AI Powered Tourism Planner"
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <ClerkProvider>
      <html lang="en" className={cn("font-sans", geist.variable)}>
        <body><Navbar/>{children}</body>
      </html>
    </ClerkProvider>
  );
}