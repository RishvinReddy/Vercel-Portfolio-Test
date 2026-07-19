import type { Metadata } from "next";
import "./globals.css";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";

export const metadata: Metadata = {
  title: "Rishvin Reddy | Software Engineering, Cybersecurity, IoT & Blockchain",
  description: "Official portfolio of Erolla Rishvin Reddy, a B.Tech CSE student at Woxsen University specializing in Blockchain, IoT and Cybersecurity.",
  keywords: "Rishvin Reddy, Erolla Rishvin Reddy, Software Engineer, Cybersecurity, IoT, Blockchain, Woxsen University",
  authors: [{ name: "Erolla Rishvin Reddy" }],
  creator: "Erolla Rishvin Reddy",
  publisher: "Rishvin Reddy",
  openGraph: {
    type: "website",
    locale: "en_IN",
    url: "https://rishvinreddy.github.io/",
    siteName: "Rishvin Reddy Portfolio",
    title: "Rishvin Reddy | Software Engineering, Cybersecurity, IoT & Blockchain",
    description: "Explore the engineering portfolio of Erolla Rishvin Reddy.",
    images: [{ url: "https://rishvinreddy.github.io/icon.png", width: 1200, height: 630, alt: "Rishvin Reddy Portfolio" }],
  },
  twitter: {
    card: "summary_large_image",
    site: "@RishvinReddy",
    creator: "@RishvinReddy",
    title: "Rishvin Reddy | Software Engineering, Cybersecurity, IoT & Blockchain",
    description: "Engineering portfolio covering cybersecurity, IoT, blockchain, full-stack development.",
    images: ["https://rishvinreddy.github.io/icon.png"],
  },
  icons: {
    icon: "/icon.png",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="h-full antialiased">
      <body className="min-h-full flex flex-col pt-16">
        <Header />
        <main className="flex-grow">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
