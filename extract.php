<?php
  $xmlstr = file_get_contents("artlung.wordpress.2018-02-22.xml");
  $outputfilename = "artlung.corpus.txt";
  $blogcontent = new SimpleXMLElement($xmlstr);
  $all_text = array();
  $i = 0;
  foreach ($blogcontent->channel->item as $item) {
    $content = $item->children('content', true);
    $content = str_replace('>', "> ", $content);
    $content = str_replace('\n', " ", $content);
    $all_text[] = (strip_tags($item->children('content', true)));
    $all_text[] = ((string)$item->title);
  }
  $str = implode("\n", $all_text);
  file_put_contents($outputfilename, $all_text);
?>
