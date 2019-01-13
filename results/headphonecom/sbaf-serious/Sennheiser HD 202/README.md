# Sennheiser HD 202
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.6; 31 4.8; 34 3.8; 37 3.0; 41 2.1; 45 1.2; 49 0.7; 54 0.3; 60 -0.3; 66 -1.0; 72 -1.0; 79 -1.5; 87 -1.7; 96 -1.8; 106 -1.8; 116 -1.6; 128 -1.5; 141 -1.2; 155 -0.8; 170 0.0; 187 1.4; 206 4.1; 227 5.1; 249 4.5; 274 4.3; 302 4.2; 332 3.7; 365 3.0; 402 2.9; 442 2.7; 486 2.1; 535 1.8; 588 1.3; 647 1.0; 712 0.7; 783 0.4; 861 0.3; 947 0.1; 1042 -0.0; 1146 -0.3; 1261 -0.1; 1387 -0.4; 1526 -0.7; 1678 -0.2; 1846 0.9; 2031 2.4; 2234 4.2; 2457 5.8; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 1.1; 4788 2.1; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 202 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 202 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.07 | 6.6 dB  |
| Peaking | 156 Hz  | 0.59 | -5.9 dB |
| Peaking | 242 Hz  | 0.96 | 9.3 dB  |
| Peaking | 3018 Hz | 1.82 | 6.7 dB  |
| Peaking | 5844 Hz | 3.68 | 5.9 dB  |
| Peaking | 2374 Hz | 2.57 | 6.1 dB  |
| Peaking | 2651 Hz | 1    | -5.5 dB |
| Peaking | 4215 Hz | 2.01 | 6.4 dB  |
| Peaking | 4490 Hz | 7.9  | -7.9 dB |
| Peaking | 8255 Hz | 3.5  | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20202/Sennheiser%20HD%20202.png)