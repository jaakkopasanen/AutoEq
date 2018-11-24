# Sennheiser RS 195

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -9.0; 23 -9.0; 25 -8.9; 28 -8.8; 31 -8.6; 34 -8.4; 37 -8.1; 41 -7.8; 45 -7.7; 49 -8.0; 54 -8.4; 60 -8.9; 66 -8.9; 72 -7.8; 79 -5.5; 87 -2.7; 96 -0.5; 106 0.9; 116 2.0; 128 2.6; 141 2.5; 155 2.0; 170 1.7; 187 1.5; 206 1.9; 227 2.6; 249 3.2; 274 3.3; 302 3.0; 332 2.6; 365 2.3; 402 1.9; 442 1.5; 486 1.0; 535 0.7; 588 0.6; 647 0.6; 712 0.7; 783 0.6; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.6; 1261 -1.5; 1387 -2.9; 1526 -4.1; 1678 -3.2; 1846 2.2; 2031 5.8; 2234 -2.4; 2457 -6.8; 2703 -7.7; 2973 -7.1; 3270 -5.1; 3597 -2.4; 3957 -1.7; 4353 -0.3; 4788 2.9; 5267 5.6; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.8; 10263 -2.9; 11289 -0.1; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 195 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 195 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 1.18 | -9.7 dB |
| Peaking | 62 Hz   | 2.98 | -8.3 dB |
| Peaking | 2574 Hz | 7.02 | -6.2 dB |
| Peaking | 3069 Hz | 3.67 | -6.6 dB |
| Peaking | 5725 Hz | 3.29 | 7.2 dB  |
| Peaking | 128 Hz  | 3.23 | 3.2 dB  |
| Peaking | 284 Hz  | 1.18 | 3.3 dB  |
| Peaking | 1586 Hz | 2.86 | -4.8 dB |
| Peaking | 1972 Hz | 7.79 | 9.7 dB  |
| Peaking | 9943 Hz | 5.69 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20RS%20195/Sennheiser%20RS%20195.png)