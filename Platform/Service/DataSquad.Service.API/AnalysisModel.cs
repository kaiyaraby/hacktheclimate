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

            var resultSet = (await _context.AccessibilityRecords.ToListAsync()).Where(
                x => x.ToAccessibilityRecord().ToGeoPoint().WithinRegion(region));

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
            var resultSet = (await _context.TurbineRecords.ToListAsync()).Where(
                    x => x.ToTurbineRecord().ToGeoPoint().WithinRegion(region));

            var minAvailability = resultSet.Min(x => x.MeanAvailability);
            var maxAvailability = resultSet.Max(x => x.MeanAvailability);
            var meanAvailability = resultSet.Average(x => x.MeanAvailability);

            var minCostPerKiloWatt = resultSet.Min(x => x.MeanCostPerKiloWatt);
            var maxCostPerKiloWatt = resultSet.Max(x => x.MeanCostPerKiloWatt);
            var meanCostPerKiloWatt = resultSet.Average(x => x.MeanCostPerKiloWatt);

            var minDowntime = resultSet.Min(x => x.MeanDowntime);
            var maxDowntime = resultSet.Max(x => x.MeanDowntime);
            var meanDowntime = resultSet.Average(x => x.MeanDowntime);

            return new TurbineAnalysisResult
            {
                Region = region,
                MinAvailability = minAvailability,
                MaxAvailability = maxAvailability,
                MeanAvailability = meanAvailability,
                MinCostPerKiloWatt = minCostPerKiloWatt,
                MaxCostPerKiloWatt = maxCostPerKiloWatt,
                MeanCostPerKiloWatt = meanCostPerKiloWatt,
                MinDowntime = minDowntime,
                MaxDowntime = maxDowntime,
                MeanDowntime = meanDowntime
            };
        }
    }
}
