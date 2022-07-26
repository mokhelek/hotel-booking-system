            
 //const linkedPicker1Element = document.getElementById('linkedPickers1');
 
 //const linked1 = new tempusDominus.TempusDominus(linkedPicker1Element);
 const linked1 = new tempusDominus.TempusDominus(document.getElementById('linkedPickers1'),{
   display:{
     components:{
       decades:true,
       year:true,
       month:true,
       date:true,
       hours:false,
       minutes:false,
       seconds:false,
     }
   },
 
 })
 
 const linked2 = new tempusDominus.TempusDominus(document.getElementById('linkedPickers2'), {
   useCurrent: false,
   display:{
     components:{
       decades:true,
       year:true,
       month:true,
       date:true,
       hours:false,
       minutes:false,
       seconds:false,
     }
   }
   
 });
 
 //using event listeners
 linkedPicker1Element.addEventListener(tempusDominus.Namespace.events.change, (e) => {
   linked2.updateOptions({
     restrictions: {
       minDate: e.detail.date
     }
   });
 });
 
 //using subscribe method
 const subscription = linked2.subscribe(tempusDominus.Namespace.events.change, (e) => {
   linked1.updateOptions({
     restrictions: {
       maxDate: e.date
     }
   });
 });
       
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 new tempusDominus.TempusDominus(document.getElementById('datetimepicker4'), {
    display: {
      viewMode: 'clock',
      components: {
        decades: true,
        year: true,
        month: true,
        date: true,
        hours: false,
        minutes: false,
        seconds: false,
      }
    }
  });
            
 
 
 
 
 
 
 
 
 