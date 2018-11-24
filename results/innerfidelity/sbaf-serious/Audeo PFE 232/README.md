# Audeo PFE 232

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 -3.9; 23 -4.0; 25 -4.1; 28 -4.2; 31 -4.4; 34 -4.5; 37 -4.6; 41 -4.6; 45 -4.7; 49 -4.9; 54 -5.1; 60 -5.4; 66 -5.7; 72 -5.9; 79 -6.2; 87 -6.6; 96 -6.9; 106 -7.2; 116 -7.2; 128 -7.4; 141 -7.5; 155 -7.4; 170 -7.4; 187 -7.2; 206 -7.0; 227 -6.7; 249 -6.4; 274 -6.0; 302 -5.5; 332 -5.0; 365 -4.4; 402 -3.9; 442 -3.2; 486 -2.8; 535 -2.2; 588 -1.4; 647 -0.9; 712 -0.7; 783 -0.2; 861 0.1; 947 0.1; 1042 -0.1; 1146 -0.1; 1261 -0.4; 1387 -0.7; 1526 -1.1; 1678 -1.4; 1846 -1.2; 2031 -0.9; 2234 -0.5; 2457 0.7; 2703 2.1; 2973 3.1; 3270 3.1; 3597 2.7; 3957 2.7; 4353 2.4; 4788 2.6; 5267 2.7; 5793 2.6; 6373 -0.2; 7010 1.2; 7711 0.1; 8482 -3.5; 9330 -5.8; 10263 -3.8; 11289 -0.3; 12418 -0.5; 13660 -7.4; 15026 -10.8; 16529 -0.8; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeo PFE 232 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 232 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.25 | -3.9 dB  |
| Peaking | 146 Hz   | 0.7  | -4.9 dB  |
| Peaking | 299 Hz   | 1.18 | -2.8 dB  |
| Peaking | 14590 Hz | 3.6  | -12.3 dB |
| Peaking | 24000 Hz | 1.89 | -6.6 dB  |
| Peaking | 1935 Hz  | 2.16 | -2.0 dB  |
| Peaking | 3013 Hz  | 2.6  | 2.4 dB   |
| Peaking | 4920 Hz  | 0.92 | 2.6 dB   |
| Peaking | 9362 Hz  | 3.46 | -6.7 dB  |
| Peaking | 11906 Hz | 4.87 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeo%20PFE%20232/Audeo%20PFE%20232.png)