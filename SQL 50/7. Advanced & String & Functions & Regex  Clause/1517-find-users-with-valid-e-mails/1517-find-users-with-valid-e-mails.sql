# Write your MySQL query statement below
Select user_id, name, mail
From Users
Where mail Regexp '^[a-zA-Z][a-zA-Z0-9_.-]*\\@leetcode\\.com$'


-- ^: This represents the start of a string or line.
-- [a-z]*: This represents a character range, matching any character from a to z zero or more times.

-- [a-z]+: This represents a character range, matching any character from a to z one or more times.
-- .: This matches exactly one of any character.

-- `\\@` : `@` 문자를 나타냅니다. 정규 표현식에서 `@`는 특별한 의미를 가질 수 있기 때문에, 이를 리터럴 문자로 사용하기 위해 이스케이프(escape) 처리가 필요합니다. 여기서는 이스케이프 문자로 바로 `\`를 사용하고 있으나, SQL 쿼리 내에서 `\` 자체도 이스케이프 처리가 필요하므로 `\\`로 작성되었습니다.
-- `\\.` : 마침표(.) 문자를 나타냅니다. 마침표는 정규 표현식에서 "어떤 하나의 문자"를 의미하는 특별한 기호이므로, 리터럴 마침표 문자로 사용하기 위해 이스케이프 처리가 필요합니다. 여기서도 SQL 쿼리 내 이스케이프 규칙에 따라 `\\`를 사용합니다.
-- `$` : 문자열의 끝을 나타냅니다.