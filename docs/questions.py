# Q#:[[Question Text, ['next question if answer "yes",'next question if answer "No"']], isquestion = boolean ]
# next question = '99' == no next question. End of the line
qs = {
      1:['Does the material which the agency proposes to release constitute or contain a copyright work?', ['02','18'], True],
      2:['Does the agency own copyright in the work or otherwise have sufficient rights to license the work?', ['03','04'], True],
      3:['Work should be licensed with Creative Commons BY licence unless restriction applies?', ['05','06'], False],
      4:['Either obtain the relevant rights and proceed or do not release for re-use', ['99','99'], False],
      5:['Are there any restrictions on release and re-use?', ['06','11'], True],
      6:['Can the restriction(s) be addressed by amendment or anonymisation of the material?', ['11','07'], True],
      7:['Does the restriction prevent all forms of release?', ['08','09'], True],
      8:['Do not publish' , ['99','99'], False],
      9:['Consider licensing work with the other CC licence (taking Creativity, Authenticity and Non-Discrimination Principles into account) or restrictive lincence as appropriate' , ['10','11'], True], 
      10:['If appropriate, prepare restricted licence and release to restricted audience', ['99','99'], False],
      11:['Apply Chosen CC licence markings to work and/or prepare to apply them at point of release. For all online releases, include the CC-generated code/metadata', ['12','12'], False],
      12:["Does the author of the work's right to be identified as author arise and, if so, has the author asserted the right to be identified?"  , ['13','14'], True],
      13:['Identify the author when publishing the work or an adaptation of it commercially, performing it in the public or communicating it to the public ', ['14','14'], False],
      14:['Does the agency know the format(s) in which people would like the material to be released?', ['15','15'], True],
      15:['To the extent practicable, prepare the material for release in those format(s). Where material is released in proprietary format, endeavor to release in open, non-proprietary format(s) as well.', ['17','17'], False],
      16:['Either seek public feedback on desired format(s) before release or prepare the material for release in one or more standards-compliant formats with a view to asking recipients, after release, whether they are satisfied with those format(s). Where material is released in proprietary format, endeavor to release in open, non-proprietary format(s) as well.', ['17','17'], False],
      17:["Select appropriate channels for release, whether government and/or third party operated, but including where possible the agency's own website and outgoing Atom or RSS feed and, for datasets, an announcement/listing on data.govt.nz. Consider using press releases and/or social media to publicise release and maximise uptake. RELEASE", ['99','99'], False],
    # T2
    
      # Some of the below is duplicated. Rather not but the html template iterates over a order list of questions. 
      # therefore for the Qs in the doc to be order questions must always increment and can not return to smaller number
      # an other table could be built separating q_ids and q_text
      18:["The copyright analysis ceases and the agency can skip to stage 2 (Evaluation of restrictions). The material should be released on open access terms unless a restriction applies.", ['19','19'], False],
      19:["Are there any restrictions on release and re-use?", ['20','25'], True],
      20:["Can the restrictions(s) be addressed by amendment or anonymisation of the material?", ['23','21'], True],
      21:["Does the restriction prevent all forms of release?", ['8','22'], True],
      22:['Do not publish' , ['99','99'], False],
      23:["Consider releasing on restricted contractual terms to restricted audience", ['24','24'], False], 
      24:['If appropriate, prepare restricted licence and release to restricted audience', ['99','99'], False],
      25:["Include within material and/or prepare to include at point of release a 'no known rights' statement", ['26','26'], False], 
      26:["Note: Moral rights are not relevant to non-copyright material", ['27','27'], True]}   
      27:['Does the agency know the format(s) in which people would like the material to be released?', ['28','29'], True],
      28:['To the extent practicable, prepare the material for release in those format(s). Where material is released in proprietary format, endeavor to release in open, non-proprietary format(s) as well.', ['30','30'], False],
      29:['Either seek public feedback on desired format(s) before release or prepare the material for release in one or more standards-compliant formats with a view to asking recipients, after release, whether they are satisfied with those format(s). Where material is released in proprietary format, endeavor to release in open, non-proprietary format(s) as well.', ['17','17'], False],
      30:["Select appropriate channels for release, whether government and/or third party operated, but including where possible the agency's own website and outgoing Atom or RSS feed and, for datasets, an announcement/listing on data.govt.nz. Consider using press releases and/or social media to publicise release and maximise uptake. RELEASE", ['99','99'], False],

