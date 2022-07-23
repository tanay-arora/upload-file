import re
from django.http import JsonResponse
from django.shortcuts import render
from home.models import *
from registration.models import *
from event.models import *
from speakers.models import *
from sponsors.models import *

footer = '''<div class="section padding-top padding-bottom-big background-dark footer">
                        <div class="container">
                            <div class="row">
                                <div class="col-md-12">
                                    <img src="static/assets/img/main-logo.svg" alt="">
                                    <h6 class="mt-5 mb-3">Get in touch:</h6>
                                    <p>test@cutbi.in</p>
                                    <p>+1 325 2532</p>
                                </div>
                                <div class="col-md-12 mt-5 mb-5">
                                    <div class="title-page-line"></div>
                                </div>
                                <div class="col-md-12">
                                    <p><small>© 2022 All rigths reserved. Chandigarh University | Ecell</small></p>
                                </div>
                            </div>
                        </div>
                    </div>'''

def home(req):
    cspeakers = current_speakers.objects.all()
    pspeakers = past_speakers.objects.all()
    investor = investors.objects.all()
    cgallery = gallery.objects.all()
    sponsor = sponsors_category.objects.all()
    schedule = event_day.objects.all()
    tickets = ticket.objects.all()
    data = {
        "cspeakers":cspeakers,
        "pspeakers":pspeakers,
        "investors":investor,
        "gallery":cgallery,
        "sponsors":sponsor,
        "schedule":schedule,
        "tickets":tickets,
        "footer":footer
    }
    return render(req,'main/index.html',data)

def registration(req,slug):
    tickets = ticket.objects.all()
    data = {
        "footer":footer,
        "tickets":tickets,
        "selected":slug
    }
    return render(req,'main/registration.html', data)

def sitform(req):
    if req.method == 'POST':
        try:
            name = req.POST.get("name")
            email = req.POST.get("email")
            message = req.POST.get("message")
            if len(name) > 0 and len(email) > 0:
                stay_informed.objects.create(name=name,email=email,message=message) #mail service have to intiallized
                return JsonResponse({"success":"Your response saved successfully!"})
        except:
            return JsonResponse({"error":"Something went wrong!"})

def subscribe(req):
    if req.method == 'POST':
        try:
            email = req.POST.get("subscribeemail")
            if len(email) > 0:
                subscriber.objects.create(email=email) #add email to subscriber list
                return JsonResponse({"success":"Your response saved successfully!"}) 
        except:
            return JsonResponse({"error":"Something went wrong!"})

