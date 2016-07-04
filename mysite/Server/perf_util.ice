module Vistek
{
	module Perf
	{
		enum ResponseStringType
		{
			rstXml,
			rstJson
		};

		class ObjectTrack
		{
			string ClassName;
		};

		class ClientInfo extends ObjectTrack
		{
			string IP;
			int port = 0;
			optional(1) float UpRate = 0;
		};
		sequence<ClientInfo> ClientInfoList;

		class PipelineInfo extends ObjectTrack
		{
			string uri;
			optional(1) float DownRate = 0;
		};
		sequence<PipelineInfo> PipelineInfoList;

		interface ServicePerf
		{
			string GetSumRate(ResponseStringType rst);
			long GetTimestampTicks();
			ClientInfoList GetAllClients();
		};

		interface MediaServicePerf extends ServicePerf
		{
			PipelineInfoList GetAllPipelines();
		};

		interface DeviceServicePerf extends ServicePerf
		{
		};
	};
};
