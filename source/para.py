NA = ['ngh', 
      'ng', 'th', 'ph', 'ch', 'gh', 'nh', 'tr', 'kh',
      'd', 'đ', 'k', 't', 'g', 'm', 'n', 'h', 'g', 'r', 'q', 'p', 'v', 'h','x', 'l', 's', 'b', 'c']

patterns = {
    '[-]': ' ',
    '[!#,]': '',
    '[ầấậẫẩ]': 'â',
    '[ắằẵặẳ]': 'ă',
    '[àáảãạ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹ]': 'e',
    '[êềếểễệ]': 'ê',
    #'[èéẻẽẹêềếểễệ]': 'e',
    
    '[ìíỉĩịỳýỷỹỵ]': 'i',
    '[òóỏõọ]': 'o',
    '[ôồốổỗộ]': 'ô',
    '[ờớởỡợ]': 'ơ',
    #'[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụ]': 'u',
    '[ừứửữự]': 'ư',
    #'[ùúủũụưừứửữự]': 'u',
    #'[ỳýỷỹỵ]': 'y'
}