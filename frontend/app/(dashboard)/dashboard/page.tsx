"use client";

import { useAuth } from "@clerk/nextjs";
import { api } from "@/services/api";

export default function DashboardPage() {
  const { getToken } = useAuth();

  async function testBackend() {
    try {
      // Get JWT from Clerk
      const token = await getToken({
        template: "fastapi",
      });

      console.log("JWT:", token);

      // Call FastAPI
      const response = await api.get("/auth/me", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      console.log("Backend Response:", response.data);

      alert("Backend Connected Successfully!");
    } catch (error) {
      console.error("Error:", error);
      alert("Backend Connection Failed");
    }
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Dashboard</h1>

      <button
        onClick={testBackend}
        style={{
          padding: "10px 20px",
          cursor: "pointer",
        }}
      >
        Test Backend
      </button>
    </div>
  );
}