using DataSquad.Service.Data;
using DataSquad.Service.Domain;
using Microsoft.EntityFrameworkCore;

namespace DataSquad.Service.API
{
    public class AnalysisModel
    {

        private readonly ApplicationDbContext _context;

        public AnalysisModel(ApplicationDbContext context)
        {
            _context = context;
        }

        public async Task<AccessibilityAnalysisResult> CreateAccessibilityAnalysis(List<GeoPoint> region)
        {

            var resultSet = (await _context.AccessibilityRecords.ToListAsync()).Select(x => x.ToAccessibilityRecord()).Where(
                x => x.ToGeoPoint().WithinRegion(region));

            int pointCount = resultSet.Count();

            float minDepth = resultSet.Min(x => x.MeanDepth);
            float maxDepth =  resultSet.Max(x => x.MeanDepth);
            float meanDepth =  resultSet.Average(x => x.MeanDepth);

            float minWaveHeight =  resultSet.Min(x => x.MeanWaveHeight);
            float maxWaveHeight =  resultSet.Max(x => x.MeanWaveHeight);
            float meanWaveHeight =  resultSet.Average(x => x.MeanWaveHeight);

            float minInstantAccessProbability =  resultSet.Min(x => x.MeanInstantAccessProbability);
            float maxInstantAccessProbability =  resultSet.Max(x => x.MeanInstantAccessProbability);
            float meanInstantAccessProbability =  resultSet.Average(x => x.MeanInstantAccessProbability);

            float minExpectedDelayHours =  resultSet.Min(x => x.MeanExpectedDelayHours);
            float maxExpectedDelayHours =  resultSet.Max(x => x.MeanExpectedDelayHours);
            float meanExpectedDelayHours =  resultSet.Average(x => x.MeanExpectedDelayHours);

            return new AccessibilityAnalysisResult
            {
                Region = region,
                PointCount = pointCount,
                MinDepth = minDepth,
                MaxDepth = maxDepth,
                MeanDepth = meanDepth,
                MinWaveHeight = minWaveHeight,
                MaxWaveHeight = maxWaveHeight,
                MeanWaveHeight = meanWaveHeight,
                MinInstantAccessProbability = minInstantAccessProbability,
                MaxInstantAccessProbability = maxInstantAccessProbability,
                MeanInstantAccessProbability = meanInstantAccessProbability,
                MinExpectedDelayHours = minExpectedDelayHours,
                MaxExpectedDelayHours = maxExpectedDelayHours,
                MeanExpectedDelayHours = meanExpectedDelayHours
            };
        }

        public async Task<TurbineAnalysisResult> CreateTurbineAnalysis(List<GeoPoint> region)
        {
            var resultSet = (await _context.TurbineRecords.ToListAsync()).Select(x => x.ToTurbineRecord()).Where(
                    x => x.ToGeoPoint().WithinRegion(region));

            int pointCount = resultSet.Count();

            var minAvailability = resultSet.Min(x => x.MeanAvailability);
            var maxAvailability = resultSet.Max(x => x.MeanAvailability);
            var meanAvailability = resultSet.Average(x => x.MeanAvailability);

            var minCostPerKiloWatt = resultSet.Min(x => x.MeanCostPerKiloWatt);
            var maxCostPerKiloWatt = resultSet.Max(x => x.MeanCostPerKiloWatt);
            var meanCostPerKiloWatt = resultSet.Average(x => x.MeanCostPerKiloWatt);

            var minDowntime = resultSet.Min(x => x.MeanDowntime);
            var maxDowntime = resultSet.Max(x => x.MeanDowntime);
            var meanDowntime = resultSet.Average(x => x.MeanDowntime);

            var minAnnualExpectedPower = resultSet.Min(x => x.MeanAnnualExpectedPower);
            var maxAnnualExpectedPower = resultSet.Max(x => x.MeanAnnualExpectedPower);
            var meanAnnualExpectedPower = resultSet.Average(x => x.MeanAnnualExpectedPower);

            return new TurbineAnalysisResult
            {
                Region = region,
                PointCount = pointCount,
                MinAvailability = minAvailability,
                MaxAvailability = maxAvailability,
                MeanAvailability = meanAvailability,
                MinCostPerKiloWatt = minCostPerKiloWatt,
                MaxCostPerKiloWatt = maxCostPerKiloWatt,
                MeanCostPerKiloWatt = meanCostPerKiloWatt,
                MinDowntime = minDowntime,
                MaxDowntime = maxDowntime,
                MeanDowntime = meanDowntime,
                MinAnnualExpectedPower = minAnnualExpectedPower,
                MaxAnnualExpectedPower = maxAnnualExpectedPower,
                MeanAnnualExpectedPower = meanAnnualExpectedPower
            };
        }
    }
}
