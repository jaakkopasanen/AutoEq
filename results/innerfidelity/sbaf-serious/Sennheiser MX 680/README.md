# Sennheiser MX 680

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 5.9; 206 5.3; 227 4.9; 249 4.4; 274 4.1; 302 3.7; 332 3.4; 365 3.3; 402 3.5; 442 3.2; 486 3.1; 535 2.8; 588 2.7; 647 2.0; 712 1.6; 783 1.4; 861 0.9; 947 0.3; 1042 0.1; 1146 -0.6; 1261 -1.7; 1387 -3.2; 1526 -5.1; 1678 -7.1; 1846 -9.0; 2031 -10.5; 2234 -11.2; 2457 -10.8; 2703 -10.1; 2973 -7.1; 3270 -4.1; 3597 -2.1; 3957 -2.3; 4353 -4.2; 4788 -5.3; 5267 -6.4; 5793 -9.2; 6373 -10.1; 7010 -7.5; 7711 -5.6; 8482 -5.8; 9330 -5.5; 10263 -2.3; 11289 0.0; 12418 0.0; 13660 -0.4; 15026 -2.2; 16529 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MX 680 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MX 680 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.1  | 5.7 dB   |
| Peaking | 347 Hz   | 0.26 | 2.3 dB   |
| Peaking | 2168 Hz  | 1.6  | -12.3 dB |
| Peaking | 6477 Hz  | 1.82 | -9.2 dB  |
| Peaking | 15068 Hz | 7.53 | -2.1 dB  |
| Peaking | 2733 Hz  | 6.9  | -2.7 dB  |
| Peaking | 3637 Hz  | 5.06 | 2.7 dB   |
| Peaking | 5873 Hz  | 3.31 | -2.2 dB  |
| Peaking | 8732 Hz  | 1.2  | 4.1 dB   |
| Peaking | 9082 Hz  | 3.28 | -6.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20MX%20680/Sennheiser%20MX%20680.png)