# Sennheiser RS 185

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 21 0.0; 23 0.2; 25 -0.2; 28 -0.8; 31 -1.3; 34 -1.6; 37 -1.9; 41 -2.1; 45 -2.2; 49 -2.3; 54 -2.4; 60 -2.6; 66 -3.0; 72 -3.3; 79 -3.7; 87 -4.0; 96 -4.4; 106 -4.8; 116 -5.1; 128 -5.4; 141 -5.6; 155 -5.8; 170 -5.8; 187 -5.7; 206 -5.5; 227 -5.4; 249 -5.2; 274 -5.1; 302 -4.9; 332 -4.8; 365 -4.6; 402 -4.4; 442 -4.3; 486 -4.0; 535 -2.7; 588 -1.6; 647 -1.3; 712 -1.4; 783 -1.1; 861 0.9; 947 0.2; 1042 -0.3; 1146 -0.7; 1261 -1.0; 1387 -0.9; 1526 -0.3; 1678 -0.5; 1846 -0.9; 2031 -1.4; 2234 -3.2; 2457 -5.8; 2703 -7.2; 2973 -7.9; 3270 -7.8; 3597 -5.6; 3957 -3.3; 4353 -2.0; 4788 1.3; 5267 3.8; 5793 2.8; 6373 4.8; 7010 2.5; 7711 0.3; 8482 -0.3; 9330 -3.4; 10263 -5.3; 11289 -3.2; 12418 -0.0; 13660 0.0; 15026 -1.2; 16529 -0.3; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 185 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 185 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 150 Hz   | 0.53 | -5.6 dB |
| Peaking | 390 Hz   | 1.77 | -2.4 dB |
| Peaking | 3089 Hz  | 2.04 | -9.3 dB |
| Peaking | 5921 Hz  | 1.86 | 5.5 dB  |
| Peaking | 10145 Hz | 3.36 | -6.2 dB |
| Peaking | 42 Hz    | 2.9  | -0.7 dB |
| Peaking | 489 Hz   | 8.43 | -0.9 dB |
| Peaking | 891 Hz   | 7.17 | 1.9 dB  |
| Peaking | 1868 Hz  | 2.54 | 1.1 dB  |
| Peaking | 2484 Hz  | 7.51 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20RS%20185/Sennheiser%20RS%20185.png)