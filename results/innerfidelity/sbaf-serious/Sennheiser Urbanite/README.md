# Sennheiser Urbanite
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.8; 23 -0.9; 25 -1.0; 28 -1.1; 31 -1.1; 34 -1.1; 37 -1.1; 41 -1.1; 45 -1.1; 49 -1.1; 54 -1.2; 60 -1.3; 66 -1.4; 72 -1.4; 79 -1.6; 87 -1.8; 96 -1.9; 106 -1.8; 116 -1.7; 128 -1.6; 141 -1.7; 155 -2.0; 170 -1.4; 187 -1.7; 206 -1.6; 227 -1.1; 249 -0.8; 274 -0.4; 302 0.0; 332 0.4; 365 0.6; 402 0.7; 442 0.9; 486 0.9; 535 0.9; 588 1.0; 647 0.7; 712 0.3; 783 0.4; 861 0.2; 947 0.1; 1042 0.0; 1146 0.1; 1261 0.3; 1387 0.2; 1526 -0.2; 1678 -0.1; 1846 1.1; 2031 2.9; 2234 4.8; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Urbanite GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Urbanite ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 46 Hz   | 0.27 | -0.9 dB |
| Peaking | 203 Hz  | 3.81 | -0.4 dB |
| Peaking | 471 Hz  | 0.55 | 5.7 dB  |
| Peaking | 563 Hz  | 0.25 | -4.9 dB |
| Peaking | 3430 Hz | 0.76 | 8.1 dB  |
| Peaking | 1707 Hz | 4.58 | -1.7 dB |
| Peaking | 2381 Hz | 3.6  | 2.0 dB  |
| Peaking | 3497 Hz | 2.54 | -1.3 dB |
| Peaking | 6219 Hz | 2.23 | 5.4 dB  |
| Peaking | 7469 Hz | 1.5  | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Urbanite/Sennheiser%20Urbanite.png)