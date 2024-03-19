namespace DataSquad.Service.Domain
{
    public struct GeoPoint
    {
        public float Latitude { get; set; }
        public float Longitude { get; set; }

        public bool WithinRegion(List<GeoPoint> region)
        {
            bool result = false;
            int j = region.Count - 1;
            for (int i = 0; i < region.Count; i++)
            {
                if (region[i].Longitude < Longitude && region[j].Longitude >= Longitude ||
                    region[j].Longitude < Longitude && region[i].Longitude >= Longitude)
                {
                    if (region[i].Latitude + (Longitude - region[i].Longitude) /
                        (region[j].Longitude - region[i].Longitude) *
                        (region[j].Latitude - region[i].Latitude) < Latitude)
                    {
                        result = !result;
                    }
                }
            }
            return result;
        }
    }

    public interface IGeoPointRecord
    {
        float Latitude { get; set; }
        float Longitude { get; set; }
    }

    public static class GeoPointExtensions
    {
        public static GeoPoint ToGeoPoint(this IGeoPointRecord x)
        {
             return new GeoPoint
            {
                Latitude = x.Latitude,
                Longitude = x.Longitude,
            };
        }
    }

    public class AccessibilityRecord : IGeoPointRecord
    {
        public float Latitude { get; set; }
        public float Longitude { get; set; }
        public float MeanDepth { get; set; }
        public float MeanWaveHeight { get; set; }
        public float MeanInstantAccessProbability { get; set; }
        public float MeanExpectedDelayHours { get; set; }
    }

    public class TurbineRecord : IGeoPointRecord
    {
        public float Latitude { get; set; }
        public float Longitude { get; set; }
        public float MeanAvailability { get; set; }
        public float MeanCostPerKiloWatt { get; set; }
        public float MeanDowntime { get; set; }
        public float MeanAnnualExpectedPower { get; set; }
    }

    public class TurbineAnalysisResult
    {
        public List<GeoPoint> Region { get; set; }

        public int PointCount { get; set; }

        public float MinAvailability { get; set; }
        public float MaxAvailability { get; set; }
        public float MeanAvailability { get; set; }

        public float MinCostPerKiloWatt { get; set; }
        public float MaxCostPerKiloWatt { get; set; }
        public float MeanCostPerKiloWatt { get; set; }

        public float MinDowntime { get; set; }
        public float MaxDowntime { get; set; }
        public float MeanDowntime { get; set; }

        public float MinAnnualExpectedPower { get; set; }
        public float MaxAnnualExpectedPower { get; set; }
        public float MeanAnnualExpectedPower { get; set; }
    }

    public class AccessibilityAnalysisResult
    {
        public List<GeoPoint> Region { get; set; }

        public int PointCount { get; set; }

        public float MinDepth { get; set; }
        public float MaxDepth { get; set; }
        public float MeanDepth { get; set; }

        public float MinWaveHeight { get; set; }
        public float MaxWaveHeight { get; set; }
        public float MeanWaveHeight { get; set; }

        public float MinInstantAccessProbability { get; set; }
        public float MaxInstantAccessProbability { get; set; }
        public float MeanInstantAccessProbability { get; set; }

        public float MinExpectedDelayHours { get; set; }
        public float MaxExpectedDelayHours { get; set; }
        public float MeanExpectedDelayHours { get; set; }
    }
}
