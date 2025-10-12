<script setup>
import Navbar from "@/shared/components/Navbar.vue";
import { Card, CardHeader, CardContent } from "@/shared/components/ui/card";
import { Shield, Lock, FileText, Globe, Mail, User } from "lucide-vue-next";
</script>

<template>
    <div>
        <Navbar variant="app" />
        <section id="privacy"
            class="bg-gradient-to-b from-gray-50/50 to-white dark:from-gray-900/50 dark:to-background py-20 md:py-32">
            <div class="w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto">
                <div class="text-center mb-16">
                    <h1 class="text-4xl md:text-5xl font-bold mb-6">
                        Política de
                        <span
                            class="text-transparent bg-gradient-to-r from-[#4ed636] to-[#048044] bg-clip-text">Privacidad</span>
                    </h1>
                    <p class="text-lg text-muted-foreground max-w-3xl mx-auto leading-relaxed">
                        En <strong>JOM</strong> valoramos tu confianza. Esta política describe cómo recopilamos,
                        usamos y protegemos tu información personal conforme a la
                        <strong>Ley Federal de Protección de Datos Personales en Posesión de los Particulares
                            (LFPDPPP)</strong>.
                    </p>
                </div>

                <div class="space-y-10">
                    <Card
                        class="border-2 hover:border-[#4ed636]/20 bg-gradient-to-br from-white to-gray-50/50 dark:from-gray-900 dark:to-gray-800/50 transition-all duration-500 hover:shadow-xl hover:-translate-y-1">
                        <CardHeader class="flex items-center gap-3">
                            <Shield class="w-8 h-8 text-[#4ed636]" />
                            <h2 class="text-2xl font-bold text-foreground">1. Responsable del tratamiento de datos</h2>
                        </CardHeader>
                        <CardContent class="text-muted-foreground leading-relaxed">
                            <p>
                                <strong>Refaccionaria JOM</strong> (en adelante, “JOM”), con domicilio en <em>Calle Fray
                                    Servando T. de M. Ote. 211, Barrio Alto, 99070 Fresnillo, Zac.</em>,
                                es responsable del uso y protección de los datos personales recabados a través de su
                                portal
                                web y sistema de cotización.
                            </p>
                            <p class="mt-3">
                                Para cualquier duda o solicitud relacionada con sus datos personales, puede contactarnos
                                al
                                correo:
                                <a href="mailto:privacidad@jomrefacciones.com"
                                    class="text-[#048044] font-semibold hover:underline">
                                    privacidad@jomrefacciones.com
                                </a>.
                            </p>
                        </CardContent>
                    </Card>

                    <Card
                        class="border-2 hover:border-[#4ed636]/20 bg-gradient-to-br from-white to-gray-50/50 dark:from-gray-900 dark:to-gray-800/50 transition-all duration-500 hover:shadow-xl hover:-translate-y-1">
                        <CardHeader class="flex items-center gap-3">
                            <User class="w-8 h-8 text-[#4ed636]" />
                            <h2 class="text-2xl font-bold text-foreground">2. Datos personales que recabamos</h2>
                        </CardHeader>
                        <CardContent class="text-muted-foreground leading-relaxed">
                            <p>
                                JOM podrá solicitar los siguientes datos personales, de manera enunciativa mas no
                                limitativa:
                            </p>
                            <ul class="list-disc pl-6 mt-3 space-y-1">
                                <li>Nombre completo y datos de contacto (correo electrónico, teléfono)</li>
                                <li>Empresa o razón social</li>
                                <li>Datos de facturación y entrega</li>
                                <li>Historial de cotizaciones y pedidos</li>
                                <li>Información técnica (IP, navegador, dispositivo, cookies)</li>
                            </ul>
                            <p class="mt-3">
                                Estos datos son utilizados exclusivamente para fines comerciales legítimos relacionados
                                con
                                la prestación de nuestros servicios.
                            </p>
                        </CardContent>
                    </Card>

                    <Card
                        class="border-2 hover:border-[#4ed636]/20 bg-gradient-to-br from-white to-gray-50/50 dark:from-gray-900 dark:to-gray-800/50 transition-all duration-500 hover:shadow-xl hover:-translate-y-1">
                        <CardHeader class="flex items-center gap-3">
                            <Globe class="w-8 h-8 text-[#4ed636]" />
                            <h2 class="text-2xl font-bold text-foreground">3. Finalidades del tratamiento</h2>
                        </CardHeader>
                        <CardContent class="text-muted-foreground leading-relaxed space-y-3">
                            <p>Los datos personales se utilizan para las siguientes finalidades:</p>

                            <p class="font-semibold text-foreground">Finalidades primarias</p>
                            <ul class="list-disc pl-6 space-y-1">
                                <li>Gestionar y generar cotizaciones solicitadas por los usuarios.</li>
                                <li>Enviar cotizaciones por correo electrónico o WhatsApp.</li>
                                <li>Registrar clientes y solicitudes de alta.</li>
                                <li>Cumplir con obligaciones derivadas de una relación comercial.</li>
                            </ul>

                            <p class="font-semibold text-foreground mt-3">Finalidades secundarias</p>
                            <ul class="list-disc pl-6 space-y-1">
                                <li>Enviar promociones, noticias o encuestas de satisfacción.</li>
                                <li>Analizar métricas del sistema para mejorar la experiencia de usuario.</li>
                                <li>Generar reportes estadísticos internos sin identificar individualmente a los
                                    usuarios.
                                </li>
                            </ul>

                            <p class="mt-3">
                                Si no desea que sus datos se utilicen para finalidades secundarias, puede manifestarlo
                                enviando un correo a
                                <a href="mailto:privacidad@jomrefacciones.com"
                                    class="text-[#048044] font-semibold hover:underline">
                                    privacidad@jomrefacciones.com
                                </a>.
                            </p>
                        </CardContent>
                    </Card>

                    <Card
                        class="border-2 hover:border-[#4ed636]/20 bg-gradient-to-br from-white to-gray-50/50 dark:from-gray-900 dark:to-gray-800/50 transition-all duration-500 hover:shadow-xl hover:-translate-y-1">
                        <CardHeader class="flex items-center gap-3">
                            <FileText class="w-8 h-8 text-[#4ed636]" />
                            <h2 class="text-2xl font-bold text-foreground">4. Uso de cookies y tecnologías similares
                            </h2>
                        </CardHeader>
                        <CardContent class="text-muted-foreground leading-relaxed">
                            <p>
                                Este sitio utiliza cookies y herramientas analíticas para mejorar la experiencia del
                                usuario, personalizar contenido y analizar el tráfico.
                                Puede deshabilitar las cookies desde la configuración de su navegador, sin embargo,
                                algunas
                                funciones podrían no estar disponibles.
                            </p>
                        </CardContent>
                    </Card>

                    <Card
                        class="border-2 hover:border-[#4ed636]/20 bg-gradient-to-br from-white to-gray-50/50 dark:from-gray-900 dark:to-gray-800/50 transition-all duration-500 hover:shadow-xl hover:-translate-y-1">
                        <CardHeader class="flex items-center gap-3">
                            <Lock class="w-8 h-8 text-[#4ed636]" />
                            <h2 class="text-2xl font-bold text-foreground">5. Transferencia y seguridad de datos</h2>
                        </CardHeader>
                        <CardContent class="text-muted-foreground leading-relaxed">
                            <p>
                                JOM no transfiere datos personales a terceros sin su consentimiento, salvo en los
                                siguientes
                                casos:
                            </p>
                            <ul class="list-disc pl-6 mt-3 space-y-1">
                                <li>Para cumplir con obligaciones legales o contractuales.</li>
                                <li>Con proveedores que brinden servicios de alojamiento, mensajería o soporte técnico.
                                </li>
                                <li>Para integración con sistemas administrativos internos como Microsip, garantizando
                                    la
                                    seguridad de la información.</li>
                            </ul>
                            <p class="mt-3">
                                Implementamos medidas administrativas, técnicas y físicas para proteger los datos
                                personales
                                contra pérdida, uso indebido o acceso no autorizado.
                            </p>
                        </CardContent>
                    </Card>

                    <Card
                        class="border-2 hover:border-[#4ed636]/20 bg-gradient-to-br from-white to-gray-50/50 dark:from-gray-900 dark:to-gray-800/50 transition-all duration-500 hover:shadow-xl hover:-translate-y-1">
                        <CardHeader class="flex items-center gap-3">
                            <Mail class="w-8 h-8 text-[#4ed636]" />
                            <h2 class="text-2xl font-bold text-foreground">6. Derechos ARCO</h2>
                        </CardHeader>
                        <CardContent class="text-muted-foreground leading-relaxed">
                            <p>
                                Puede ejercer sus derechos de Acceso, Rectificación, Cancelación u Oposición enviando
                                una
                                solicitud al correo:
                                <a href="mailto:privacidad@jomrefacciones.com"
                                    class="text-[#048044] font-semibold hover:underline">
                                    privacidad@jomrefacciones.com
                                </a>.
                            </p>
                            <p class="mt-3">
                                Su solicitud deberá incluir nombre completo, medio de contacto y descripción de los
                                datos
                                sobre los que desea ejercer el derecho.
                                JOM responderá en un plazo máximo de <strong>20 días hábiles</strong>.
                            </p>
                        </CardContent>
                    </Card>

                    <Card
                        class="border-2 hover:border-[#4ed636]/20 bg-gradient-to-br from-white to-gray-50/50 dark:from-gray-900 dark:to-gray-800/50 transition-all duration-500 hover:shadow-xl hover:-translate-y-1">
                        <CardHeader class="flex items-center gap-3">
                            <Shield class="w-8 h-8 text-[#4ed636]" />
                            <h2 class="text-2xl font-bold text-foreground">7. Modificaciones a esta política</h2>
                        </CardHeader>
                        <CardContent class="text-muted-foreground leading-relaxed">
                            <p>
                                JOM se reserva el derecho de modificar esta Política de Privacidad en cualquier momento.
                                Las actualizaciones se publicarán en el sitio web oficial y entrarán en vigor a partir
                                de su
                                publicación.
                            </p>
                        </CardContent>
                    </Card>

                    <Card
                        class="border-2 hover:border-[#4ed636]/20 bg-gradient-to-br from-white to-gray-50/50 dark:from-gray-900 dark:to-gray-800/50 transition-all duration-500 hover:shadow-xl hover:-translate-y-1">
                        <CardHeader class="flex items-center gap-3">
                            <Globe class="w-8 h-8 text-[#4ed636]" />
                            <h2 class="text-2xl font-bold text-foreground">8. Autoridad competente</h2>
                        </CardHeader>
                        <CardContent class="text-muted-foreground leading-relaxed">
                            <p>
                                Si considera que su derecho de protección de datos ha sido vulnerado, puede acudir al
                                <strong>Instituto Nacional de Transparencia, Acceso a la Información y Protección de
                                    Datos
                                    Personales (INAI)</strong>
                                a través de su sitio web:
                                <a href="https://www.inai.org.mx" target="_blank"
                                    class="text-[#048044] font-semibold hover:underline">
                                    www.inai.org.mx
                                </a>.
                            </p>
                        </CardContent>
                    </Card>
                </div>

                <div class="mt-16 text-center text-sm text-muted-foreground">
                    <p>Última actualización: 8 de octubre de 2025 · © JOM Refacciones. Todos los derechos reservados.
                    </p>
                </div>
            </div>
        </section>
    </div>
</template>
