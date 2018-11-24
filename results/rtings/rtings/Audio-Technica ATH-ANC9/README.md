# Audio-Technica ATH-ANC9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 -7.5; 23 -7.9; 25 -8.2; 28 -8.5; 31 -8.6; 34 -8.5; 37 -8.2; 41 -7.9; 45 -7.5; 49 -7.1; 54 -6.7; 60 -6.3; 66 -6.2; 72 -6.2; 79 -6.4; 87 -6.8; 96 -7.3; 106 -7.9; 116 -8.3; 128 -8.7; 141 -8.7; 155 -8.4; 170 -7.8; 187 -7.1; 206 -6.2; 227 -5.4; 249 -4.6; 274 -4.1; 302 -3.7; 332 -3.4; 365 -2.9; 402 -2.7; 442 -2.6; 486 -2.6; 535 -2.6; 588 -2.2; 647 -1.1; 712 0.6; 783 1.8; 861 2.5; 947 1.4; 1042 -1.1; 1146 -3.3; 1261 -5.0; 1387 -5.5; 1526 -5.6; 1678 -5.2; 1846 -5.2; 2031 -4.9; 2234 -4.7; 2457 -4.4; 2703 -4.7; 2973 -4.7; 3270 -4.7; 3597 -4.8; 3957 -6.4; 4353 -5.8; 4788 -7.1; 5267 -7.1; 5793 -6.7; 6373 -5.2; 7010 -4.9; 7711 -4.6; 8482 -3.3; 9330 -0.7; 10263 0.0; 11289 -2.4; 12418 -6.8; 13660 -8.9; 15026 -7.0; 16529 -3.6; 18182 -1.1; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.63 | -8.1 dB |
| Peaking | 143 Hz   | 0.74 | -7.8 dB |
| Peaking | 1642 Hz  | 1.86 | -5.1 dB |
| Peaking | 4800 Hz  | 1    | -6.8 dB |
| Peaking | 14061 Hz | 2.39 | -9.2 dB |
| Peaking | 561 Hz   | 1.93 | -2.1 dB |
| Peaking | 849 Hz   | 2.21 | 4.8 dB  |
| Peaking | 1217 Hz  | 3.85 | -2.9 dB |
| Peaking | 10128 Hz | 3.06 | 6.5 dB  |
| Peaking | 10361 Hz | 1.27 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Audio-Technica%20ATH-ANC9/Audio-Technica%20ATH-ANC9.png)