{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "aws.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "aws.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "aws.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "aws.labels" -}}
helm.sh/chart: {{ include "aws.chart" . }}
{{ include "aws.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
aws Selector labels
*/}}
{{- define "aws.selectorLabels" -}}
app.kubernetes.io/name: {{ include "aws.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "aws.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "aws.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}

{{- define "worker.serviceAccountName" -}}
{{- if .Values.worker.serviceAccount.create }}
{{- default "default" .Values.worker.serviceAccount.name }}
{{- end }}
{{- end }}


{{/*
Create the ingress hostname
*/}}
{{- define "aws.ingressHostname" -}}
{{- if .Values.ingress.hostname }}
{{- .Values.ingress.hostname }}
{{- else }}
{{- if eq .Values.global.environment "dev" }}
{{- printf "aws.%s.ankra.cloud" .Release.Namespace }}
{{- end }}
{{- if eq .Values.global.environment "local" }}
{{- printf "aws.local.app" }}
{{- end }}
{{- end }}
{{- end }}
