# Sennheiser MX 560

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.6; 106 5.0; 116 4.6; 128 4.2; 141 3.8; 155 3.7; 170 3.5; 187 3.2; 206 2.9; 227 3.0; 249 3.0; 274 2.8; 302 2.6; 332 2.4; 365 1.9; 402 1.6; 442 1.8; 486 2.8; 535 2.3; 588 2.0; 647 1.6; 712 1.3; 783 1.0; 861 0.7; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -1.1; 1387 -2.2; 1526 -3.7; 1678 -5.2; 1846 -7.2; 2031 -9.4; 2234 -11.4; 2457 -12.6; 2703 -12.0; 2973 -9.4; 3270 -5.5; 3597 -3.4; 3957 -3.2; 4353 -4.9; 4788 -6.0; 5267 -6.3; 5793 -6.5; 6373 -5.5; 7010 -4.0; 7711 -2.9; 8482 -4.9; 9330 -6.5; 10263 -4.0; 11289 -0.1; 12418 0.0; 13660 -0.4; 15026 -2.3; 16529 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MX 560 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MX 560 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.23 | 6.3 dB   |
| Peaking | 581 Hz   | 0.85 | 1.8 dB   |
| Peaking | 2386 Hz  | 1.86 | -12.6 dB |
| Peaking | 6771 Hz  | 0.88 | -4.8 dB  |
| Peaking | 24000 Hz | 2.17 | -3.9 dB  |
| Peaking | 3761 Hz  | 3.74 | 4.5 dB   |
| Peaking | 4577 Hz  | 1.02 | -2.3 dB  |
| Peaking | 7606 Hz  | 3.13 | 4.2 dB   |
| Peaking | 9412 Hz  | 2.84 | -4.6 dB  |
| Peaking | 11387 Hz | 3.23 | 3.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20MX%20560/Sennheiser%20MX%20560.png)