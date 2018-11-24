# Audio-Technica ATH-ANC7B SVIS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 21 0.0; 23 5.2; 25 4.6; 28 3.7; 31 2.9; 34 2.3; 37 1.8; 41 1.2; 45 0.8; 49 0.4; 54 -0.2; 60 -0.6; 66 -0.7; 72 -0.7; 79 -0.7; 87 -0.7; 96 -1.0; 106 -1.5; 116 -2.0; 128 -2.2; 141 -2.3; 155 -2.3; 170 -2.0; 187 -1.7; 206 -1.5; 227 -1.3; 249 -1.0; 274 -0.6; 302 -0.3; 332 -0.0; 365 0.2; 402 0.2; 442 0.1; 486 -0.2; 535 -0.6; 588 -1.3; 647 -0.4; 712 2.0; 783 2.6; 861 1.2; 947 -0.5; 1042 1.9; 1146 5.5; 1261 6.0; 1387 6.0; 1526 6.0; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.1; 15026 -1.3; 16529 -2.4; 18182 -1.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC7B SVIS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC7B SVIS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.23 | 6.2 dB  |
| Peaking | 143 Hz   | 0.88 | -2.4 dB |
| Peaking | 1515 Hz  | 1.53 | 4.7 dB  |
| Peaking | 4407 Hz  | 0.62 | 7.9 dB  |
| Peaking | 9910 Hz  | 0.38 | -2.9 dB |
| Peaking | 606 Hz   | 3.36 | -3.8 dB |
| Peaking | 802 Hz   | 1.4  | 3.3 dB  |
| Peaking | 943 Hz   | 5.43 | -5.4 dB |
| Peaking | 7951 Hz  | 6.52 | -2.1 dB |
| Peaking | 12702 Hz | 3.62 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audio-Technica%20ATH-ANC7B%20SVIS/Audio-Technica%20ATH-ANC7B%20SVIS.png)