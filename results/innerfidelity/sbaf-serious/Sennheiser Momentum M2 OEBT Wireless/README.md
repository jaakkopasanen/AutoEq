# Sennheiser Momentum M2 OEBT Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.6; 23 -4.1; 25 -4.5; 28 -5.1; 31 -5.5; 34 -5.8; 37 -6.0; 41 -6.4; 45 -6.6; 49 -6.6; 54 -6.7; 60 -6.9; 66 -2.9; 72 -3.9; 79 -5.4; 87 -4.6; 96 -4.1; 106 -3.2; 116 -2.5; 128 -2.1; 141 -1.4; 155 -0.8; 170 -0.2; 187 0.2; 206 0.6; 227 1.1; 249 1.9; 274 2.8; 302 3.6; 332 4.2; 365 4.3; 402 4.3; 442 4.2; 486 3.8; 535 3.5; 588 3.4; 647 2.8; 712 2.1; 783 1.6; 861 0.9; 947 0.3; 1042 -0.2; 1146 -0.5; 1261 -0.8; 1387 -1.7; 1526 -2.7; 1678 -3.8; 1846 -4.2; 2031 -4.7; 2234 -4.8; 2457 -3.9; 2703 -2.8; 2973 -0.9; 3270 1.2; 3597 3.0; 3957 5.6; 4353 6.0; 4788 4.1; 5267 1.7; 5793 4.1; 6373 4.1; 7010 2.0; 7711 0.3; 8482 -1.1; 9330 -2.7; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum M2 OEBT Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum M2 OEBT Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.66 | -4.7 dB |
| Peaking | 78 Hz   | 0.47 | -2.7 dB |
| Peaking | 398 Hz  | 0.71 | 5.1 dB  |
| Peaking | 2228 Hz | 1.06 | -6.6 dB |
| Peaking | 4135 Hz | 1.59 | 7.7 dB  |
| Peaking | 68 Hz   | 8.4  | 6.0 dB  |
| Peaking | 68 Hz   | 2.91 | -2.5 dB |
| Peaking | 5201 Hz | 8.34 | -2.8 dB |
| Peaking | 6126 Hz | 4.58 | 3.2 dB  |
| Peaking | 9114 Hz | 5.01 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2%20OEBT%20Wireless/Sennheiser%20Momentum%20M2%20OEBT%20Wireless.png)