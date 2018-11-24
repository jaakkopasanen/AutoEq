# AKG K612

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 4.9; 25 4.4; 28 3.7; 31 3.2; 34 2.7; 37 2.3; 41 1.9; 45 1.5; 49 1.2; 54 0.9; 60 0.4; 66 0.1; 72 0.3; 79 0.7; 87 -0.5; 96 -0.2; 106 -0.9; 116 -1.5; 128 -1.9; 141 -2.2; 155 -2.5; 170 -2.5; 187 -2.6; 206 -2.7; 227 -2.6; 249 -2.5; 274 -2.4; 302 -2.3; 332 -2.0; 365 -1.8; 402 -1.7; 442 -1.4; 486 -1.4; 535 -1.1; 588 -0.3; 647 0.2; 712 0.2; 783 0.4; 861 0.1; 947 -0.0; 1042 -0.0; 1146 0.2; 1261 0.5; 1387 0.0; 1526 -0.8; 1678 -1.4; 1846 -2.3; 2031 -3.7; 2234 -4.1; 2457 -4.3; 2703 -4.0; 2973 -2.5; 3270 -0.9; 3597 0.7; 3957 -0.1; 4353 -2.1; 4788 -1.7; 5267 0.9; 5793 0.5; 6373 -1.0; 7010 -2.0; 7711 -2.6; 8482 -3.6; 9330 -2.1; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.5; 18182 -3.3; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K612 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K612 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.61 | 6.4 dB  |
| Peaking | 204 Hz   | 0.78 | -3.0 dB |
| Peaking | 2366 Hz  | 2.53 | -4.8 dB |
| Peaking | 8303 Hz  | 3.84 | -3.7 dB |
| Peaking | 18340 Hz | 3.28 | -3.7 dB |
| Peaking | 1057 Hz  | 1.33 | 0.8 dB  |
| Peaking | 3713 Hz  | 4.03 | 4.6 dB  |
| Peaking | 4510 Hz  | 1.52 | -4.3 dB |
| Peaking | 5370 Hz  | 4.41 | 4.5 dB  |
| Peaking | 10885 Hz | 1.72 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K612/AKG%20K612.png)