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
}
