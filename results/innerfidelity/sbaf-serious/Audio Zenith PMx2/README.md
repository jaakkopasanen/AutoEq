# Audio Zenith PMx2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.8; 28 5.4; 31 5.1; 34 4.8; 37 4.6; 41 4.5; 45 4.6; 49 4.4; 54 3.8; 60 3.0; 66 2.6; 72 2.2; 79 1.8; 87 1.4; 96 0.8; 106 0.6; 116 0.3; 128 -0.1; 141 -0.4; 155 -0.7; 170 -0.7; 187 -1.0; 206 -1.1; 227 -1.0; 249 -1.1; 274 -1.1; 302 -1.1; 332 -0.5; 365 0.6; 402 0.8; 442 0.5; 486 0.1; 535 -0.2; 588 -0.1; 647 -0.3; 712 -0.4; 783 -0.3; 861 -0.1; 947 0.0; 1042 0.2; 1146 0.7; 1261 1.6; 1387 1.8; 1526 1.6; 1678 1.8; 1846 2.5; 2031 3.7; 2234 4.4; 2457 5.1; 2703 5.5; 2973 5.8; 3270 5.6; 3597 5.4; 3957 5.7; 4353 5.2; 4788 5.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.5; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Zenith PMx2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Zenith PMx2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.83 | 5.5 dB  |
| Peaking | 49 Hz   | 1.09 | 2.8 dB  |
| Peaking | 205 Hz  | 1.22 | -1.4 dB |
| Peaking | 2980 Hz | 1.11 | 5.7 dB  |
| Peaking | 5550 Hz | 2.65 | 5.0 dB  |
| Peaking | 395 Hz  | 5.96 | 1.3 dB  |
| Peaking | 754 Hz  | 2.6  | -0.7 dB |
| Peaking | 4437 Hz | 2.76 | 1.2 dB  |
| Peaking | 6544 Hz | 4.9  | 3.8 dB  |
| Peaking | 6861 Hz | 1.38 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Zenith%20PMx2/Audio%20Zenith%20PMx2.png)