# Polk Audio UltraFocus 8000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 21 -7.1; 23 -6.5; 25 -5.9; 28 -5.2; 31 -4.7; 34 -4.2; 37 -3.8; 41 -3.4; 45 -3.2; 49 -3.0; 54 -2.7; 60 -2.5; 66 -2.4; 72 -2.3; 79 -2.1; 87 -2.0; 96 -1.9; 106 -2.0; 116 -2.0; 128 -2.0; 141 -1.9; 155 -1.8; 170 -1.9; 187 -1.9; 206 -1.9; 227 -1.8; 249 -1.8; 274 -1.6; 302 -1.4; 332 -1.0; 365 -0.9; 402 -0.9; 442 -0.7; 486 -0.6; 535 -0.5; 588 -0.5; 647 -0.2; 712 -0.3; 783 -0.2; 861 -0.2; 947 0.1; 1042 -0.1; 1146 -0.0; 1261 -0.1; 1387 -0.3; 1526 -0.8; 1678 -1.3; 1846 -1.6; 2031 -1.4; 2234 -0.7; 2457 0.5; 2703 1.3; 2973 1.4; 3270 0.6; 3597 -0.7; 3957 -2.9; 4353 -3.3; 4788 -3.2; 5267 -1.5; 5793 1.0; 6373 3.6; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.2; 11289 -1.1; 12418 -2.6; 13660 -3.5; 15026 -2.9; 16529 -2.8; 18182 -2.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFocus 8000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFocus 8000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.45 | -8.3 dB |
| Peaking | 173 Hz   | 0.53 | -1.7 dB |
| Peaking | 4513 Hz  | 3.71 | -4.1 dB |
| Peaking | 6550 Hz  | 4.56 | 4.9 dB  |
| Peaking | 15604 Hz | 0.94 | -3.4 dB |
| Peaking | 1924 Hz  | 2.94 | -1.9 dB |
| Peaking | 2869 Hz  | 2.77 | 2.2 dB  |
| Peaking | 3947 Hz  | 7.35 | -1.4 dB |
| Peaking | 10087 Hz | 4.13 | 0.9 dB  |
| Peaking | 12953 Hz | 5.24 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Polk%20Audio%20UltraFocus%208000/Polk%20Audio%20UltraFocus%208000.png)