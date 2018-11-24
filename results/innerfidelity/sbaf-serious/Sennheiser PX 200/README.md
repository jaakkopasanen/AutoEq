# Sennheiser PX 200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 5.6; 128 4.9; 141 4.8; 155 5.3; 170 4.8; 187 5.5; 206 5.5; 227 4.8; 249 4.0; 274 3.3; 302 2.9; 332 2.7; 365 2.7; 402 2.6; 442 2.3; 486 0.8; 535 -0.3; 588 -0.6; 647 -1.0; 712 -0.7; 783 -0.5; 861 -0.2; 947 -0.0; 1042 0.0; 1146 0.1; 1261 0.0; 1387 -0.5; 1526 -1.1; 1678 -1.6; 1846 -1.7; 2031 -1.0; 2234 -0.0; 2457 1.0; 2703 2.5; 2973 4.7; 3270 6.0; 3597 4.5; 3957 1.8; 4353 2.0; 4788 3.5; 5267 5.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.19 | 6.1 dB  |
| Peaking | 241 Hz  | 0.73 | 2.8 dB  |
| Peaking | 1409 Hz | 0.12 | -1.4 dB |
| Peaking | 3205 Hz | 3.29 | 7.0 dB  |
| Peaking | 5753 Hz | 2.56 | 7.4 dB  |
| Peaking | 431 Hz  | 3.39 | 2.2 dB  |
| Peaking | 580 Hz  | 1    | -2.9 dB |
| Peaking | 1000 Hz | 0.59 | 2.2 dB  |
| Peaking | 1768 Hz | 2.58 | -2.2 dB |
| Peaking | 4044 Hz | 8.7  | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20200/Sennheiser%20PX%20200.png)