# Audio-Technica ATH-ANC70

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 5.7; 96 5.2; 106 4.7; 116 4.2; 128 3.8; 141 3.5; 155 3.3; 170 3.1; 187 3.0; 206 3.0; 227 2.9; 249 3.2; 274 3.5; 302 3.7; 332 4.0; 365 4.3; 402 4.7; 442 5.1; 486 5.6; 535 6.0; 588 6.0; 647 6.0; 712 5.8; 783 4.4; 861 2.6; 947 0.9; 1042 -1.0; 1146 -2.5; 1261 -3.3; 1387 -3.2; 1526 -2.6; 1678 -1.3; 1846 -0.9; 2031 -0.6; 2234 0.6; 2457 0.5; 2703 0.5; 2973 0.2; 3270 0.6; 3597 3.3; 3957 5.0; 4353 5.7; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC70 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC70 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.31 | 6.4 dB  |
| Peaking | 653 Hz  | 0.79 | 7.3 dB  |
| Peaking | 1226 Hz | 1.41 | -6.9 dB |
| Peaking | 4483 Hz | 2.52 | 5.6 dB  |
| Peaking | 5964 Hz | 3.83 | 4.9 dB  |
| Peaking | 84 Hz   | 4.63 | 0.7 dB  |
| Peaking | 3163 Hz | 5.71 | -3.0 dB |
| Peaking | 3291 Hz | 2.56 | 1.7 dB  |
| Peaking | 8274 Hz | 3.75 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audio-Technica%20ATH-ANC70/Audio-Technica%20ATH-ANC70.png)