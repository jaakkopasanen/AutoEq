# TDK BA200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.1; 25 0.1; 28 0.0; 31 -0.1; 34 -0.2; 37 -0.3; 41 -0.4; 45 -0.5; 49 -0.7; 54 -0.9; 60 -1.2; 66 -1.5; 72 -1.8; 79 -2.2; 87 -2.6; 96 -3.1; 106 -3.3; 116 -3.4; 128 -3.8; 141 -3.9; 155 -4.1; 170 -4.1; 187 -4.2; 206 -4.2; 227 -4.0; 249 -3.9; 274 -3.7; 302 -3.4; 332 -3.2; 365 -3.0; 402 -2.6; 442 -2.0; 486 -1.7; 535 -1.3; 588 -0.6; 647 -0.3; 712 -0.0; 783 0.4; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.4; 1526 -2.0; 1678 -2.6; 1846 -2.7; 2031 -2.3; 2234 -1.6; 2457 -0.1; 2703 1.5; 2973 3.7; 3270 5.7; 3597 6.0; 3957 5.6; 4353 3.1; 4788 3.6; 5267 5.6; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.4; 9330 -4.4; 10263 -1.0; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TDK BA200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TDK BA200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 180 Hz  | 0.6  | -4.4 dB |
| Peaking | 1914 Hz | 2.2  | -3.6 dB |
| Peaking | 3464 Hz | 2.46 | 6.3 dB  |
| Peaking | 5902 Hz | 2.62 | 6.1 dB  |
| Peaking | 9112 Hz | 4.4  | -5.6 dB |
| Peaking | 21 Hz   | 1.01 | 0.3 dB  |
| Peaking | 383 Hz  | 2.26 | -0.7 dB |
| Peaking | 794 Hz  | 1.73 | 1.1 dB  |
| Peaking | 1492 Hz | 4.91 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/TDK%20BA200/TDK%20BA200.png)