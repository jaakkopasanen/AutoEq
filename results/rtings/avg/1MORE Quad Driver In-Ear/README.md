# 1MORE Quad Driver In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.7; 37 5.2; 41 4.6; 45 4.1; 49 3.6; 54 3.0; 60 2.1; 66 1.3; 72 0.6; 79 -0.1; 87 -1.0; 96 -1.8; 106 -2.8; 116 -3.6; 128 -4.4; 141 -5.1; 155 -5.6; 170 -5.8; 187 -6.0; 206 -6.2; 227 -6.2; 249 -6.1; 274 -5.9; 302 -5.5; 332 -5.1; 365 -4.6; 402 -4.0; 442 -3.3; 486 -2.4; 535 -1.4; 588 -0.5; 647 0.3; 712 0.8; 783 0.9; 861 0.6; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.1; 1387 0.1; 1526 0.0; 1678 -0.2; 1846 -0.5; 2031 -0.7; 2234 -0.4; 2457 0.0; 2703 0.1; 2973 -0.2; 3270 -0.8; 3597 -1.9; 3957 -3.9; 4353 -5.8; 4788 -4.7; 5267 -0.7; 5793 2.5; 6373 5.1; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -1.2; 12418 -5.0; 13660 -7.0; 15026 -5.4; 16529 -2.2; 18182 -3.3; 20000 -10.3
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
| Peaking | 28 Hz    | 0.62 | 6.6 dB  |
| Peaking | 199 Hz   | 0.72 | -7.1 dB |
| Peaking | 4551 Hz  | 3.06 | -8.2 dB |
| Peaking | 6201 Hz  | 1.81 | 6.9 dB  |
| Peaking | 21404 Hz | 0.14 | -5.8 dB |
| Peaking | 389 Hz   | 2.25 | -1.3 dB |
| Peaking | 717 Hz   | 2.01 | 2.2 dB  |
| Peaking | 10764 Hz | 3.19 | 3.9 dB  |
| Peaking | 13466 Hz | 1.83 | -4.2 dB |
| Peaking | 16874 Hz | 2.75 | 4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Quad%20Driver%20In-Ear/1MORE%20Quad%20Driver%20In-Ear.png)