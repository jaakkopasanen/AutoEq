# Sennheiser HD 650 (balanced)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.6; 25 5.1; 28 4.3; 31 3.6; 34 3.1; 37 2.7; 41 2.2; 45 2.0; 49 2.0; 54 1.4; 60 0.4; 66 0.2; 72 0.1; 79 -0.6; 87 -1.2; 96 -1.7; 106 -2.0; 116 -2.2; 128 -2.7; 141 -2.9; 155 -3.0; 170 -2.7; 187 -2.9; 206 -2.8; 227 -2.7; 249 -2.6; 274 -2.4; 302 -2.2; 332 -1.9; 365 -1.6; 402 -1.2; 442 -1.0; 486 -0.8; 535 -0.8; 588 -0.6; 647 -0.4; 712 -0.5; 783 -0.6; 861 -0.7; 947 -0.2; 1042 -0.4; 1146 -0.8; 1261 -1.1; 1387 -1.3; 1526 -1.7; 1678 -2.0; 1846 -2.2; 2031 -2.2; 2234 -1.9; 2457 -1.8; 2703 -1.8; 2973 -1.7; 3270 -1.8; 3597 -1.0; 3957 0.3; 4353 -0.4; 4788 -0.8; 5267 2.6; 5793 2.2; 6373 -1.0; 7010 -0.9; 7711 -0.8; 8482 -2.3; 9330 -2.7; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -3.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 (balanced) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 (balanced) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.41 | 7.0 dB  |
| Peaking | 163 Hz   | 0.6  | -3.3 dB |
| Peaking | 1870 Hz  | 1.82 | -2.3 dB |
| Peaking | 3003 Hz  | 3.84 | -1.4 dB |
| Peaking | 8900 Hz  | 6.33 | -3.4 dB |
| Peaking | 5545 Hz  | 5.78 | 5.4 dB  |
| Peaking | 5901 Hz  | 2.14 | -1.9 dB |
| Peaking | 10334 Hz | 3.77 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20650%20(balanced)/Sennheiser%20HD%20650%20(balanced).png)