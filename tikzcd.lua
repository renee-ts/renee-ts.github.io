local system = require 'pandoc.system'

local CACHE_DIR = "tikz-cache"

local TEMPLATE = [[
\documentclass[border=4pt]{standalone}
\usepackage{tikz-cd}
\usepackage{amsmath}
\usepackage{amssymb}
\begin{document}
\nopagecolor
%s
\end{document}
]]

local function file_exists(path)
  local f = io.open(path, 'r')
  if f then f:close(); return true end
  return false
end

local function ensure_cache_dir()
  os.execute('mkdir -p ' .. CACHE_DIR)
end

local function compile_to_svg(src)
  ensure_cache_dir()

  local hash    = pandoc.sha1(src)
  local svg_path = CACHE_DIR .. '/' .. hash .. '.svg'

  if file_exists(svg_path) then
    return svg_path
  end

  local ok, err = system.with_temporary_directory('tikzcd-' .. hash, function(tmpdir)
    system.with_working_directory(tmpdir, function()
      -- Write the .tex file.
      local tex_file = io.open('diagram.tex', 'w')
      tex_file:write(TEMPLATE:format(src))
      tex_file:close()

      local pdf_ok = os.execute(
        'pdflatex -interaction=nonstopmode -halt-on-error diagram.tex > /dev/null 2>&1'
      )
      if not pdf_ok then
        error('pdflatex failed. Check your tikz-cd source.')
      end

      local svg_ok = os.execute('pdf2svg diagram.pdf diagram.svg')
      if not svg_ok then
        error('pdf2svg failed. Is pdf2svg installed?')
      end

      local abs_cache = system.get_working_directory()
      os.execute('cp diagram.svg ' .. abs_cache .. '/' .. svg_path)
    end)
  end)

  if ok == false then
    return nil, err
  end

  return svg_path
end

function RawBlock(el)
  if el.format ~= 'latex' then return el end

  local src = el.text
  if not (src:match('\\begin%{tikzcd%}') or src:match('\\begin%{tikzpicture%}')) then
    return el
  end

  local svg_path, err = compile_to_svg(src)

  if not svg_path then
    io.stderr:write('[tikzcd.lua] ERROR: ' .. tostring(err) .. '\n')
    return pandoc.CodeBlock(src, {class='latex'})
  end

  local img_html = string.format(
    '<figure><img src="%s" alt="commutative diagram" style="display:block; margin:1.5em auto;"/></figure>',
    svg_path
  )

  return pandoc.RawBlock('html', img_html)
end