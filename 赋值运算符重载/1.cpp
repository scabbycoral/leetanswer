class CMyString
{
public:
    CMyString(char* pData = nullptr);
    CMyString(const CMyString& str);
    ~CMyString(void);

    CMyString& operator = (const CMyString& str);

    void Print();
      
private:
    char* m_pData;
};

CMyString::CMyString(char *pData)
{
    if(pData == nullptr)
    {
        m_pData = new char[1];
        m_pData[0] = '\0';
    }
    else
    {
        int length = strlen(pData);
        m_pData = new char[length + 1];
        strcpy(m_pData, pData);
    }
}

CMyString::CMyString(const CMyString &str)
{
    int length = strlen(str.m_pData);
    m_pData = new char[length + 1];
    strcpy(m_pData, str.m_pData);
}

CMyString::~CMyString()
{
    delete[] m_pData;
}

CMyString& CMyString::operator = (const CMyString& str)
{
    if(this == &str)
        return *this;

    delete []m_pData;
    m_pData = nullptr;

    m_pData = new char[strlen(str.m_pData) + 1];
    strcpy(m_pData, str.m_pData);

    return *this;
	#1.返回值声明为该类的引用，返回值为*this自身的引用，只有返回了这个引用才可以连等
	#2.传入的参数类型为const引用，否则会调用一次从形参到入参的复制构造函数
	#3.申请空间之前释放之前申请的空间
	#4.判断实参和*this受否是一个实例，如果是，则不进行赋值，直接返回*this，因为继续往下进行会释放之前的空间，等号左右两边就都会出现内存问题
}

"""
#改进
CMyString& CMyString::operator = (const CMyString& str)
{
	if(this!=&str)
	{
		CMyString strTemp(str);
		char* pTemp=strTemp.m_pData;
		strTemp.m_pData=m_pData;
		m_pData=pTemp;
		#创建一个临时实例，通过他对实参和*this进行交换，退出当前作用域自动调用析构函数，不需要考虑内存问题
		#实参strTemp，临时pTemp
	}
}
"""