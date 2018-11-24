# Cardas EM5813

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -8.5; 23 -8.5; 25 -8.5; 28 -8.6; 31 -8.6; 34 -8.6; 37 -8.5; 41 -8.6; 45 -8.7; 49 -8.9; 54 -9.1; 60 -9.2; 66 -9.4; 72 -9.7; 79 -9.8; 87 -10.0; 96 -10.2; 106 -10.2; 116 -10.3; 128 -10.3; 141 -10.3; 155 -10.3; 170 -10.1; 187 -9.9; 206 -9.6; 227 -9.3; 249 -8.8; 274 -8.4; 302 -7.8; 332 -7.1; 365 -6.5; 402 -5.9; 442 -5.3; 486 -4.7; 535 -4.0; 588 -3.4; 647 -2.8; 712 -2.3; 783 -2.1; 861 -1.3; 947 1.4; 1042 -0.4; 1146 -0.9; 1261 -1.3; 1387 -1.9; 1526 -2.7; 1678 -3.2; 1846 -3.6; 2031 -4.1; 2234 -5.1; 2457 -7.1; 2703 -5.6; 2973 -1.7; 3270 0.9; 3597 1.3; 3957 -1.6; 4353 -6.4; 4788 -4.1; 5267 2.8; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cardas EM5813 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cardas EM5813 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.24 | -7.8 dB |
| Peaking | 129 Hz  | 0.58 | -6.3 dB |
| Peaking | 290 Hz  | 0.76 | -4.5 dB |
| Peaking | 2353 Hz | 2.22 | -6.3 dB |
| Peaking | 6059 Hz | 5.49 | 7.3 dB  |
| Peaking | 951 Hz  | 6.37 | 3.4 dB  |
| Peaking | 1299 Hz | 0.53 | -0.6 dB |
| Peaking | 3480 Hz | 4.17 | 4.5 dB  |
| Peaking | 4490 Hz | 4.92 | -8.0 dB |
| Peaking | 5425 Hz | 7.93 | 4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Cardas%20EM5813/Cardas%20EM5813.png)