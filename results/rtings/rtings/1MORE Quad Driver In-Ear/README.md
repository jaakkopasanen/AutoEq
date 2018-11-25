# 1MORE Quad Driver In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.7; 37 5.2; 41 4.6; 45 4.1; 49 3.6; 54 3.0; 60 2.1; 66 1.3; 72 0.6; 79 -0.1; 87 -1.0; 96 -1.8; 106 -2.8; 116 -3.6; 128 -4.4; 141 -5.1; 155 -5.6; 170 -5.8; 187 -6.0; 206 -6.2; 227 -6.2; 249 -6.1; 274 -5.9; 302 -5.5; 332 -5.1; 365 -4.6; 402 -4.0; 442 -3.3; 486 -2.4; 535 -1.4; 588 -0.5; 647 0.3; 712 0.8; 783 0.9; 861 0.6; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.1; 1387 0.1; 1526 0.0; 1678 -0.2; 1846 -0.5; 2031 -0.7; 2234 -0.4; 2457 0.1; 2703 0.3; 2973 0.3; 3270 -0.0; 3597 -0.9; 3957 -2.7; 4353 -4.5; 4788 -2.9; 5267 1.9; 5793 5.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.3; 12418 -1.7; 13660 -3.8; 15026 -2.8; 16529 -0.0; 18182 0.0; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Quad Driver In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Quad Driver In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.61 | 6.6 dB  |
| Peaking | 198 Hz   | 0.72 | -7.1 dB |
| Peaking | 4414 Hz  | 4.35 | -6.0 dB |
| Peaking | 6026 Hz  | 3.57 | 6.9 dB  |
| Peaking | 14004 Hz | 3    | -4.2 dB |
| Peaking | 210 Hz   | 1.83 | 1.6 dB  |
| Peaking | 378 Hz   | 0.59 | -1.8 dB |
| Peaking | 713 Hz   | 1.41 | 3.1 dB  |
| Peaking | 997 Hz   | 2.57 | -0.4 dB |
| Peaking | 6656 Hz  | 4.95 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/1MORE%20Quad%20Driver%20In-Ear/1MORE%20Quad%20Driver%20In-Ear.png)