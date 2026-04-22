# 🔐 SDN-Based Access Control System

## 📌 Project Description

This project implements an **access control system using Software Defined Networking (SDN)**. It leverages a centralized controller to enforce network policies dynamically, allowing or denying traffic based on predefined rules. Unlike traditional networks where access control is distributed across devices, this system centralizes decision-making, improving scalability, flexibility, and security.

The system monitors incoming network traffic, evaluates it against defined policies, and installs flow rules in switches to control packet forwarding behavior.

---

## ❗ Problem Statement

Traditional network access control systems suffer from several limitations:

* ❌ Decentralized rule management across multiple devices
* ❌ Difficult to update and maintain policies
* ❌ Lack of scalability in large networks
* ❌ Increased chances of misconfiguration and security vulnerabilities

There is a need for a **centralized, flexible, and scalable solution** to efficiently manage access control in modern networks.

---

## 🎯 Objectives

* To design a **centralized access control system** using SDN
* To dynamically **allow or deny traffic** based on policies
* To reduce manual configuration in network devices
* To improve **network security and manageability**
* To demonstrate **real-time policy enforcement** using SDN controller

---

## 🛠️ Tools & Technologies Used

* **Programming Language:** Python
* **SDN Controller:** (e.g., Ryu / POX / OpenDaylight – update based on your project)
* **Network Emulator:** Mininet
* **Protocols:** OpenFlow
* **Operating System:** Linux (Ubuntu recommended)
* **Libraries/Modules:**

  * Ryu framework (if used)
  * Networking libraries

---

## 🌐 Network Topology

The project uses a simple SDN-based topology consisting of:

* One **SDN Controller (central brain)**
* One or more **OpenFlow-enabled switches**
* Multiple **hosts (clients/servers)**

### Example Topology:

```
       Controller
           |
        Switch
       /   |   \
    Host1 Host2 Host3
```

* All hosts connect to the switch
* The switch communicates with the controller
* The controller decides how traffic should flow

---

## ⚙️ How It Works

1. A host sends a packet to another host
2. The switch checks its flow table:

   * If rule exists → forward packet
   * If no rule → send request to controller
3. The controller:

   * Checks access control policies
   * Decides whether to allow or deny traffic
4. Based on decision:

   * ✅ Allow → installs flow rule in switch
   * ❌ Deny → drops packet
5. Future packets follow installed rules (faster processing)

---

## ▶️ How to Run the Project

### Step 1: Install Dependencies

```bash
sudo apt update
sudo apt install mininet python3
pip install ryu
```

---

### Step 2: Clone the Repository

```bash
git clone https://github.com/amarpatil2004/SDN---based-access-control-system.git
cd SDN---based-access-control-system
```

---

### Step 3: Start the Controller

```bash
ryu-manager <controller_file.py>
```

*(Replace `<controller_file.py>` with your actual file name)*

---

### Step 4: Run Mininet Topology

```bash
sudo mn --topo single,3 --controller remote
```

---

### Step 5: Test the Network

Inside Mininet CLI:

```bash
pingall
```

* Observe allowed/blocked traffic based on rules

---

## 📊 Key Features

* Centralized access control
* Dynamic rule enforcement
* Reduced manual configuration
* Improved scalability and security

---

## ⚠️ Limitations

* Single point of failure (controller)
* Performance depends on controller efficiency
* Requires SDN-compatible infrastructure

---

## 🔮 Future Enhancements

* Add authentication mechanisms
* Implement role-based access control (RBAC)
* Use machine learning for adaptive policies
* Improve fault tolerance with distributed controllers

---

## 👨‍💻 Author

Amar Patil

---

## 📎 Conclusion

This project demonstrates how SDN can be effectively used to implement a **flexible and centralized access control system**, overcoming the limitations of traditional networks and providing better security and scalability.
