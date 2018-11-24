# Audio-Technica ATH-ANC70

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.9; 87 5.3; 96 4.8; 106 4.2; 116 3.7; 128 3.2; 141 2.9; 155 2.7; 170 2.5; 187 2.4; 206 2.5; 227 2.5; 249 2.6; 274 2.8; 302 2.9; 332 3.0; 365 3.3; 402 3.6; 442 4.0; 486 4.4; 535 4.9; 588 5.3; 647 5.4; 712 5.0; 783 3.9; 861 2.4; 947 0.9; 1042 -1.0; 1146 -2.7; 1261 -3.6; 1387 -3.2; 1526 -2.2; 1678 -1.0; 1846 -1.0; 2031 -1.0; 2234 0.2; 2457 0.0; 2703 -0.3; 2973 -1.4; 3270 -1.9; 3597 0.1; 3957 2.6; 4353 4.5; 4788 6.0; 5267 6.0; 5793 6.0; 6373 3.6; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.2; 12418 -2.6; 13660 -3.7; 15026 -2.8; 16529 -0.1; 18182 -0.6; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC70 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC70 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.34 | 6.4 dB   |
| Peaking | 730 Hz   | 0.83 | 8.4 dB   |
| Peaking | 1161 Hz  | 1.08 | -7.9 dB  |
| Peaking | 5236 Hz  | 2.52 | 7.1 dB   |
| Peaking | 20255 Hz | 2.13 | -13.3 dB |
| Peaking | 3213 Hz  | 3.65 | -5.3 dB  |
| Peaking | 3354 Hz  | 1.46 | 2.6 dB   |
| Peaking | 13898 Hz | 2.31 | -4.1 dB  |
| Peaking | 17555 Hz | 1.97 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC70/Audio-Technica%20ATH-ANC70.png)