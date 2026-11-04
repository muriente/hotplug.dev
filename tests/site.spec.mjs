import {test,expect} from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
for(const path of ['/','/guide/','/privacy/','/404.html'])test(`${path} accessibility and responsive layout`,async({page})=>{
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 const live404=path==='/404.html'&&process.env.SITE_URL;
 const response=await page.goto(live404?'/not-found-acceptance/':path);expect(response.status()).toBe(live404?404:200);
 await expect(page.locator('h1')).toBeVisible();
 expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBeTruthy();
 const audit=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']).analyze();expect(audit.violations).toEqual([]);expect(errors).toEqual([]);
 if(path==='/'){await page.screenshot({path:`artifacts/${test.info().project.name}.png`,fullPage:true});}
});
test('skip link, native disclosures and navigation work by keyboard',async({page})=>{
 await page.goto('/');await page.keyboard.press('Tab');await expect(page.getByRole('link',{name:'Skip to content'})).toBeFocused();await page.keyboard.press('Enter');await expect(page.locator('h1')).toBeFocused();
 const summary=page.locator('summary').first();await summary.focus();await page.keyboard.press('Enter');await expect(page.locator('details').first()).toHaveAttribute('open','');await page.keyboard.press('Space');await expect(page.locator('details').first()).not.toHaveAttribute('open','');
 await page.getByRole('link',{name:'Project guide',exact:true}).click();await expect(page).toHaveURL(/\/guide\/$/);
});
test('320px and enlarged text still reflow',async({page})=>{
 await page.setViewportSize({width:320,height:800});await page.goto('/');await page.addStyleTag({content:'html {font-size: 200% !important}'});expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBeTruthy();
});
