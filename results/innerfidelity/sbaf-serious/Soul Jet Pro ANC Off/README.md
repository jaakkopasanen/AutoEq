# Soul Jet Pro ANC Off
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.4; 25 3.9; 28 3.2; 31 2.6; 34 2.0; 37 1.4; 41 0.8; 45 0.2; 49 -0.3; 54 -1.0; 60 -1.7; 66 -2.3; 72 -2.9; 79 -3.4; 87 -3.8; 96 -4.0; 106 -4.0; 116 -4.5; 128 -6.0; 141 -7.3; 155 -8.1; 170 -8.0; 187 -9.5; 206 -10.2; 227 -10.8; 249 -10.9; 274 -10.3; 302 -9.2; 332 -7.3; 365 -4.9; 402 -3.1; 442 -0.7; 486 1.6; 535 4.7; 588 6.0; 647 4.8; 712 1.2; 783 2.5; 861 0.8; 947 -0.2; 1042 0.3; 1146 0.5; 1261 1.1; 1387 1.2; 1526 0.8; 1678 0.7; 1846 0.1; 2031 -1.4; 2234 -2.5; 2457 -2.5; 2703 -2.3; 2973 -1.1; 3270 -0.7; 3597 -2.5; 3957 -4.9; 4353 -8.6; 4788 -7.0; 5267 -4.8; 5793 -2.6; 6373 -1.0; 7010 2.4; 7711 0.3; 8482 -0.6; 9330 -2.7; 10263 -1.4; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.0; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul Jet Pro ANC Off GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul Jet Pro ANC Off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 1.25 | 5.1 dB   |
| Peaking | 247 Hz   | 0.67 | -12.1 dB |
| Peaking | 562 Hz   | 1.57 | 10.4 dB  |
| Peaking | 2370 Hz  | 5.43 | -2.6 dB  |
| Peaking | 4491 Hz  | 3.51 | -8.9 dB  |
| Peaking | 74 Hz    | 3.72 | -0.9 dB  |
| Peaking | 1430 Hz  | 3.69 | 1.5 dB   |
| Peaking | 6946 Hz  | 9.91 | 3.8 dB   |
| Peaking | 9469 Hz  | 6.64 | -2.8 dB  |
| Peaking | 20058 Hz | 3.41 | -5.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20Jet%20Pro%20ANC%20Off/Soul%20Jet%20Pro%20ANC%20Off.png)