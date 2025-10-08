<script setup>
import { Card, CardContent } from '@/shared/components/ui/card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/shared/components/ui/table';
import { ref } from 'vue'

</script>

<template>
    <div>
        <div>
            <h2 class="text-3xl font-bold">Gestión de solicitudes</h2>
            <p class="text-muted-foreground mt-2">
                Administra usuarios, revisa metricas y gestiona el sistema
            </p>
        </div>

        <Card>
            <CardContent>
                <Table>
                    <TableHeader>
                        <TableRow>
                            <TableHead class="w-[100px]">
                                Invoice
                            </TableHead>
                            <TableHead>Status</TableHead>
                            <TableHead>Method</TableHead>
                            <TableHead class="text-right">
                                Amount
                            </TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        <TableRow v-for="invoice in invoices" :key="invoice.invoice">
                            <TableCell class="font-medium">
                                {{ invoice.invoice }}
                            </TableCell>
                            <TableCell>{{ invoice.paymentStatus }}</TableCell>
                            <TableCell>{{ invoice.paymentMethod }}</TableCell>
                            <TableCell class="text-right">
                                {{ invoice.totalAmount }}
                            </TableCell>
                        </TableRow>
                    </TableBody>
                </Table>
            </CardContent>
        </Card>
    </div>
</template>