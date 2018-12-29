# Sennheiser PX 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 5.8; 365 5.5; 402 4.9; 442 4.7; 486 3.8; 535 3.0; 588 2.4; 647 1.3; 712 0.7; 783 -0.0; 861 -0.1; 947 -0.1; 1042 0.0; 1146 0.3; 1261 0.2; 1387 -0.1; 1526 -0.7; 1678 -1.0; 1846 -1.2; 2031 -1.0; 2234 0.4; 2457 1.2; 2703 1.9; 2973 3.5; 3270 4.9; 3597 5.7; 3957 6.0; 4353 4.3; 4788 4.2; 5267 5.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.11 | 6.0 dB  |
| Peaking | 354 Hz  | 0.81 | 3.7 dB  |
| Peaking | 1789 Hz | 0.18 | -2.0 dB |
| Peaking | 3612 Hz | 1.74 | 7.1 dB  |
| Peaking | 5867 Hz | 2.75 | 6.4 dB  |
| Peaking | 797 Hz  | 3.95 | -0.8 dB |
| Peaking | 1244 Hz | 2.57 | 1.1 dB  |
| Peaking | 2001 Hz | 2.53 | -1.5 dB |
| Peaking | 2312 Hz | 3.51 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20200/Sennheiser%20PX%20200.png)