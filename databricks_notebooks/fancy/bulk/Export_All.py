# Databricks notebook source
# MAGIC %md ## Export All
# MAGIC 
# MAGIC Export all the MLflow registered models and all experiments of a tracking server.
# MAGIC 
# MAGIC **Widgets**
# MAGIC * `1. Output directory` - shared directory between source and destination workspaces.
# MAGIC * `2. Stages` - comma seperated stages to be exported.
# MAGIC * `3. Export latest versions` - expor all or just the "latest" versions.
# MAGIC * `4. Export permissions` - export Databricks permissions.
# MAGIC * `5. Notebook formats`
# MAGIC * `6. Use threads`

# COMMAND ----------

# MAGIC %run ./Common

# COMMAND ----------

dbutils.widgets.text("1. Output directory", "") 
output_dir = dbutils.widgets.get("1. Output directory")
output_dir = output_dir.replace("dbfs:","/dbfs")

dbutils.widgets.multiselect("2. Stages", "Production", ["Production","Staging","Archived","None"])
stages = dbutils.widgets.get("2. Stages")

dbutils.widgets.dropdown("3. Export latest versions","no",["yes","no"])
export_latest_versions = dbutils.widgets.get("3. Export latest versions") == "yes"

dbutils.widgets.dropdown("4. Export permissions","no",["yes","no"])
export_permissions = dbutils.widgets.get("4. Export permissions") == "yes"
 
all_formats = [ "SOURCE", "DBC", "HTML", "JUPYTER" ]
dbutils.widgets.multiselect("5. Notebook formats",all_formats[0],all_formats)
notebook_formats = dbutils.widgets.get("5. Notebook formats")

dbutils.widgets.dropdown("6. Use threads","no",["yes","no"])
use_threads = dbutils.widgets.get("6. Use threads") == "yes"
 
print("output_dir:", output_dir)
print("stages:", stages)
print("export_latest_versions:", export_latest_versions)
print("export_permissions:", export_permissions)
print("notebook_formats:", notebook_formats)
print("use_threads:", use_threads)

# COMMAND ----------

assert_widget(output_dir, "1. Output directory")

# COMMAND ----------

from mlflow_export_import.bulk.export_all import export_all

export_all(
    output_dir = output_dir, 
    stages = stages,
    export_latest_versions = export_latest_versions,
    export_permissions = export_permissions,
    notebook_formats = notebook_formats, 
    use_threads = use_threads
)