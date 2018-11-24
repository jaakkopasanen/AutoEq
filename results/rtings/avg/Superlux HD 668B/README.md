# Superlux HD 668B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 0.0; 23 4.2; 25 3.4; 28 2.4; 31 1.5; 34 0.6; 37 -0.1; 41 -0.9; 45 -1.6; 49 -2.0; 54 -2.5; 60 -3.0; 66 -3.5; 72 -3.9; 79 -4.3; 87 -4.7; 96 -4.9; 106 -5.0; 116 -5.0; 128 -4.8; 141 -4.4; 155 -3.9; 170 -3.2; 187 -2.6; 206 -2.3; 227 -2.2; 249 -2.2; 274 -2.2; 302 -2.3; 332 -2.3; 365 -1.9; 402 -1.9; 442 -2.0; 486 -1.8; 535 -0.9; 588 -1.1; 647 -1.1; 712 -0.9; 783 -0.7; 861 -0.3; 947 -0.2; 1042 0.1; 1146 0.2; 1261 0.0; 1387 -0.3; 1526 -1.1; 1678 -2.5; 1846 -4.3; 2031 -5.6; 2234 -5.1; 2457 -4.3; 2703 -3.3; 2973 -2.7; 3270 -2.6; 3597 -1.2; 3957 0.2; 4353 1.7; 4788 1.6; 5267 -6.7; 5793 -7.9; 6373 -5.1; 7010 -3.9; 7711 -4.8; 8482 -6.6; 9330 -7.6; 10263 -8.0; 11289 -7.9; 12418 -5.9; 13660 -5.3; 15026 -8.2; 16529 -7.7; 18182 -4.6; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 668B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 668B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 3.81 | 5.0 dB  |
| Peaking | 2128 Hz  | 2.61 | -5.5 dB |
| Peaking | 9741 Hz  | 0.89 | -7.3 dB |
| Peaking | 15869 Hz | 2.39 | -6.2 dB |
| Peaking | 20314 Hz | 1.51 | -6.8 dB |
| Peaking | 103 Hz   | 0.82 | -5.1 dB |
| Peaking | 371 Hz   | 1.34 | -1.5 dB |
| Peaking | 4708 Hz  | 4.15 | 7.0 dB  |
| Peaking | 5510 Hz  | 5.02 | -8.9 dB |
| Peaking | 7229 Hz  | 4.41 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Superlux%20HD%20668B/Superlux%20HD%20668B.png)