def startup_register(req):
    if req.method == 'POST':
        rcompany_name = req.POST.get("rcompany_name")
        roffice_location = req.POST.get("roffice_location")
        rtotal_employees = req.POST.get("rtotal_employees")
        rwebsite_url = req.POST.get("rwebsite_url")
        rcompany_category = req.POST.get("rcompany_category")
        rindustry = req.POST.get("rindustry")
        rpitchbook = req.FILES.get("rpitchbook")
        rwhere_you_know_id = req.POST.get("rwhere_you_know")
        rshowcasing_product_id = req.POST.get("rshowcasing_product")
        rcu_passout_id = req.POST.get("rcu_passout")
        rhiring_interns_id = req.POST.get("rhiring_interns")
        rhiring_professionals_id = req.POST.get("rhiring_professionals")
        rdescribe_one_sentence = req.POST.get("rdescribe_one_sentence")
        rcore_problem = req.POST.get("rcore_problem")
        ruse_case = req.POST.get("ruse_case")
        rtarget_audience = req.POST.get("rtarget_audience")
        rbusiness_model = req.POST.get("rbusiness_model")
        rbiggest_competitors = req.POST.get("rbiggest_competitors")
        rwhy_unique = req.POST.get("rwhy_unique")
        rraise_capital = req.POST.get("rraise_capital")
        rvideo_url = req.POST.get("rvideo_url")
        rincubator_program = req.POST.get("rincubator_program")
        rhave_revenue_id = req.POST.get("rhave_revenue")
        ris_proprietary_id = req.POST.get("ris_proprietary")
        rname = req.POST.get("rname")
        remail = req.POST.get("remail")
        rmobile = req.POST.get("rmobile")
        rcountry = req.POST.get("rcountry")
        rgender_id = req.POST.get("rgender")
        rtshirt_size_id = req.POST.get("rtshirt_size")
        rcollege = req.POST.get("rcollege")
        rlinkedin = req.POST.get("rlinkedin")
        rsocial_links = req.POST.get("rsocial_links")
        # validators variables
        rwhere_you_know=rcu_passout=rshowcasing_product=rhiring_interns=rhiring_professionals=rhave_revenue=ris_proprietary=rtshirt_size=rgender=''
        vbool=[False,True]
        gen = ["Male","Female","Other"]
        tsize = ['S','M','L','XL','XXL']
        wknow = ['effectus.cutbi.in','Chandigarh University Alumni','Investor','Social Media','Accelerator/Incubator',"Email from Effectus E-Summit '22",'Friend/Advisor','Other']
        # validators conditions
        if rwhere_you_know_id and rwhere_you_know_id.isdigit():
            rwhere_you_know=wknow[int(rwhere_you_know_id)]
        if rshowcasing_product_id and rshowcasing_product_id.isdigit():
            rshowcasing_product=vbool[int(rshowcasing_product_id)]
        if rhiring_interns_id and rhiring_interns_id.isdigit():
            rhiring_interns=vbool[int(rhiring_interns_id)]
        if rhiring_professionals_id and rhiring_professionals_id.isdigit():
            rhiring_professionals=vbool[int(rhiring_professionals_id)]
        if rcu_passout_id and rcu_passout_id.isdigit():
            rcu_passout=vbool[int(rcu_passout_id)]
        if rhave_revenue_id and rhave_revenue_id.isdigit():
            rhave_revenue=vbool[int(rhave_revenue_id)]
        if ris_proprietary_id and ris_proprietary_id.isdigit():
            ris_proprietary=vbool[int(ris_proprietary_id)]
        if rtshirt_size_id and rtshirt_size_id.isdigit():
            rtshirt_size=tsize[int(rtshirt_size_id)]
        if rgender_id and rgender_id.isdigit():
            rgender = gen[int(rgender_id)]
        if len(rcompany_name) > 0 and len(rtotal_employees) > 0 and \
            len(rwhere_you_know) > 0 and len(rdescribe_one_sentence) > 0 and len(rcore_problem) > 0 and \
            len(rbiggest_competitors) > 0 and len(rwhy_unique) > 0 and len(rraise_capital) > 0 and \
            len(rname) > 0 and len(remail) > 0 and re.match('[^@]+@[^@]+\.[^@]+',remail) and len(rmobile) > 0 and len(rcountry) > 0 and \
            len(rtshirt_size) > 0 and len(rcollege) > 0 and len(rlinkedin) > 0:
                tr,_ =participants.objects.get_or_create(name=rname,
                    email=remail,
                    contact=rmobile,
                    gender=rgender,
                    tshirt_size=rtshirt_size)
                startup.objects.create(
                    company_name=rcompany_name,
                    country=rcountry,
                    office_location=roffice_location,
                    total_employees=rtotal_employees,
                    website_url=rwebsite_url,
                    company_category=rcompany_category,
                    industry=rindustry,
                    pitchbook=rpitchbook,
                    where_you_know=rwhere_you_know,
                    showcasing_product=rshowcasing_product,
                    cu_passout=rcu_passout,
                    hiring_interns=rhiring_interns,
                    hiring_professionals=rhiring_professionals,
                    describe_one_sentence=rdescribe_one_sentence,
                    core_problem=rcore_problem,
                    use_case=ruse_case,
                    target_audience=rtarget_audience,
                    business_model=rbusiness_model,
                    biggest_competitors=rbiggest_competitors,
                    why_unique=rwhy_unique,
                    raise_capital=rraise_capital,
                    video_url=rvideo_url,
                    incubator_program=rincubator_program,
                    have_revenue=rhave_revenue,
                    is_proprietary=ris_proprietary,
                    college_name=rcollege,
                    linkedin=rlinkedin,
                    social_links=rsocial_links,
                    team_representative=tr
                )
        else:
            print("in error ----------------------------")





















