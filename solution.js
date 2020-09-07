const validBraces = braces =>{
  if(braces.length%2 !==0) return false
  const brace_length = braces.length/2
  for(let i=0;i<brace_length;i++){
    braces=braces.replace(/\[\]|\(\)|\{\}/gi,'')
    if (braces.length===0) return true
  }
  return false
}