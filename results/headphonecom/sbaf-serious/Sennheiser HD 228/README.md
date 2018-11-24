# Sennheiser HD 228

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 -2.5; 23 -2.9; 25 -3.3; 28 -3.8; 31 -4.2; 34 -4.6; 37 -4.9; 41 -5.3; 45 -5.6; 49 -5.8; 54 -6.1; 60 -6.5; 66 -6.9; 72 -7.3; 79 -7.6; 87 -7.4; 96 -6.9; 106 -6.8; 116 -7.7; 128 -8.8; 141 -9.3; 155 -9.2; 170 -8.4; 187 -7.7; 206 -5.9; 227 -4.3; 249 -5.7; 274 -5.3; 302 -4.6; 332 -3.8; 365 -3.2; 402 -2.4; 442 -1.4; 486 -0.6; 535 0.1; 588 0.7; 647 1.0; 712 1.1; 783 0.8; 861 0.5; 947 0.2; 1042 0.0; 1146 0.4; 1261 0.7; 1387 1.0; 1526 0.9; 1678 -0.2; 1846 0.6; 2031 1.0; 2234 1.6; 2457 2.4; 2703 2.8; 2973 3.3; 3270 3.9; 3597 5.1; 3957 4.0; 4353 -0.8; 4788 -3.8; 5267 -0.5; 5793 2.4; 6373 1.4; 7010 0.9; 7711 -0.6; 8482 -1.9; 9330 -0.4; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.7; 18182 -4.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 228 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 228 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 62 Hz    | 0.54 | -6.3 dB |
| Peaking | 153 Hz   | 1.62 | -6.4 dB |
| Peaking | 290 Hz   | 2.56 | -3.1 dB |
| Peaking | 3794 Hz  | 1.48 | 6.3 dB  |
| Peaking | 4618 Hz  | 4.71 | -8.5 dB |
| Peaking | 307 Hz   | 5.27 | 0.7 dB  |
| Peaking | 373 Hz   | 2.47 | -1.1 dB |
| Peaking | 639 Hz   | 1.96 | 1.6 dB  |
| Peaking | 5854 Hz  | 8.52 | 1.6 dB  |
| Peaking | 19441 Hz | 1.48 | -6.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20228/Sennheiser%20HD%20228.png)