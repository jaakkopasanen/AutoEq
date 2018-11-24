# Sennheiser PX 100-IIi

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.8; 41 5.1; 45 4.4; 49 3.7; 54 2.8; 60 2.0; 66 1.3; 72 0.6; 79 0.0; 87 -0.7; 96 -1.3; 106 -1.6; 116 -1.7; 128 -2.1; 141 -2.4; 155 -2.6; 170 -2.8; 187 -2.8; 206 -2.8; 227 -2.5; 249 -2.4; 274 -2.3; 302 -2.0; 332 -1.7; 365 -1.5; 402 -1.2; 442 -0.7; 486 -0.7; 535 -0.4; 588 -0.1; 647 0.0; 712 0.2; 783 0.4; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.6; 1387 -1.4; 1526 -2.4; 1678 -3.1; 1846 -3.3; 2031 -2.3; 2234 -0.1; 2457 2.7; 2703 4.0; 2973 4.8; 3270 3.4; 3597 2.4; 3957 3.8; 4353 -0.9; 4788 -0.0; 5267 4.2; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 100-IIi GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 100-IIi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.66 | 6.7 dB  |
| Peaking | 157 Hz  | 0.63 | -3.3 dB |
| Peaking | 1830 Hz | 2.65 | -4.5 dB |
| Peaking | 2854 Hz | 2.46 | 5.5 dB  |
| Peaking | 5989 Hz | 4.31 | 6.6 dB  |
| Peaking | 776 Hz  | 2.4  | 0.8 dB  |
| Peaking | 3940 Hz | 9.29 | 3.7 dB  |
| Peaking | 4535 Hz | 4.84 | -4.1 dB |
| Peaking | 5230 Hz | 6.51 | 2.5 dB  |
| Peaking | 8271 Hz | 4.96 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20100-IIi/Sennheiser%20PX%20100-IIi.png)