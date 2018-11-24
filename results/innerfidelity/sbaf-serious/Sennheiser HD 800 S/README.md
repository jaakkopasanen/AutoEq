# Sennheiser HD 800 S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 0.0; 23 4.1; 25 3.7; 28 3.2; 31 2.7; 34 2.4; 37 2.1; 41 1.7; 45 1.5; 49 1.4; 54 1.2; 60 1.0; 66 0.9; 72 0.8; 79 0.1; 87 -0.5; 96 -1.1; 106 -1.6; 116 -1.9; 128 -2.3; 141 -2.5; 155 -2.7; 170 -2.7; 187 -2.9; 206 -3.0; 227 -3.0; 249 -3.0; 274 -2.9; 302 -2.8; 332 -2.7; 365 -2.5; 402 -2.3; 442 -2.0; 486 -2.0; 535 -1.8; 588 -1.3; 647 -1.2; 712 -1.1; 783 -0.6; 861 -0.5; 947 -0.2; 1042 0.3; 1146 0.5; 1261 1.0; 1387 1.4; 1526 1.8; 1678 1.6; 1846 1.5; 2031 1.8; 2234 1.6; 2457 2.1; 2703 2.4; 2973 1.9; 3270 2.2; 3597 1.5; 3957 0.3; 4353 -0.2; 4788 0.1; 5267 -0.8; 5793 -1.1; 6373 -3.8; 7010 -3.5; 7711 -2.0; 8482 -1.0; 9330 -0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.53 | 5.5 dB  |
| Peaking | 70 Hz   | 1.46 | 1.8 dB  |
| Peaking | 200 Hz  | 0.33 | -3.2 dB |
| Peaking | 2162 Hz | 0.68 | 2.3 dB  |
| Peaking | 6712 Hz | 3.21 | -4.6 dB |
| Peaking | 35 Hz   | 0.7  | 0.2 dB  |
| Peaking | 2159 Hz | 4.24 | -0.6 dB |
| Peaking | 3600 Hz | 1.99 | 1.3 dB  |
| Peaking | 4085 Hz | 4.01 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20800%20S/Sennheiser%20HD%20800%20S.png)