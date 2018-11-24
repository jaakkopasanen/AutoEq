# Sennheiser RS 175

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 21 -9.7; 23 -9.7; 25 -9.6; 28 -9.4; 31 -9.0; 34 -8.5; 37 -8.1; 41 -7.5; 45 -6.9; 49 -6.3; 54 -5.8; 60 -5.5; 66 -5.6; 72 -5.8; 79 -6.1; 87 -6.4; 96 -6.5; 106 -6.4; 116 -6.1; 128 -5.4; 141 -4.4; 155 -3.2; 170 -1.8; 187 -0.2; 206 1.3; 227 2.4; 249 3.0; 274 3.0; 302 2.6; 332 2.3; 365 2.8; 402 4.0; 442 4.6; 486 4.1; 535 3.5; 588 2.8; 647 2.2; 712 1.6; 783 1.0; 861 0.6; 947 0.2; 1042 -0.0; 1146 -0.3; 1261 -0.7; 1387 -0.7; 1526 -0.2; 1678 0.3; 1846 1.0; 2031 -0.3; 2234 -3.7; 2457 -6.3; 2703 -7.2; 2973 -6.7; 3270 -4.7; 3597 -1.9; 3957 -1.0; 4353 -1.0; 4788 0.3; 5267 1.4; 5793 0.5; 6373 3.9; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 175 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 175 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.5  | -8.8 dB |
| Peaking | 30 Hz   | 0.72 | -5.1 dB |
| Peaking | 113 Hz  | 0.98 | -6.9 dB |
| Peaking | 306 Hz  | 0.61 | 4.8 dB  |
| Peaking | 2748 Hz | 3.13 | -8.3 dB |
| Peaking | 340 Hz  | 3.02 | -3.8 dB |
| Peaking | 401 Hz  | 1.31 | 2.8 dB  |
| Peaking | 1249 Hz | 0.67 | -1.3 dB |
| Peaking | 1836 Hz | 4.84 | 3.0 dB  |
| Peaking | 6515 Hz | 5.66 | 4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20RS%20175/Sennheiser%20RS%20175.png)