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

    public class AccessibilityRecord
    {
        public float Latitude { get; set; }
        public float Longitude { get; set; }
        public float MeanDepth { get; set; }
        public float MeanWaveHeight { get; set; }
        public float MeanInstantAccessProbability { get; set; }
        public float MeanExpectedDelayHours { get; set; }

        public GeoPoint ToGeoPoint()
        {
            return new GeoPoint
            {
                Latitude = Latitude,
                Longitude = Longitude,
            };
        }
    }

    public class AccessibilityAnalysisResult
    {
        public List<GeoPoint> Region { get; set; }

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
