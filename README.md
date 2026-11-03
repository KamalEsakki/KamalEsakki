<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>T. Kamal Esakki | Portfolio</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- AOS Animation Library -->
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Poppins', 'sans-serif'],
                    },
                    colors: {
                        dark: '#0a0f0d',
                        card: '#111a16',
                        emeraldAccent: '#10b981',
                    }
                }
            }
        }
    </script>

    <style>
        body {
            background-color: #0a0f0d;
            color: #e2e8f0;
            overflow-x: hidden;
        }
        /* Floating Photo Animation */
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-15px); }
            100% { transform: translateY(0px); }
        }
        .animate-float {
            animation: float 4s ease-in-out infinite;
        }
        /* Glowing Border Effect */
        .glow-box {
            box-shadow: 0 0 25px rgba(16, 185, 129, 0.3);
            transition: all 0.3s ease-in-out;
        }
        .glow-box:hover {
            box-shadow: 0 0 40px rgba(16, 185, 129, 0.6);
            transform: translateY(-5px);
        }
        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0a0f0d;
        }
        ::-webkit-scrollbar-thumb {
            background: #10b981;
            border-radius: 4px;
        }
    </style>
</head>
<body class="font-sans antialiased selection:bg-emerald-500 selection:text-white">

    <!-- Navbar -->
    <nav class="fixed w-full z-50 bg-dark/80 backdrop-blur-md border-b border-emerald-900/40">
        <div class="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
            <a href="#" class="text-2xl font-bold text-white tracking-wider">
                KAMAL<span class="text-emerald-500">.DEV</span>
            </a>
            <div class="hidden md:flex space-x-8 text-sm font-medium">
                <a href="#home" class="hover:text-emerald-400 transition">Home</a>
                <a href="#skills" class="hover:text-emerald-400 transition">Skills</a>
                <a href="#experience" class="hover:text-emerald-400 transition">Experience</a>
                <a href="#projects" class="hover:text-emerald-400 transition">Projects</a>
                <a href="#education" class="hover:text-emerald-400 transition">Education</a>
                <a href="#contact" class="hover:text-emerald-400 transition">Contact</a>
            </div>
            <a href="mailto:kamalesakki11@gmail.com" class="bg-emerald-600 hover:bg-emerald-500 text-white px-5 py-2 rounded-full text-sm font-semibold transition shadow-lg shadow-emerald-600/30">
                Hire Me
            </a>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="min-h-screen flex items-center justify-center pt-20 px-6">
        <div class="max-w-6xl mx-auto grid md:grid-cols-2 gap-12 items-center">
            
            <!-- Left Text -->
            <div data-aos="fade-right" data-aos-duration="1000">
                <p class="text-emerald-400 font-semibold tracking-widest uppercase text-sm mb-2">Welcome to my portfolio</p>
                <h1 class="text-4xl md:text-6xl font-bold text-white leading-tight mb-4">
                    Hi, I'm <br>
                    <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-teal-200">T. Kamal Esakki</span>
                </h1>
                <h2 class="text-xl md:text-2xl text-gray-300 font-medium mb-6">
                    <span id="typewriter" class="text-emerald-400 font-semibold"></span>
                </h2>
                <p class="text-gray-400 leading-relaxed mb-8">
                    Computer Science graduate with hands-on experience in full-stack development, REST API development, authentication, and database management[cite: 4]. Proficient in Python, JavaScript, SQL, React.js, Node.js, and PostgreSQL[cite: 4].
                </p>
                
                <!-- Social & Action Buttons -->
                <div class="flex flex-wrap gap-4 items-center">
                    <a href="#projects" class="bg-emerald-500 hover:bg-emerald-400 text-dark font-bold px-7 py-3 rounded-full transition transform hover:scale-105">
                        View My Work
                    </a>
                    <a href="https://www.linkedin.com/in/kamalesakki" target="_blank" class="border border-emerald-500/50 hover:border-emerald-400 p-3 rounded-full text-emerald-400 hover:bg-emerald-500/10 transition">
                        <i class="fab fa-linkedin-in text-xl w-6 h-6 text-center"></i>
                    </a>
                    <a href="https://github.com/KamalEsakki" target="_blank" class="border border-emerald-500/50 hover:border-emerald-400 p-3 rounded-full text-emerald-400 hover:bg-emerald-500/10 transition">
                        <i class="fab fa-github text-xl w-6 h-6 text-center"></i>
                    </a>
                    <a href="mailto:kamalesakki11@gmail.com" class="border border-emerald-500/50 hover:border-emerald-400 p-3 rounded-full text-emerald-400 hover:bg-emerald-500/10 transition">
                        <i class="fas fa-envelope text-xl w-6 h-6 text-center"></i>
                    </a>
                </div>
            </div>

            <!-- Right Image -->
            <div class="flex justify-center" data-aos="zoom-in" data-aos-duration="1200">
                <div class="relative w-72 h-72 md:w-96 md:h-96 animate-float">
                    <div class="absolute inset-0 bg-gradient-to-tr from-emerald-600 to-teal-400 rounded-full blur-2xl opacity-40 animate-pulse"></div>
                    <img src="profile.jpg" alt="T. Kamal Esakki" class="relative w-full h-full object-cover rounded-full border-4 border-emerald-500 shadow-2xl">
                </div>
            </div>

        </div>
    </section>

    <!-- Technical Skills Section -->
    <section id="skills" class="py-20 px-6 bg-card/50">
        <div class="max-w-6xl mx-auto">
            <div class="text-center mb-16" data-aos="fade-up">
                <h2 class="text-3xl md:text-4xl font-bold text-white">Technical <span class="text-emerald-400">Skills</span></h2>
                <div class="w-20 h-1 bg-emerald-500 mx-auto mt-3 rounded"></div>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="bg-card p-6 rounded-2xl border border-emerald-900/40 glow-box" data-aos="fade-up" data-aos-delay="100">
                    <i class="fas fa-code text-3xl text-emerald-400 mb-4"></i>
                    <h3 class="text-xl font-bold text-white mb-3">Programming & Core</h3>
                    <div class="flex flex-wrap gap-2">
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Python</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">JavaScript</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">TypeScript</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">SQL & COQL</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Java (Beginner)</span>
                    </div>
                </div>

                <div class="bg-card p-6 rounded-2xl border border-emerald-900/40 glow-box" data-aos="fade-up" data-aos-delay="200">
                    <i class="fas fa-laptop-code text-3xl text-emerald-400 mb-4"></i>
                    <h3 class="text-xl font-bold text-white mb-3">Frontend Development</h3>
                    <div class="flex flex-wrap gap-2">
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">HTML</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">CSS</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">React.js</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Next.js</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Tailwind CSS</span>
                    </div>
                </div>

                <div class="bg-card p-6 rounded-2xl border border-emerald-900/40 glow-box" data-aos="fade-up" data-aos-delay="300">
                    <i class="fas fa-server text-3xl text-emerald-400 mb-4"></i>
                    <h3 class="text-xl font-bold text-white mb-3">Backend & APIs</h3>
                    <div class="flex flex-wrap gap-2">
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Node.js</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Express.js</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Nest.js</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">REST APIs</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">CRUD Operations</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">API Integration</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Error Handling</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Data Migration</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Webhooks</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">MCP Server Development</span>
                    </div>
                </div>

                <div class="bg-card p-6 rounded-2xl border border-emerald-900/40 glow-box" data-aos="fade-up" data-aos-delay="400">
                    <i class="fas fa-shield-alt text-3xl text-emerald-400 mb-4"></i>
                    <h3 class="text-xl font-bold text-white mb-3">Authentication & Security</h3>
                    <div class="flex flex-wrap gap-2">
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">JWT Authentication</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">OAuth 2.0</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Google OAuth</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Role-Based Authorization</span>
                    </div>
                </div>

                <div class="bg-card p-6 rounded-2xl border border-emerald-900/40 glow-box" data-aos="fade-up" data-aos-delay="500">
                    <i class="fas fa-database text-3xl text-emerald-400 mb-4"></i>
                    <h3 class="text-xl font-bold text-white mb-3">Databases</h3>
                    <div class="flex flex-wrap gap-2">
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">MongoDB</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">MySQL</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">PostgreSQL</span>
                    </div>
                </div>

                <div class="bg-card p-6 rounded-2xl border border-emerald-900/40 glow-box" data-aos="fade-up" data-aos-delay="600">
                    <i class="fas fa-tools text-3xl text-emerald-400 mb-4"></i>
                    <h3 class="text-xl font-bold text-white mb-3">Data Analytics & Tools</h3>
                    <div class="flex flex-wrap gap-2">
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Data Analysis & EDA</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Pandas & NumPy</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Streamlit</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Docker</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">n8n (Workflow Automation)</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">ngrok</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">GitHub & GitLab</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">UiPath RPA</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Power BI</span>
                        <span class="bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full text-sm">Google Cloud Platform</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Experience & Achievements Section -->
    <section id="experience" class="py-20 px-6">
        <div class="max-w-6xl mx-auto grid md:grid-cols-2 gap-12">
            
            <!-- Work Experience -->
            <div data-aos="fade-right">
                <h2 class="text-3xl font-bold text-white mb-8"><i class="fas fa-briefcase text-emerald-400 mr-3"></i>Experience</h2>
                
                <div class="space-y-6">
                    <!-- Zeeyes AI Labs -->
                    <div class="bg-card p-6 rounded-2xl border-l-4 border-emerald-500 glow-box">
                        <div class="flex justify-between items-center flex-wrap gap-2 mb-2">
                            <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 bg-emerald-950 px-3 py-1 rounded-full">Present</span>
                            <span class="text-xs text-teal-300 bg-teal-950/60 px-3 py-1 rounded-full border border-teal-800/50">Product-based Company</span>
                        </div>
                        <h3 class="text-xl font-bold text-white mt-1">Backend Developer Intern (Node.js & NestJS)</h3>
                        <p class="text-emerald-300 text-sm mb-3">Zeeyes AI Labs</p>
                        <ul class="text-gray-400 text-sm space-y-2 list-disc list-inside">
                            <li>Developing robust backend architectures and high-performance RESTful APIs using Node.js, Express.js, and NestJS.</li>
                            <li>Implementing secure authentication & authorization workflows including JWT, OAuth 2.0, Google OAuth, and Role-Based Access Control (RBAC).</li>
                            <li>Integrating third-party APIs and enterprise platforms like Zoho CRM, HubSpot, QuickBooks, and MCP (Model Context Protocol).</li>
                            <li>Managing database operations and ORMs like PostgreSQL, MySQL, TypeORM, and SQLAlchemy with Dockerized environments.</li>
                        </ul>
                    </div>

                    <!-- Extazee Software Solution -->
                    <div class="bg-card p-6 rounded-2xl border-l-4 border-teal-600 glow-box">
                        <span class="text-xs font-bold uppercase tracking-wider text-teal-400 bg-teal-950 px-3 py-1 rounded-full">Jun 2025 - Jul 2025</span>
                        <h3 class="text-xl font-bold text-white mt-3">Data Science Intern</h3>
                        <p class="text-teal-300 text-sm mb-3">Extazee Software Solution, Trichy</p>
                        <ul class="text-gray-400 text-sm space-y-2 list-disc list-inside">
                            <li>Applied Python and data science libraries for data preprocessing, exploratory analysis, and visualization to insights from datasets[cite: 4].</li>
                            <li>Developed data science mini-projects using Python libraries, strengthening practical skills in data analysis, visualization, and problem solving[cite: 4].</li>
                            <li>Received recognition for dedication and performance during the internship[cite: 4].</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Achievements -->
            <div data-aos="fade-left">
                <h2 class="text-3xl font-bold text-white mb-8"><i class="fas fa-trophy text-emerald-400 mr-3"></i>Achievements</h2>
                <div class="bg-card p-6 rounded-2xl border-l-4 border-emerald-500 glow-box space-y-4">
                    <div>
                        <h3 class="text-lg font-bold text-white">Coordinator - INNOFEST '25</h3>
                        <p class="text-gray-400 text-sm mt-1">Organized and coordinated INNOFEST '25, a technical symposium attended by 200+ participants, managing event planning, coordination, and execution[cite: 4].</p>
                    </div>
                    <hr class="border-emerald-900/40">
                    <div>
                        <h3 class="text-lg font-bold text-white">Event Registration Web Developer</h3>
                        <p class="text-gray-400 text-sm mt-1">Developed and maintained the event registration website using HTML, CSS, and JavaScript, improving the registration workflow[cite: 4].</p>
                    </div>
                    <hr class="border-emerald-900/40">
                    <div>
                        <h3 class="text-lg font-bold text-white">Competitive Programming</h3>
                        <p class="text-gray-400 text-sm mt-1">Participated in coding competitions involving problem solving, debugging, logical reasoning, and algorithmic challenges[cite: 4].</p>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- Featured Projects Section -->
    <section id="projects" class="py-20 px-6 bg-card/50">
        <div class="max-w-6xl mx-auto">
            <div class="text-center mb-16" data-aos="fade-up">
                <h2 class="text-3xl md:text-4xl font-bold text-white">Featured <span class="text-emerald-400">Projects</span></h2>
                <div class="w-20 h-1 bg-emerald-500 mx-auto mt-3 rounded"></div>
            </div>

            <div class="grid md:grid-cols-3 gap-8">
                
                <!-- Project 1 -->
                <div class="bg-card rounded-2xl p-6 border border-emerald-900/40 flex flex-col justify-between glow-box" data-aos="flip-left" data-aos-delay="100">
                    <div>
                        <div class="flex justify-between items-center mb-4">
                            <i class="fas fa-chart-pie text-3xl text-emerald-400"></i>
                            <a href="https://github.com/marikannan234/stock entinal" target="_blank" class="text-gray-400 hover:text-emerald-400"><i class="fab fa-github text-2xl"></i></a>
                        </div>
                        <h3 class="text-xl font-bold text-white mb-2">Stock Sentinel Stock Monitoring System</h3>
                        <p class="text-gray-400 text-sm mb-4">
                            Developed a stock monitoring web application for portfolio and watchlist tracking using Next.js, Tailwind CSS, Recharts, and Docker, with a FastAPI, PostgreSQL, SQLAlchemy backend secured by JWT Authentication[cite: 4].
                        </p>
                    </div>
                    <div class="flex flex-wrap gap-2 mt-4 pt-4 border-t border-emerald-900/30 text-xs text-emerald-300">
                        <span>#Next.js</span> <span>#FastAPI</span> <span>#PostgreSQL</span> <span>#Docker</span> <span>#Recharts</span>
                    </div>
                </div>

                <!-- Project 2 -->
                <div class="bg-card rounded-2xl p-6 border border-emerald-900/40 flex flex-col justify-between glow-box" data-aos="flip-left" data-aos-delay="200">
                    <div>
                        <div class="flex justify-between items-center mb-4">
                            <i class="fas fa-shopping-bag text-3xl text-emerald-400"></i>
                            <a href="https://github.com/KamalEsakki/Ecommerce-Customer-Behavior-Analysis" target="_blank" class="text-gray-400 hover:text-emerald-400"><i class="fab fa-github text-2xl"></i></a>
                        </div>
                        <h3 class="text-xl font-bold text-white mb-2">E-Commerce Customer Analysis</h3>
                        <p class="text-gray-400 text-sm mb-4">
                            Conducted data preprocessing, EDA, and customer segmentation using Python and Pandas; applied K-Means, DBSCAN, and Apriori to develop clustering and recommendation insights through an interactive Streamlit application[cite: 4].
                        </p>
                    </div>
                    <div class="flex flex-wrap gap-2 mt-4 pt-4 border-t border-emerald-900/30 text-xs text-emerald-300">
                        <span>#Python</span> <span>#Pandas</span> <span>#Streamlit</span> <span>#MachineLearning</span>
                    </div>
                </div>

                <!-- Project 3 -->
                <div class="bg-card rounded-2xl p-6 border border-emerald-900/40 flex flex-col justify-between glow-box" data-aos="flip-left" data-aos-delay="300">
                    <div>
                        <div class="flex justify-between items-center mb-4">
                            <i class="fas fa-exchange-alt text-3xl text-emerald-400"></i>
                        </div>
                        <h3 class="text-xl font-bold text-white mb-2">Zoho CRM to HubSpot Migration & MCP Integration</h3>
                        <p class="text-gray-400 text-sm mb-4">
                            Developed CRM migration using Nest.JS, PostgreSQL, and REST APIs, implementing contact synchronization, OAuth 2.0, duplicate handling, n8n workflow automation, and MCP-based AI agent integration for CRM operations[cite: 4].
                        </p>
                    </div>
                    <div class="flex flex-wrap gap-2 mt-4 pt-4 border-t border-emerald-900/30 text-xs text-emerald-300">
                        <span>#Nest.js</span> <span>#PostgreSQL</span> <span>#OAuth2.0</span> <span>#n8n</span> <span>#MCP</span>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Education & Certifications -->
    <section id="education" class="py-20 px-6">
        <div class="max-w-6xl mx-auto grid md:grid-cols-2 gap-12">
            
            <!-- Education -->
            <div data-aos="fade-up">
                <h2 class="text-3xl font-bold text-white mb-8"><i class="fas fa-graduation-cap text-emerald-400 mr-3"></i>Education</h2>
                <div class="space-y-6 border-l-2 border-emerald-500 pl-6">
                    <div class="relative">
                        <div class="absolute -left-8 top-1 w-4 h-4 bg-emerald-500 rounded-full"></div>
                        <h3 class="text-lg font-bold text-white">B.E. Computer Science and Engineering</h3>
                        <p class="text-emerald-400 text-sm">Unnamalai Institute of Technology (Affiliated to Anna University, Chennai) (2022 - 2026)[cite: 4]</p>
                        <p class="text-gray-400 text-sm mt-1">CGPA: 7.77[cite: 4]</p>
                    </div>
                    <div class="relative">
                        <div class="absolute -left-8 top-1 w-4 h-4 bg-emerald-500 rounded-full"></div>
                        <h3 class="text-lg font-bold text-white">Higher Secondary (HSC)</h3>
                        <p class="text-emerald-400 text-sm">St. Xavier's Higher Secondary School (2022)[cite: 4]</p>
                        <p class="text-gray-400 text-sm mt-1">Score: 60%[cite: 4]</p>
                    </div>
                    <div class="relative">
                        <div class="absolute -left-8 top-1 w-4 h-4 bg-emerald-500 rounded-full"></div>
                        <h3 class="text-lg font-bold text-white">SSLC</h3>
                        <p class="text-emerald-400 text-sm">Kathi Vidyalaya Matriculation School (2020)[cite: 4]</p>
                        <p class="text-gray-400 text-sm mt-1">Score: 87%[cite: 4]</p>
                    </div>
                </div>
            </div>

            <!-- Certifications -->
            <div data-aos="fade-up" data-aos-delay="200">
                <h2 class="text-3xl font-bold text-white mb-8"><i class="fas fa-certificate text-emerald-400 mr-3"></i>Certifications</h2>
                <div class="grid grid-cols-1 gap-4">
                    <div class="bg-card p-4 rounded-xl border border-emerald-900/40 flex items-center gap-4">
                        <i class="fas fa-check-circle text-emerald-400 text-xl"></i>
                        <span class="text-gray-200 font-medium text-sm">Data Analytics Master Program Certification</span>
                    </div>
                    <div class="bg-card p-4 rounded-xl border border-emerald-900/40 flex items-center gap-4">
                        <i class="fas fa-check-circle text-emerald-400 text-xl"></i>
                        <span class="text-gray-200 font-medium text-sm">Google Cloud Cybersecurity Certification</span>
                    </div>
                    <div class="bg-card p-4 rounded-xl border border-emerald-900/40 flex items-center gap-4">
                        <i class="fas fa-check-circle text-emerald-400 text-xl"></i>
                        <span class="text-gray-200 font-medium text-sm">IBM Experience Based Project Learning</span>
                    </div>
                    <div class="bg-card p-4 rounded-xl border border-emerald-900/40 flex items-center gap-4">
                        <i class="fas fa-check-circle text-emerald-400 text-xl"></i>
                        <span class="text-gray-200 font-medium text-sm">UiPath RPA Certification</span>
                    </div>
                    <div class="bg-card p-4 rounded-xl border border-emerald-900/40 flex items-center gap-4">
                        <i class="fas fa-check-circle text-emerald-400 text-xl"></i>
                        <span class="text-gray-200 font-medium text-sm">Cambridge University Communication Skills</span>
                    </div>
                    <div class="bg-card p-4 rounded-xl border border-emerald-900/40 flex items-center gap-4">
                        <i class="fas fa-check-circle text-emerald-400 text-xl"></i>
                        <span class="text-gray-200 font-medium text-sm">Salesforce CRM Jewellery Management</span>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- Contact Footer -->
    <footer id="contact" class="bg-card border-t border-emerald-900/40 py-12 px-6 text-center">
        <div class="max-w-4xl mx-auto" data-aos="zoom-in">
            <h2 class="text-3xl font-bold text-white mb-4">Let's Connect!</h2>
            <p class="text-gray-400 mb-6">Open for entry-level software or data-focused opportunities[cite: 2].</p>
            <div class="flex flex-wrap justify-center gap-6 mb-8 text-sm">
                <a href="mailto:kamalesakki11@gmail.com" class="flex items-center gap-2 text-emerald-400 hover:underline">
                    <i class="fas fa-envelope"></i> kamalesakki11@gmail.com
                </a>
                <a href="tel:9025857346" class="flex items-center gap-2 text-emerald-400 hover:underline">
                    <i class="fas fa-phone"></i> +91 9025857346
                </a>
                <a href="https://www.linkedin.com/in/kamalesakki" target="_blank" class="flex items-center gap-2 text-emerald-400 hover:underline">
                    <i class="fab fa-linkedin"></i> linkedin.com/in/kamalesakki
                </a>
            </div>
            <p class="text-gray-600 text-xs">© 2026 T. Kamal Esakki. All rights reserved.</p>
        </div>
    </footer>

    <!-- Scripts for Animations -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script src="https://unpkg.com/typed.js@2.0.16/dist/typed.umd.js"></script>
    <script>
        // Initialize Scroll Animations
        AOS.init({
            once: false,
            mirror: true,
        });

        // Initialize Typewriter Effect
        new Typed('#typewriter', {
            strings: ['Full-Stack & Backend Developer', 'NestJS & Node.js Specialist', 'Data Analyst & Problem Solver'],
            typeSpeed: 60,
            backSpeed: 40,
            loop: true
        });
    </script>
</body>
</html>
