# 1MORE Quad Driver

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.8dB
GraphicEQ: 21 0.0; 23 1.3; 25 0.7; 28 0.3; 31 -0.3; 34 -1.0; 37 -1.5; 41 -2.2; 45 -2.7; 49 -3.2; 54 -4.0; 60 -4.7; 66 -5.5; 72 -5.9; 79 -6.6; 87 -6.8; 96 -7.1; 106 -7.7; 116 -7.7; 128 -8.2; 141 -8.1; 155 -8.2; 170 -8.2; 187 -8.2; 206 -8.2; 227 -8.0; 249 -7.7; 274 -7.4; 302 -7.0; 332 -6.7; 365 -6.2; 402 -5.7; 442 -5.2; 486 -4.6; 535 -4.0; 588 -3.4; 647 -2.7; 712 -2.0; 783 -1.2; 861 -0.6; 947 -0.1; 1042 -0.0; 1146 -0.3; 1261 -0.7; 1387 -0.8; 1526 -0.9; 1678 -0.6; 1846 -0.3; 2031 -0.4; 2234 -0.8; 2457 -1.4; 2703 -1.8; 2973 -1.7; 3270 -1.3; 3597 -1.2; 3957 -2.0; 4353 -3.0; 4788 -2.2; 5267 -0.4; 5793 1.2; 6373 2.4; 7010 -1.3; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -1.2; 12418 -5.2; 13660 -8.4; 15026 -10.1; 16529 -11.3; 18182 -12.6; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Quad Driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-28**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Quad Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.78 | 4.1 dB   |
| Peaking | 120 Hz   | 0.46 | -7.4 dB  |
| Peaking | 319 Hz   | 0.84 | -3.6 dB  |
| Peaking | 4263 Hz  | 5.39 | -2.8 dB  |
| Peaking | 17867 Hz | 0.92 | -13.9 dB |
| Peaking | 958 Hz   | 4.11 | 1.3 dB   |
| Peaking | 2787 Hz  | 3.02 | -1.6 dB  |
| Peaking | 6159 Hz  | 7.87 | 3.6 dB   |
| Peaking | 10502 Hz | 1.91 | 3.5 dB   |
| Peaking | 13667 Hz | 2.39 | -4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/1MORE%20Quad%20Driver/1MORE%20Quad%20Driver.png)