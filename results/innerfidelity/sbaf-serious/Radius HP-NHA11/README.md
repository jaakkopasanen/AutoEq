# Radius HP-NHA11
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 -13.1; 23 -13.0; 25 -12.8; 28 -12.6; 31 -12.4; 34 -12.3; 37 -12.1; 41 -11.9; 45 -11.7; 49 -11.5; 54 -11.3; 60 -11.1; 66 -10.9; 72 -10.8; 79 -10.6; 87 -10.5; 96 -10.3; 106 -10.0; 116 -9.7; 128 -9.4; 141 -9.0; 155 -8.6; 170 -8.1; 187 -7.6; 206 -7.1; 227 -6.4; 249 -5.8; 274 -5.2; 302 -4.6; 332 -3.9; 365 -3.3; 402 -2.8; 442 -2.1; 486 -1.5; 535 -1.1; 588 -0.4; 647 0.0; 712 0.3; 783 0.7; 861 0.5; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -1.1; 1387 -2.1; 1526 -3.2; 1678 -4.1; 1846 -4.6; 2031 -4.9; 2234 -5.0; 2457 -4.1; 2703 -3.6; 2973 -1.8; 3270 -0.3; 3597 0.1; 3957 -1.7; 4353 -5.7; 4788 -8.7; 5267 -5.7; 5793 -0.7; 6373 2.2; 7010 2.4; 7711 0.3; 8482 -0.5; 9330 -0.9; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Radius HP-NHA11 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-NHA11 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 0.18 | -12.7 dB |
| Peaking | 161 Hz  | 0.73 | -4.1 dB  |
| Peaking | 2038 Hz | 2.12 | -5.4 dB  |
| Peaking | 4845 Hz | 4.75 | -9.5 dB  |
| Peaking | 6558 Hz | 4.63 | 4.1 dB   |
| Peaking | 796 Hz  | 2.14 | 1.7 dB   |
| Peaking | 1541 Hz | 5.67 | -1.2 dB  |
| Peaking | 2676 Hz | 6.85 | -1.4 dB  |
| Peaking | 3483 Hz | 6.25 | 2.2 dB   |
| Peaking | 9059 Hz | 6.76 | -1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-NHA11/Radius%20HP-NHA11.png)