function Pandoc(doc)
  local words = 0
  pandoc.walk_block(pandoc.Div(doc.blocks), {
    Str = function(el)
      words = words + 1
    end
  })
  local minutes = math.ceil(words / 80)
  local meta = doc.meta
  meta['readtime'] = pandoc.MetaInlines({
    pandoc.Str(minutes .. " min read")
  })
  return pandoc.Pandoc(doc.blocks, meta)
end