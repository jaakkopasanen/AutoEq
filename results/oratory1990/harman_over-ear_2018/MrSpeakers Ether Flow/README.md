# MrSpeakers Ether Flow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.5; 25 2.6; 28 2.9; 31 3.1; 34 3.4; 37 4.0; 41 4.0; 45 1.8; 49 0.2; 54 1.6; 60 0.9; 66 -1.6; 72 -2.1; 79 -1.9; 87 -2.2; 96 -2.9; 106 -3.2; 116 -3.3; 128 -3.5; 141 -3.8; 155 -4.0; 170 -4.2; 187 -4.2; 206 -4.2; 227 -4.0; 249 -3.7; 274 -3.1; 302 -2.4; 332 -2.0; 365 -1.0; 402 -0.0; 442 1.2; 486 2.3; 535 1.7; 588 0.8; 647 1.0; 712 0.8; 783 0.0; 861 -0.0; 947 0.2; 1042 0.5; 1146 2.2; 1261 2.1; 1387 1.8; 1526 1.9; 1678 1.2; 1846 1.4; 2031 0.8; 2234 1.3; 2457 0.8; 2703 1.1; 2973 1.5; 3270 3.1; 3597 5.4; 3957 6.0; 4353 6.0; 4788 6.0; 5267 4.4; 5793 0.0; 6373 -2.8; 7010 -3.1; 7711 -2.0; 8482 0.0; 9330 0.0; 10263 -2.1; 11289 -1.0; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether Flow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether Flow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 1.21 | 4.5 dB  |
| Peaking | 243 Hz   | 0.45 | -7.1 dB |
| Peaking | 444 Hz   | 0.64 | 5.8 dB  |
| Peaking | 4662 Hz  | 1.52 | 8.6 dB  |
| Peaking | 6479 Hz  | 2.12 | -7.0 dB |
| Peaking | 488 Hz   | 7.15 | 1.7 dB  |
| Peaking | 986 Hz   | 1.62 | -3.2 dB |
| Peaking | 1165 Hz  | 1.76 | 3.7 dB  |
| Peaking | 2692 Hz  | 4.92 | -1.1 dB |
| Peaking | 10692 Hz | 9.13 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/MrSpeakers%20Ether%20Flow/MrSpeakers%20Ether%20Flow.png)