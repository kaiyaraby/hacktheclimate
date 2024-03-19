﻿// <auto-generated />
using DataSquad.Service.Data;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;

#nullable disable

namespace DataSquad.Service.Data.Migrations
{
    [DbContext(typeof(ApplicationDbContext))]
    [Migration("20240319110329_new_turbine_field")]
    partial class new_turbine_field
    {
        /// <inheritdoc />
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "8.0.3")
                .HasAnnotation("Relational:MaxIdentifierLength", 128);

            SqlServerModelBuilderExtensions.UseIdentityColumns(modelBuilder);

            modelBuilder.Entity("DataSquad.Service.Data.AccessibilityRecordEntity", b =>
                {
                    b.Property<long>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("bigint");

                    SqlServerPropertyBuilderExtensions.UseIdentityColumn(b.Property<long>("Id"));

                    b.Property<float>("Latitude")
                        .HasColumnType("real");

                    b.Property<float>("Longitude")
                        .HasColumnType("real");

                    b.Property<float>("MeanDepth")
                        .HasColumnType("real");

                    b.Property<float>("MeanExpectedDelayHours")
                        .HasColumnType("real");

                    b.Property<float>("MeanInstantAccessProbability")
                        .HasColumnType("real");

                    b.Property<float>("MeanWaveHeight")
                        .HasColumnType("real");

                    b.HasKey("Id");

                    b.HasIndex("Latitude", "Longitude");

                    b.ToTable("AccessibilityRecords");
                });

            modelBuilder.Entity("DataSquad.Service.Data.TurbineRecordEntity", b =>
                {
                    b.Property<long>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("bigint");

                    SqlServerPropertyBuilderExtensions.UseIdentityColumn(b.Property<long>("Id"));

                    b.Property<float>("Latitude")
                        .HasColumnType("real");

                    b.Property<float>("Longitude")
                        .HasColumnType("real");

                    b.Property<float>("MeanAnnualExpectedPower")
                        .HasColumnType("real");

                    b.Property<float>("MeanAvailability")
                        .HasColumnType("real");

                    b.Property<float>("MeanCostPerKiloWatt")
                        .HasColumnType("real");

                    b.Property<float>("MeanDowntime")
                        .HasColumnType("real");

                    b.HasKey("Id");

                    b.HasIndex("Latitude", "Longitude");

                    b.ToTable("TurbineRecords");
                });
#pragma warning restore 612, 618
        }
    }
}