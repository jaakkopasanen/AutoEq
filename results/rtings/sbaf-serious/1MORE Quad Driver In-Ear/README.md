# 1MORE Quad Driver In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.6; 37 5.1; 41 4.4; 45 3.8; 49 3.3; 54 2.6; 60 1.8; 66 1.2; 72 0.6; 79 0.1; 87 -0.6; 96 -1.4; 106 -2.3; 116 -3.1; 128 -3.9; 141 -4.5; 155 -4.9; 170 -5.2; 187 -5.4; 206 -5.7; 227 -5.7; 249 -5.6; 274 -5.2; 302 -4.7; 332 -4.2; 365 -3.6; 402 -2.9; 442 -2.2; 486 -1.2; 535 -0.2; 588 0.6; 647 1.4; 712 1.7; 783 1.4; 861 0.8; 947 0.1; 1042 0.0; 1146 -0.0; 1261 0.1; 1387 0.1; 1526 -0.4; 1678 -0.6; 1846 -0.4; 2031 -0.3; 2234 0.1; 2457 0.5; 2703 0.9; 2973 1.3; 3270 1.8; 3597 1.3; 3957 -1.5; 4353 -4.5; 4788 -3.1; 5267 2.3; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.1; 15026 -0.0; 16529 0.0; 18182 0.0; 20000 -2.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Quad Driver In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Quad Driver In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.7  | 6.5 dB  |
| Peaking | 196 Hz  | 0.85 | -6.4 dB |
| Peaking | 3460 Hz | 2.6  | 3.1 dB  |
| Peaking | 4490 Hz | 3.42 | -7.3 dB |
| Peaking | 5945 Hz | 3.48 | 7.6 dB  |
| Peaking | 199 Hz  | 2.23 | 1.6 dB  |
| Peaking | 322 Hz  | 0.58 | -1.5 dB |
| Peaking | 670 Hz  | 1.8  | 3.2 dB  |
| Peaking | 1755 Hz | 3.89 | -0.6 dB |
| Peaking | 8100 Hz | 5.48 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/1MORE%20Quad%20Driver%20In-Ear/1MORE%20Quad%20Driver%20In-Ear.png)