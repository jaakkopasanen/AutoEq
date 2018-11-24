# Focal Utopia snA1BEHG003253

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 21 0.0; 23 3.7; 25 3.5; 28 3.2; 31 3.0; 34 2.8; 37 2.6; 41 2.4; 45 2.2; 49 2.1; 54 1.8; 60 1.5; 66 1.2; 72 0.9; 79 0.6; 87 0.3; 96 -0.2; 106 -0.4; 116 -0.5; 128 -0.8; 141 -0.9; 155 -1.0; 170 -1.0; 187 -0.9; 206 -0.9; 227 -0.7; 249 -0.6; 274 -0.4; 302 -0.3; 332 -0.1; 365 0.1; 402 0.3; 442 0.5; 486 0.5; 535 0.7; 588 1.0; 647 1.0; 712 0.8; 783 0.9; 861 0.5; 947 0.3; 1042 0.0; 1146 -0.6; 1261 -1.3; 1387 -1.2; 1526 -0.6; 1678 -0.4; 1846 0.3; 2031 0.9; 2234 1.0; 2457 0.0; 2703 0.0; 2973 1.1; 3270 1.8; 3597 2.7; 3957 -0.3; 4353 -0.1; 4788 1.9; 5267 4.5; 5793 2.2; 6373 0.1; 7010 2.5; 7711 0.3; 8482 -1.8; 9330 -1.4; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.1; 18182 -1.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Utopia snA1BEHG003253 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Utopia snA1BEHG003253 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.32 | 3.9 dB  |
| Peaking | 45 Hz    | 2.12 | 1.7 dB  |
| Peaking | 5313 Hz  | 6.55 | 4.9 dB  |
| Peaking | 6873 Hz  | 8.76 | 2.6 dB  |
| Peaking | 8804 Hz  | 7.57 | -2.9 dB |
| Peaking | 181 Hz   | 1.07 | -1.3 dB |
| Peaking | 917 Hz   | 0.56 | 1.3 dB  |
| Peaking | 1293 Hz  | 2.4  | -2.5 dB |
| Peaking | 3469 Hz  | 8.51 | 2.6 dB  |
| Peaking | 18248 Hz | 3.73 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Utopia%20snA1BEHG003253/Focal%20Utopia%20snA1BEHG003253.png)