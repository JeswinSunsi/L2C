<script setup>
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';

const router = useRouter();
const authStore = useAuthStore();

const startLearning = () => {
  if (authStore.isAuthenticated) {
    router.push('/dashboard');
  } else {
    router.push('/register');
  }
};

onMounted(() => {
  // Typewriter effect
  const text = "def learn_to_code():\n    curiosity = True\n    while curiosity:\n        explore()\n        build()\n        deploy()";
  const typeWriterElement = document.getElementById('typewriter');
  let i = 0;
  
  if (typeWriterElement) {
    function type() {
      if (i < text.length) {
        typeWriterElement.innerHTML += text.charAt(i) === '\n' ? '<br>' : text.charAt(i);
        i++;
        setTimeout(type, 50);
      }
    }
    type();
  }

  // Terminal effect
  setTimeout(() => {
    const el = document.getElementById('term-line-1');
    if(el) el.classList.remove('opacity-0');
  }, 1000);
  setTimeout(() => {
    const el = document.getElementById('term-line-2');
    if(el) el.classList.remove('opacity-0');
  }, 2000);
  setTimeout(() => {
    const el = document.getElementById('term-line-3');
    if(el) el.classList.remove('opacity-0');
    
    const badge = document.getElementById('success-badge');
    if(badge) badge.classList.remove('scale-0');
  }, 3000);

  // Scroll Reveal
  const observerOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.1
  };

  const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
          if (entry.isIntersecting) {
              entry.target.classList.add('active');
              observer.unobserve(entry.target);
          }
      });
  }, observerOptions);

  document.querySelectorAll('.reveal').forEach(el => {
      observer.observe(el);
  });
});
</script>

