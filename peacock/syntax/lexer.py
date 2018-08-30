from pygments.token import *;
from pygments.lexer import RegexLexer, bygroups;


from pygments.token import Token, STANDARD_TYPES;

DataType = Token.DataType;

class RE:
	Domain = r'\b(?:[A-Za-z0-9\-\.]+){1,4}\.(?:com|net|org|biz|gov|edu|mil|aero|asia|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|[A-Za-z]{2})\b';
	Email = r'[\w\d!#$%&*._0/=?^_`{|}~\-]+@(?:[A-Za-z0-9\-\.]+){1,}\.[A-Za-z\-]{2,6}';
	IPv4_CIDR = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(/)(\d{1,2})';
	IPv4_Address = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}';
	Time = r'\d{1,2}:\d{2}(:\d{2})?(\s+(AM|PM))?';
	Dates = [
		r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct\Nov|Dec)\s+\d{1,2})(\s+\d{2,4})?(\s+)',
		r'\d{1,2}/\d{1,2}/\d{2,4}',
		r'\d{4}-\d{1,2}-\d{1,2}',
	];
	URL = '';

RE.URL = r'(https?|ftp|ssh|git|svn|file)://' + RE.Domain + r'(/\S+)?\b'


class DataTypesLexer(RegexLexer):
	"""
		Custom formatter for postfix-reject-log by Clint Priest
	"""
	name = 'DataTypes'
	aliases = ['DataTypes','datatypes']
	filenames = []
	mimetypes = ['text/x-datatypes-lexer']

	tokens = {
		'root': [
			(RE.URL, DataType.URL),
			(RE.Email, DataType.Email),
			(RE.Domain, DataType.Domain),
			(RE.IPv4_CIDR, bygroups(DataType.Net.IPv4.CIDR.Address,Operator,DataType.Net.IPv4.CIDR.Mask)),
			(RE.IPv4_Address, DataType.Net.IPv4.Address),
			(RE.Time, DataType.Time),
			(RE.Dates[0], bygroups(DataType.Date, DataType.Date, Literal)),
			(RE.Dates[1], DataType.Date),
			(RE.Dates[2], DataType.Date),
			(r'.', Other),
		],
	}

	def __init__(self, **options):
#		print('DataTypesLexer Loaded');
		super(DataTypesLexer, self).__init__(**options);

	# noinspection PyMethodParameters
	def analyse_text(text):
		return .3;
