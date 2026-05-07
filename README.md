# 🚀 Gnet.AI Open SDK: The Universal Game Bridge
Welcome to the most fluid ecosystem for indie developers. 
**Gnet.AI Open SDK** allows you to export your games from any engine directly to the **Gogi Star VM** for live showcases, instant testing, and global exposure.

---

## 🧠 How it works (The Logic)
Our architecture uses a **Three-Step Secure Handshake** to ensure maximum speed and safety without exposing private keys:

1. **The Handshake**: Your game engine calls Gogi’s VM Gatekeeper.
2. **The Clearance**: Gogi verifies the SDK authenticity and issues a **Presigned R2 URL** (a temporary high-speed upload tunnel).
3. **The Teleport**: The SDK uploads your build directly to our Cloudflare R2 storage. Gogi is notified, downloads the game, extracts it, and prepares it for the next Twitch Live Session.

---

## 🛠 Supported Engines & Integration

### 🟢 Unity (C#)
1. Import `GnetSDK.cs` into your project.
2. Call `GnetSDK.instance.ShipToGogi(zipPath, "YourDevName", "ProjectName");`
*The SDK handles the REST calls and the direct R2 upload automatically.*

### 🔵 Godot (GDScript)
1. Add the `GnetNode` to your scene.
2. Use `Gnet.upload_game(file_path, dev_name, project_id)`.
*Compatible with Godot 4.x (logic-driven).*

### 🔴 Unreal Engine (C++)
1. Include the `GnetBridge` module.
2. Call `UGnetSDK::DispatchBuild(BuildPath, DeveloperInfo)`.
*Optimized for C++ performance and zero-latency handshake.*

### 🟠 GameMaker & Others
Any engine that supports **HTTP POST/PUT** can use the Gnet SDK by targeting Gogi's Public Gatekeeper: `http://[YOUR_VM_IP]:5000/sdk/get_upload_link`.

---

## 🛡 Security & Fairness
- **No Private Keys**: Developers never see our storage keys. They only get a one-time upload token. [INDEX: 1]
- **Integrity Check**: Gogi's VM cross-references your SDK version with this official GitHub repository. Modified or "trash" builds are automatically rejected. [INDEX: 2]
- **Gnet Certification**: Once your game is grabbed, Gogi writes a log on the **Live Matrix Overlay** and announces the "Grab" on our official social channels (Buffer).

---

## 📦 Getting Started
1. Clone this repository.
2. Open the folder corresponding to your engine.
3. Replace `HUB_URL` with the one found on the [Gnet.AI Portal](http://altervista.org).
4. Export your game and watch Gogi play it live!

---

## 💎 Why Gnet.AI?
We believe in **100% Human Logic** and **0% AI-Generated Art** for game cores. By using this SDK, your project becomes part of a high-performance ecosystem designed for the next generation of 144FPS gaming.

*"Lmao, nice code. Let's see if it survives my stream."* — **Gogiroy_Jay**

