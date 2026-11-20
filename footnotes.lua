local function note_inlines(blocks)
  return pandoc.utils.blocks_to_inlines(blocks, { pandoc.Space() })
end

local function is_references(block)
  return block.t == 'Header'
    and pandoc.utils.stringify(block.content):lower() == 'references'
end

function Pandoc(doc)
  local notes = {}

  doc = doc:walk({
    Note = function(note)
      local n = #notes + 1
      local num = tostring(n)
      notes[n] = note.content

      local ref = pandoc.Superscript({
        pandoc.Link({ pandoc.Str(num) }, '#fn' .. num, '',
          pandoc.Attr('fnref' .. num, { 'footnote-ref' }))
      })

      local side = pandoc.Span(
        { pandoc.Span({ pandoc.Str(num) }, pandoc.Attr('', { 'sidenote-marker' })), pandoc.Space() },
        pandoc.Attr('', { 'sidenote' }))
      side.content:extend(note_inlines(note.content))

      return { ref, side }
    end
  })

  if #notes == 0 then return doc end

  local items = {}
  for n, content in ipairs(notes) do
    local blocks = content:clone()
    local back = pandoc.Link({ pandoc.Str('↩︎') }, '#fnref' .. n, '',
      pandoc.Attr('', { 'footnote-back' }))
    local last = blocks[#blocks]
    if last and (last.t == 'Para' or last.t == 'Plain') then
      last.content:extend({ pandoc.Space(), back })
    else
      blocks:insert(pandoc.Plain({ back }))
    end
    items[n] = { pandoc.Div(blocks, pandoc.Attr('fn' .. n, { 'footnote' })) }
  end

  local section = {
    pandoc.Header(2, { pandoc.Str('Notes') }, pandoc.Attr('notes')),
    pandoc.OrderedList(items),
  }

  local at = #doc.blocks + 1
  for i, block in ipairs(doc.blocks) do
    if is_references(block) then at = i; break end
  end
  for j = #section, 1, -1 do
    doc.blocks:insert(at, section[j])
  end
  return doc
end
