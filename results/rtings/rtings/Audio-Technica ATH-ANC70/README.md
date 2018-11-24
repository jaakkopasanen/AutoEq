# Audio-Technica ATH-ANC70

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.9; 87 5.3; 96 4.8; 106 4.2; 116 3.7; 128 3.2; 141 2.9; 155 2.7; 170 2.5; 187 2.4; 206 2.5; 227 2.5; 249 2.6; 274 2.8; 302 2.9; 332 3.0; 365 3.3; 402 3.6; 442 4.0; 486 4.4; 535 4.9; 588 5.3; 647 5.4; 712 5.0; 783 3.9; 861 2.4; 947 0.9; 1042 -1.0; 1146 -2.7; 1261 -3.6; 1387 -3.2; 1526 -2.2; 1678 -1.0; 1846 -1.0; 2031 -1.0; 2234 0.1; 2457 0.1; 2703 -0.1; 2973 -0.9; 3270 -1.2; 3597 1.1; 3957 3.8; 4353 5.6; 4788 6.0; 5267 6.0; 5793 6.0; 6373 4.8; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.4; 15026 -0.3; 16529 0.0; 18182 0.0; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC70 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC70 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.34 | 6.4 dB  |
| Peaking | 682 Hz   | 0.84 | 6.5 dB  |
| Peaking | 1219 Hz  | 1.49 | -6.7 dB |
| Peaking | 3192 Hz  | 5.14 | -3.3 dB |
| Peaking | 5024 Hz  | 1.79 | 7.0 dB  |
| Peaking | 78 Hz    | 4.81 | 0.8 dB  |
| Peaking | 6483 Hz  | 4.22 | 3.2 dB  |
| Peaking | 7442 Hz  | 1.79 | -2.2 dB |
| Peaking | 19998 Hz | 5.3  | -5.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Audio-Technica%20ATH-ANC70/Audio-Technica%20ATH-ANC70.png)