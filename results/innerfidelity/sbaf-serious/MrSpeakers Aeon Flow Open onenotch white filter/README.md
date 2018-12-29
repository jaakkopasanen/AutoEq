# MrSpeakers Aeon Flow Open onenotch white filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 0.0; 23 0.8; 25 0.7; 28 0.6; 31 0.5; 34 0.4; 37 0.3; 41 0.2; 45 -0.0; 49 -0.2; 54 -0.4; 60 -0.5; 66 -0.9; 72 -1.6; 79 -2.9; 87 -3.6; 96 -4.2; 106 -4.7; 116 -5.1; 128 -5.3; 141 -5.4; 155 -4.8; 170 -5.2; 187 -5.5; 206 -5.3; 227 -5.1; 249 -4.9; 274 -4.6; 302 -4.3; 332 -4.1; 365 -3.8; 402 -3.4; 442 -2.9; 486 -2.7; 535 -1.9; 588 -1.5; 647 -1.3; 712 -1.2; 783 -0.9; 861 -0.2; 947 -0.2; 1042 0.1; 1146 1.0; 1261 2.4; 1387 0.5; 1526 -1.1; 1678 -1.9; 1846 -1.4; 2031 -0.6; 2234 0.4; 2457 2.6; 2703 4.2; 2973 3.1; 3270 4.8; 3597 3.4; 3957 2.0; 4353 2.0; 4788 2.2; 5267 3.7; 5793 5.2; 6373 5.2; 7010 2.5; 7711 0.3; 8482 -2.8; 9330 -3.7; 10263 -0.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Aeon Flow Open onenotch white filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Aeon Flow Open onenotch white filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 195 Hz  | 0.51 | -5.6 dB |
| Peaking | 1887 Hz | 1.95 | -7.8 dB |
| Peaking | 2255 Hz | 0.81 | 6.7 dB  |
| Peaking | 6160 Hz | 3.62 | 5.0 dB  |
| Peaking | 8963 Hz | 4.28 | -5.0 dB |
| Peaking | 54 Hz   | 0.41 | 1.5 dB  |
| Peaking | 102 Hz  | 1.67 | -2.1 dB |
| Peaking | 3394 Hz | 6.31 | 2.4 dB  |
| Peaking | 3883 Hz | 2.41 | -1.4 dB |
| Peaking | 5353 Hz | 5.79 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Aeon%20Flow%20Open%20onenotch%20white%20filter/MrSpeakers%20Aeon%20Flow%20Open%20onenotch%20white%20filter.png)