<template>
  <div class="text-slate-800 font-sans antialiased selection:bg-accent-indigo selection:text-white overflow-x-hidden">
    <nav class="fixed w-full z-50 bg-white/80 backdrop-blur-md border-b border-slate-200/60 supports-[backdrop-filter]:bg-white/60">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 bg-slate-900 rounded-lg flex items-center justify-center text-white font-mono font-bold text-lg shadow-lg shadow-slate-900/20">
                        &lt;/&gt;
                    </div>
                    <span class="font-display font-bold text-xl tracking-tight text-slate-900">PolyGlot_Lab</span>
                </div>
                
                <div class="hidden md:flex items-center gap-4">
                    <button @click="startLearning" class="px-6 py-2.5 text-sm font-bold text-white bg-slate-900 rounded-lg hover:bg-accent-indigo transition-colors shadow-lg shadow-slate-900/10">
                        Start Coding
                    </button>
                </div>
            </div>
        </div>
    </nav>


    <section class="pt-32 pb-20 lg:pt-48 lg:pb-32 relative w-full max-w-[100vw]">
        <div class="absolute inset-0 overflow-hidden pointer-events-none -z-10">
            <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-accent-indigo rounded-full mix-blend-multiply filter blur-3xl animate-blob opacity-20"></div>
            <div class="absolute top-0 right-80 w-[500px] h-[500px] bg-accent-cyan rounded-full mix-blend-multiply filter blur-3xl animate-blob animation-delay-2000 opacity-20"></div>
            <div class="absolute -bottom-32 right-20 w-[500px] h-[500px] bg-accent-amber rounded-full mix-blend-multiply filter blur-3xl animate-blob animation-delay-4000 opacity-20"></div>
        </div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center">
                
                <div class="relative z-10 max-w-2xl reveal active">
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-indigo-100 bg-indigo-50/50 backdrop-blur-sm mb-8">
                        <span class="relative flex h-2 w-2">
                          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-accent-indigo opacity-75"></span>
                          <span class="relative inline-flex rounded-full h-2 w-2 bg-accent-indigo"></span>
                        </span>
                        <span class="text-xs font-mono font-medium text-accent-indigo uppercase tracking-wider">Admissions Open v2.0</span>
                    </div>
                    
                    <h1 class="font-display text-5xl lg:text-7xl font-bold text-slate-900 leading-[1.05] mb-6 tracking-tight">
                        Decode the <br>
                        <span class="text-gradient">Language of Logic.</span>
                    </h1>
                    
                    <p class="text-lg text-slate-600 mb-8 leading-relaxed">
                        Forget dense textbooks. We've reverse-engineered computer science into interactive experiments. 
                        <span class="font-medium text-slate-900 px-1 decoration-accent-cyan underline decoration-2 underline-offset-2">Input curiosity, output mastery.</span>
                    </p>
                    
                    <div class="flex flex-col sm:flex-row gap-4">
                        <button @click="startLearning" class="px-8 py-4 text-base font-bold text-white bg-accent-indigo rounded-xl hover:bg-indigo-600 transition-all shadow-xl shadow-indigo-500/20 transform hover:-translate-y-1">
                            Initialize Learning
                        </button>
                    </div>
                </div>

                <div class="relative animate-float mx-auto w-full max-w-lg lg:max-w-none reveal active">
                    <div class="tech-card rounded-xl overflow-hidden shadow-2xl relative z-20">
                        <div class="px-4 py-3 border-b border-slate-100 bg-white flex items-center justify-between">
                            <div class="flex gap-2">
                                <div class="w-3 h-3 rounded-full bg-slate-300"></div>
                                <div class="w-3 h-3 rounded-full bg-slate-300"></div>
                                <div class="w-3 h-3 rounded-full bg-slate-300"></div>
                            </div>
                            <div class="flex gap-4 text-xs font-mono font-medium text-slate-400">
                                <span class="text-accent-indigo">main.py</span>
                                <span>utils.py</span>
                            </div>
                            <div class="w-3"></div>
                        </div>

                        <div class="flex bg-white/80 h-[320px]">
                            <div class="w-10 py-6 text-right pr-3 font-mono text-sm text-slate-300 select-none bg-slate-50/50 border-r border-slate-100 leading-7 flex-shrink-0">
                                1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10
                            </div>
                            <div class="p-6 font-mono text-sm leading-7 w-full overflow-hidden">
                                <div id="typewriter" class="text-slate-800 whitespace-pre-wrap break-words"></div>
                                <span class="cursor-blink bg-accent-indigo w-2 h-5 inline-block align-middle"></span>
                            </div>
                        </div>
                    </div>

                    <div class="absolute -bottom-10 -right-2 md:-right-6 z-30 w-56 md:w-64 bg-slate-900 rounded-lg shadow-2xl border border-slate-700 p-4 transform rotate-2 transition-transform hover:rotate-0">
                        <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
                            <span class="text-[10px] uppercase font-bold text-slate-400 tracking-wider">Terminal</span>
                            <div class="flex gap-1">
                                <div class="w-2 h-2 rounded-full bg-slate-700"></div>
                                <div class="w-2 h-2 rounded-full bg-slate-700"></div>
                            </div>
                        </div>
                        <div class="font-mono text-xs text-green-400 space-y-1">
                            <div><span class="text-slate-500">$</span> python main.py</div>
                            <div class="opacity-0 transition-opacity duration-300 delay-1000" id="term-line-1">> Initializing...</div>
                            <div class="opacity-0 transition-opacity duration-300 delay-[2000ms]" id="term-line-2">> Learning: 100%</div>
                            <div class="opacity-0 transition-opacity duration-300 delay-[3000ms] text-white" id="term-line-3">Done (0.4s)</div>
                        </div>
                    </div>

                    <div id="success-badge" class="absolute -top-6 -right-2 md:-right-6 z-30 bg-white border border-green-100 shadow-xl shadow-green-900/10 rounded-xl p-4 flex items-center gap-3 transform scale-0 transition-transform duration-500">
                        <div class="w-10 h-10 rounded-full bg-green-50 flex items-center justify-center text-green-600 ring-4 ring-green-50/50">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                        </div>
                        <div>
                            <div class="text-sm font-bold text-slate-900">Logic Verified</div>
                            <div class="text-xs font-mono text-slate-500">Ready to deploy</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="border-y border-slate-200 bg-white/50 backdrop-blur-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center divide-x divide-slate-200/50">
                <div class="reveal">
                    <div class="text-3xl font-display font-bold text-slate-900">1.2M+</div>
                    <div class="text-sm text-slate-500 font-medium mt-1 uppercase tracking-wide">Lines Written</div>
                </div>
                <div class="reveal delay-100">
                    <div class="text-3xl font-display font-bold text-slate-900">85%</div>
                    <div class="text-sm text-slate-500 font-medium mt-1 uppercase tracking-wide">Completion Rate</div>
                </div>
                <div class="reveal delay-200">
                    <div class="text-3xl font-display font-bold text-slate-900">500+</div>
                    <div class="text-sm text-slate-500 font-medium mt-1 uppercase tracking-wide">Challenges</div>
                </div>
                <div class="reveal delay-300">
                    <div class="text-3xl font-display font-bold text-slate-900">4.9/5</div>
                    <div class="text-sm text-slate-500 font-medium mt-1 uppercase tracking-wide">User Rating</div>
                </div>
            </div>
        </div>
    </section>

    <section class="pt-24 pb-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="mb-16 md:flex justify-between items-end reveal">
                <div>
                    <h2 class="font-display text-4xl font-bold text-slate-900 mb-4">Choose your architecture.</h2>
                    <p class="text-slate-600 max-w-xl text-lg">We don't just teach syntax. We teach you how to build scalable systems from day one.</p>
                </div>
            </div>

            <div class="grid md:grid-cols-3 gap-8">
                <div class="reveal delay-0">
                    <div class="tech-card rounded-2xl p-8 relative overflow-hidden group cursor-pointer h-full">
                        <div class="absolute top-0 right-0 w-32 h-32 bg-yellow-50 rounded-bl-full -mr-8 -mt-8 transition-transform group-hover:scale-110"></div>
                        <div class="relative z-10 flex flex-col h-full">
                            <div class="w-14 h-14 bg-white border border-slate-200 rounded-xl flex items-center justify-center text-3xl mb-6 shadow-sm group-hover:rotate-6 transition-transform">🐍</div>
                            <h3 class="font-display text-xl font-bold text-slate-900 mb-2">Python Intelligence</h3>
                            <p class="text-slate-500 mb-8 leading-relaxed flex-grow">Master the language of AI and Data Science. From simple scripts to neural networks.</p>
                            
                            <div class="mt-auto">
                                <div class="w-full bg-slate-100 rounded-full h-2 overflow-hidden mb-3">
                                    <div class="bg-yellow-400 h-full w-2/3 rounded-full"></div>
                                </div>
                                <div class="flex justify-between text-xs font-mono text-slate-400">
                                    <span>Beginner</span>
                                    <span>8 Modules</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="reveal delay-100">
                    <div class="tech-card rounded-2xl p-8 relative overflow-hidden group cursor-pointer border-indigo-200 ring-2 ring-indigo-50 h-full">
                        <div class="absolute top-0 right-0 w-32 h-32 bg-indigo-50 rounded-bl-full -mr-8 -mt-8 transition-transform group-hover:scale-110"></div>
                        <div class="relative z-10 flex flex-col h-full">
                            <div class="w-14 h-14 bg-white border border-slate-200 rounded-xl flex items-center justify-center text-3xl mb-6 shadow-sm group-hover:rotate-6 transition-transform">⚛️</div>
                            <h3 class="font-display text-xl font-bold text-slate-900 mb-2">React Frontend</h3>
                            <p class="text-slate-500 mb-8 leading-relaxed flex-grow">Build interactive UIs. Learn state management, hooks, and modern component design.</p>
                            
                            <div class="mt-auto">
                                <div class="w-full bg-slate-100 rounded-full h-2 overflow-hidden mb-3">
                                    <div class="bg-accent-indigo h-full w-3/4 rounded-full"></div>
                                </div>
                                <div class="flex justify-between text-xs font-mono text-slate-400">
                                    <span>Intermediate</span>
                                    <span>12 Modules</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="reveal delay-200">
                    <div class="tech-card rounded-2xl p-8 relative overflow-hidden group cursor-pointer h-full">
                        <div class="absolute top-0 right-0 w-32 h-32 bg-cyan-50 rounded-bl-full -mr-8 -mt-8 transition-transform group-hover:scale-110"></div>
                        <div class="relative z-10 flex flex-col h-full">
                            <div class="w-14 h-14 bg-white border border-slate-200 rounded-xl flex items-center justify-center text-3xl mb-6 shadow-sm group-hover:rotate-6 transition-transform">☁️</div>
                            <h3 class="font-display text-xl font-bold text-slate-900 mb-2">Cloud Backend</h3>
                            <p class="text-slate-500 mb-8 leading-relaxed flex-grow">Serverless functions, databases, and APIs. The engine room of modern apps.</p>
                            
                            <div class="mt-auto">
                                <div class="w-full bg-slate-100 rounded-full h-2 overflow-hidden mb-3">
                                    <div class="bg-accent-cyan h-full w-1/2 rounded-full"></div>
                                </div>
                                <div class="flex justify-between text-xs font-mono text-slate-400">
                                    <span>Advanced</span>
                                    <span>10 Modules</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="pb-20 pt-0 reveal">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="bg-slate-900 rounded-3xl p-12 relative overflow-hidden text-center shadow-2xl">
                <div class="absolute top-0 left-0 w-full h-full overflow-hidden">
                    <div class="absolute -top-1/2 -left-1/4 w-[800px] h-[800px] border border-slate-800 rounded-full opacity-30 animate-pulse"></div>
                    <div class="absolute -top-1/2 -right-1/4 w-[600px] h-[600px] border border-slate-700 rounded-full opacity-30"></div>
                </div>

                <div class="relative z-10">
                    <h2 class="font-display text-3xl md:text-5xl font-bold text-white mb-6">Compile Your Career.</h2>
                    <p class="text-slate-400 mb-10 max-w-xl mx-auto text-lg leading-relaxed">Join a community of builders. The compiler is ready. The tests are written. All that's missing is you.</p>
                    
                    <div class="flex flex-col sm:flex-row justify-center gap-4 max-w-md mx-auto">
                        <button @click="startLearning" class="px-8 py-4 font-bold text-slate-900 bg-white rounded-xl hover:bg-slate-200 transition-colors whitespace-nowrap shadow-lg shadow-white/10">
                            Get Access
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer class="bg-white border-t border-slate-200 pt-16 pb-8">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-8 mb-12">
                
                <div class="col-span-2 lg:col-span-2">
                    <div class="flex items-center gap-2 mb-4">
                        <div class="w-8 h-8 bg-slate-900 rounded-md flex items-center justify-center text-white font-mono font-bold text-sm">
                            &lt;/&gt;
                        </div>
                        <span class="font-display font-bold text-xl tracking-tight text-slate-900">PolyGlot_Lab</span>
                    </div>
                    <p class="text-slate-500 text-sm leading-relaxed max-w-xs mb-6">
                        Reverse-engineering computer science education. We build interactive playgrounds for the next generation of software architects.
                    </p>
                </div>

                <div>
                    <h3 class="font-bold text-slate-900 mb-4 text-sm uppercase tracking-wider">Curriculum</h3>
                    <ul class="space-y-3">
                        <li><a href="#" class="text-slate-500 hover:text-accent-indigo transition-colors text-sm">Python Logic</a></li>
                        <li><a href="#" class="text-slate-500 hover:text-accent-indigo transition-colors text-sm">React Systems</a></li>
                        <li><a href="#" class="text-slate-500 hover:text-accent-indigo transition-colors text-sm">Cloud Architecture</a></li>
                    </ul>
                </div>

                <div>
                    <h3 class="font-bold text-slate-900 mb-4 text-sm uppercase tracking-wider">Company</h3>
                    <ul class="space-y-3">
                        <li><a href="#" class="text-slate-500 hover:text-accent-indigo transition-colors text-sm">About Us</a></li>
                        <li><a href="#" class="text-slate-500 hover:text-accent-indigo transition-colors text-sm">Careers</a></li>
                    </ul>
                </div>

            </div>
            
            <div class="pt-8 border-t border-slate-100 flex flex-col md:flex-row justify-between items-center gap-4">
                <div class="text-slate-400 text-xs font-mono">
                    © 2024 PolyGlot Inc. All rights reserved.
                </div>
                <div class="flex items-center gap-2 text-xs font-medium text-slate-400">
                    <span class="w-2 h-2 rounded-full bg-green-500"></span>
                    System Status: Operational
                </div>
            </div>
        </div>
    </footer>
  </div>
</template>

<style scoped>
        body {
            background-color: #f8fafc;
            background-image: radial-gradient(#cbd5e1 1px, transparent 1px);
            background-size: 32px 32px;
        }
        
        .tech-card {
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.6);
            box-shadow: 
                0 4px 6px -1px rgba(0, 0, 0, 0.05), 
                0 10px 15px -3px rgba(0, 0, 0, 0.05),
                inset 0 0 0 1px rgba(255, 255, 255, 0.5);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .tech-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.01);
            border-color: #cbd5e1;
        }

        .cursor-blink {
            animation: blink 1s step-end infinite;
        }
        @keyframes blink { 50% { opacity: 0; } }

        .text-gradient {
            background: linear-gradient(135deg, #0f172a 0%, #4f46e5 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .reveal {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.8s cubic-bezier(0.5, 0, 0, 1);
        }

        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }
</style>
