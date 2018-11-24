# Sennheiser CX 200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.5; 23 -1.8; 25 -2.1; 28 -2.4; 31 -2.8; 34 -3.0; 37 -3.1; 41 -3.3; 45 -3.5; 49 -3.7; 54 -3.9; 60 -4.0; 66 -4.3; 72 -4.4; 79 -4.6; 87 -4.8; 96 -4.9; 106 -4.9; 116 -4.8; 128 -4.9; 141 -4.8; 155 -4.6; 170 -4.4; 187 -4.1; 206 -3.8; 227 -3.4; 249 -3.1; 274 -2.7; 302 -2.3; 332 -1.9; 365 -1.5; 402 -1.2; 442 -0.7; 486 -0.5; 535 -0.2; 588 0.3; 647 0.5; 712 0.5; 783 0.8; 861 0.5; 947 0.1; 1042 -0.2; 1146 -0.8; 1261 -1.0; 1387 -1.6; 1526 -2.1; 1678 -2.2; 1846 -1.7; 2031 -0.9; 2234 0.4; 2457 2.3; 2703 3.7; 2973 5.7; 3270 6.0; 3597 6.0; 3957 5.9; 4353 3.8; 4788 2.3; 5267 2.0; 5793 1.1; 6373 -0.1; 7010 -0.0; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.6; 11289 -1.3; 12418 0.0; 13660 -0.7; 15026 -2.4; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 13 Hz    |  1.02 | -1.4 dB |
| Peaking | 70 Hz    |  0.5  | -3.9 dB |
| Peaking | 173 Hz   |  0.92 | -2.7 dB |
| Peaking | 1718 Hz  |  2.28 | -3.3 dB |
| Peaking | 3385 Hz  |  1.77 | 7.0 dB  |
| Peaking | 315 Hz   |  2.33 | -0.5 dB |
| Peaking | 744 Hz   |  1.45 | 1.2 dB  |
| Peaking | 1222 Hz  |  2.5  | -0.7 dB |
| Peaking | 4076 Hz  | 12.48 | 1.2 dB  |
| Peaking | 13463 Hz |  0.81 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20CX%20200/Sennheiser%20CX%20200.png)