<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="20008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="PSLabView" Type="Folder">
			<Item Name="Libraries" Type="Folder">
				<Item Name="BouncyCastle.Crypto.dll" Type="Document" URL="../PalmSens/Libraries/BouncyCastle.Crypto.dll"/>
				<Item Name="InTheHand.Net.Personal.dll" Type="Document" URL="../PalmSens/Libraries/InTheHand.Net.Personal.dll"/>
				<Item Name="Newtonsoft.Json.dll" Type="Document" URL="../PalmSens/Libraries/Newtonsoft.Json.dll"/>
				<Item Name="PalmSens.Core.dll" Type="Document" URL="../PalmSens/Libraries/PalmSens.Core.dll"/>
				<Item Name="PalmSens.Core.Simplified.dll" Type="Document" URL="../PalmSens/Libraries/PalmSens.Core.Simplified.dll"/>
				<Item Name="PalmSens.Core.Simplified.LabVIEW.dll" Type="Document" URL="../PalmSens/Libraries/PalmSens.Core.Simplified.LabVIEW.dll"/>
				<Item Name="PalmSens.Core.Simplified.WinForms.dll" Type="Document" URL="../PalmSens/Libraries/PalmSens.Core.Simplified.WinForms.dll"/>
				<Item Name="PalmSens.Core.Windows.dll" Type="Document" URL="../PalmSens/Libraries/PalmSens.Core.Windows.dll"/>
			</Item>
			<Item Name="CurveFinished Event Callback.vi" Type="VI" URL="../PalmSens/CurveFinished Event Callback.vi"/>
			<Item Name="LiveCurveResult.ctl" Type="VI" URL="../PalmSens/LiveCurveResult.ctl"/>
			<Item Name="MeasurementEnded Event Callback.vi" Type="VI" URL="../PalmSens/MeasurementEnded Event Callback.vi"/>
			<Item Name="MeasurementResults.ctl" Type="VI" URL="../PalmSens/MeasurementResults.ctl"/>
			<Item Name="NewDataAdded Event Callback.vi" Type="VI" URL="../PalmSens/NewDataAdded Event Callback.vi"/>
			<Item Name="PalmSens.lvclass" Type="LVClass" URL="../PalmSens/PalmSens.lvclass"/>
			<Item Name="SimpleCurveAdded Event Callback.vi" Type="VI" URL="../PalmSens/SimpleCurveAdded Event Callback.vi"/>
		</Item>
		<Item Name="BasicExample.vi" Type="VI" URL="../BasicExample.vi"/>
		<Item Name="BasicUIExample.vi" Type="VI" URL="../BasicUIExample.vi"/>
		<Item Name="MethodSCRIPTExample.vi" Type="VI" URL="../MethodSCRIPTExample.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="mscorlib" Type="VI" URL="mscorlib">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
