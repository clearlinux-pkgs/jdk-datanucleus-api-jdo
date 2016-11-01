Name     : jdk-datanucleus-api-jdo
Version  : 3.2.6
Release  : 4
URL      : https://repo1.maven.org/maven2/org/datanucleus/datanucleus-api-jdo/3.2.6/datanucleus-api-jdo-3.2.6.jar
Source0  : https://repo1.maven.org/maven2/org/datanucleus/datanucleus-api-jdo/3.2.6/datanucleus-api-jdo-3.2.6.jar
Source1  : https://repo1.maven.org/maven2/org/datanucleus/datanucleus-api-jdo/3.2.6/datanucleus-api-jdo-3.2.6.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-datanucleus-api-jdo-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-datanucleus-api-jdo package.
Group: Data

%description data
data components for the jdk-datanucleus-api-jdo package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/datanucleus-api-jdo.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/datanucleus-api-jdo.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/datanucleus-api-jdo.xml \
%{buildroot}/usr/share/maven-poms/datanucleus-api-jdo.pom \
%{buildroot}/usr/share/java/datanucleus-api-jdo.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/datanucleus-api-jdo.jar
/usr/share/maven-metadata/datanucleus-api-jdo.xml
/usr/share/maven-poms/datanucleus-api-jdo.pom
