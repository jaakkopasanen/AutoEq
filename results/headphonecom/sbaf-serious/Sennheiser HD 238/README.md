# Sennheiser HD 238

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 21 0.0; 23 3.5; 25 2.8; 28 1.9; 31 1.2; 34 0.7; 37 0.2; 41 -0.3; 45 -0.5; 49 -0.9; 54 -1.5; 60 -1.9; 66 -1.9; 72 -2.4; 79 -2.9; 87 -3.4; 96 -3.7; 106 -4.1; 116 -4.2; 128 -4.5; 141 -4.4; 155 -4.4; 170 -4.6; 187 -4.4; 206 -4.3; 227 -4.1; 249 -3.9; 274 -3.6; 302 -3.3; 332 -2.9; 365 -2.4; 402 -2.1; 442 -1.8; 486 -1.5; 535 -1.2; 588 -0.8; 647 -0.4; 712 -0.2; 783 -0.0; 861 0.1; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.6; 1387 -1.3; 1526 -2.1; 1678 -1.4; 1846 -1.3; 2031 -0.2; 2234 1.2; 2457 2.1; 2703 0.5; 2973 -2.0; 3270 -3.5; 3597 -0.0; 3957 1.1; 4353 -3.8; 4788 -2.5; 5267 0.2; 5793 -1.0; 6373 -1.8; 7010 -1.1; 7711 -0.3; 8482 -1.7; 9330 -2.7; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.0; 16529 -1.3; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 238 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 238 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.3  | 4.8 dB  |
| Peaking | 122 Hz   | 0.62 | -3.9 dB |
| Peaking | 258 Hz   | 1.02 | -2.0 dB |
| Peaking | 6041 Hz  | 0.57 | -1.4 dB |
| Peaking | 21815 Hz | 1.19 | -1.3 dB |
| Peaking | 1713 Hz  | 2.64 | -2.4 dB |
| Peaking | 2600 Hz  | 2.04 | 4.1 dB  |
| Peaking | 2895 Hz  | 5.45 | -3.3 dB |
| Peaking | 3244 Hz  | 9.96 | -3.7 dB |
| Peaking | 15779 Hz | 5.69 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20238/Sennheiser%20HD%20238.png)