# Radius HP-NHR11
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 21 -12.3; 23 -12.3; 25 -12.2; 28 -12.0; 31 -11.9; 34 -11.8; 37 -11.6; 41 -11.5; 45 -11.3; 49 -11.2; 54 -11.0; 60 -10.9; 66 -10.8; 72 -10.7; 79 -10.6; 87 -10.5; 96 -10.4; 106 -10.1; 116 -9.8; 128 -9.5; 141 -9.2; 155 -8.8; 170 -8.3; 187 -7.8; 206 -7.3; 227 -6.6; 249 -6.1; 274 -5.4; 302 -4.7; 332 -4.1; 365 -3.5; 402 -2.8; 442 -2.1; 486 -1.6; 535 -1.0; 588 -0.3; 647 0.1; 712 0.3; 783 0.6; 861 0.5; 947 0.2; 1042 -0.2; 1146 -0.4; 1261 -1.0; 1387 -2.0; 1526 -3.0; 1678 -3.7; 1846 -4.1; 2031 -4.2; 2234 -4.2; 2457 -3.5; 2703 -2.8; 2973 -1.3; 3270 0.2; 3597 0.6; 3957 -0.7; 4353 -4.0; 4788 -6.8; 5267 -7.2; 5793 -3.4; 6373 0.2; 7010 2.2; 7711 0.3; 8482 0.0; 9330 -0.3; 10263 -1.9; 11289 -0.1; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Radius HP-NHR11 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-24**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-NHR11 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.18 | -12.0 dB |
| Peaking | 162 Hz   | 0.73 | -4.3 dB  |
| Peaking | 2004 Hz  | 2.23 | -4.6 dB  |
| Peaking | 5080 Hz  | 4.08 | -8.3 dB  |
| Peaking | 6783 Hz  | 5.19 | 3.3 dB   |
| Peaking | 781 Hz   | 1.92 | 1.6 dB   |
| Peaking | 1516 Hz  | 5.76 | -1.2 dB  |
| Peaking | 2624 Hz  | 5.66 | -1.3 dB  |
| Peaking | 3500 Hz  | 5.66 | 2.4 dB   |
| Peaking | 10215 Hz | 8.41 | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-NHR11/Radius%20HP-NHR11.png)