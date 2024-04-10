# Use the ASP.NET Core SDK image as build
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /app

# Copy the TestCases directory into the image
COPY . .

# Navigate to the java-prov directory and copy the JAR file
WORKDIR /app/TestCases/TestCasesWebApp

RUN dotnet restore
RUN dotnet publish -c Release -o ./publish

WORKDIR /app

# Install OpenJDK (Java runtime)
RUN apt-get update && apt-get install -y openjdk-17-jre

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Python dependencies
RUN pip3 install --no-cache-dir -r ./python-prov/requirements.txt

FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS runtime
WORKDIR /app
COPY --from=build /app .

# Specify the entry point for the container
ENTRYPOINT ["dotnet", "./TestCases/TestCasesWebApp/publish/TestCasesWebApp.dll"]
