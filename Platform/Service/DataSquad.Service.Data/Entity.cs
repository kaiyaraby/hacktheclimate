using System.ComponentModel.DataAnnotations;
using DataSquad.Service.Domain;
using Microsoft.EntityFrameworkCore;

namespace DataSquad.Service.Data
{
    public class AccessibilityRecordEntity
    {
        public long Id { get; set; }

        [Required]
        public float Latitude { get; set; }

        [Required]
        public float Longitude { get; set; }

        public float MeanDepth { get; set; }
        public float MeanWaveHeight { get; set; }
        public float MeanInstantAccessProbability { get; set; }
        public float MeanExpectedDelayHours { get; set; }

        internal static void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<AccessibilityRecordEntity>().HasIndex(x => new {x.Latitude, x.Longitude});
        }

        public AccessibilityRecord ToAccessibilityRecord()
        {
            return new AccessibilityRecord
            {
                Latitude = Latitude,
                Longitude = Longitude,
                MeanDepth = MeanDepth,
                MeanWaveHeight = MeanWaveHeight,
                MeanInstantAccessProbability = MeanInstantAccessProbability,
                MeanExpectedDelayHours = MeanExpectedDelayHours
            };
        }
    }

    public class TurbineRecordEntity
    {
        public long Id { get; set; }

        [Required]
        public float Latitude { get; set; }

        [Required]
        public float Longitude { get; set; }

        public float MeanAvailability { get; set; }
        public float MeanCostPerKiloWatt { get; set; }
        public float MeanDowntime { get; set; }
        public float MeanAnnualExpectedPower { get; set; }

        internal static void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<TurbineRecordEntity>().HasIndex(x => new {x.Latitude, x.Longitude});
        }

        public TurbineRecord ToTurbineRecord()
        {
            return new TurbineRecord
            {
                Latitude = Latitude,
                Longitude = Longitude,
                MeanAvailability = MeanAvailability,
                MeanCostPerKiloWatt = MeanCostPerKiloWatt,
                MeanDowntime = MeanDowntime,
                MeanAnnualExpectedPower = MeanAnnualExpectedPower
            };
        }
    }
}
