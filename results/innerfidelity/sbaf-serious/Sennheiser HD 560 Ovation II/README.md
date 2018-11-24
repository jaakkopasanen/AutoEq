# Sennheiser HD 560 Ovation II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.9; 66 5.1; 72 4.2; 79 3.4; 87 2.6; 96 1.9; 106 1.3; 116 0.9; 128 0.4; 141 -0.0; 155 -0.4; 170 -0.5; 187 -0.6; 206 -0.7; 227 -0.7; 249 -0.6; 274 -0.6; 302 -0.5; 332 -0.6; 365 -0.3; 402 -0.3; 442 -0.1; 486 -0.1; 535 -0.2; 588 0.3; 647 0.2; 712 0.1; 783 0.3; 861 0.0; 947 -0.1; 1042 -0.3; 1146 -0.2; 1261 -0.7; 1387 -1.4; 1526 -2.1; 1678 -2.6; 1846 -2.8; 2031 -3.1; 2234 -3.7; 2457 -4.0; 2703 -4.5; 2973 -4.0; 3270 -3.2; 3597 -2.1; 3957 -2.1; 4353 -2.7; 4788 -2.5; 5267 -0.8; 5793 5.4; 6373 5.2; 7010 0.8; 7711 -3.3; 8482 -4.6; 9330 -2.2; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.7; 15026 -0.2; 16529 0.0; 18182 -0.2; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 560 Ovation II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 560 Ovation II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.71 | 7.0 dB  |
| Peaking | 2523 Hz | 1.25 | -4.3 dB |
| Peaking | 4970 Hz | 3.22 | -4.0 dB |
| Peaking | 6034 Hz | 3.53 | 8.9 dB  |
| Peaking | 8210 Hz | 3.88 | -5.8 dB |
| Peaking | 40 Hz   | 2.75 | -1.4 dB |
| Peaking | 64 Hz   | 2.02 | 1.7 dB  |
| Peaking | 176 Hz  | 1.06 | -1.3 dB |
| Peaking | 9130 Hz | 7.69 | -1.3 dB |
| Peaking | 9912 Hz | 4.68 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20560%20Ovation%20II/Sennheiser%20HD%20560%20Ovation%20II.png)