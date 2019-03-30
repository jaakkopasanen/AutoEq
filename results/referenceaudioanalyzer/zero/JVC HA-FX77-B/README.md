# JVC HA-FX77-B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.4; 25 -2.0; 28 -2.8; 31 -3.4; 34 -3.8; 37 -4.2; 41 -4.5; 45 -4.8; 49 -5.1; 54 -5.4; 60 -5.6; 66 -5.8; 72 -5.9; 79 -5.9; 87 -6.0; 96 -6.1; 106 -6.4; 116 -6.4; 128 -6.4; 141 -6.4; 155 -6.1; 170 -5.9; 187 -5.5; 206 -5.4; 227 -5.6; 249 -5.8; 274 -5.7; 302 -5.5; 332 -5.1; 365 -5.2; 402 -5.4; 442 -5.2; 486 -5.1; 535 -4.8; 588 -4.6; 647 -4.4; 712 -4.1; 783 -4.1; 861 -4.0; 947 -3.8; 1042 -3.8; 1146 -3.8; 1261 -3.8; 1387 -3.9; 1526 -4.5; 1678 -5.4; 1846 -6.5; 2031 -7.6; 2234 -8.6; 2457 -9.9; 2703 -11.2; 2973 -12.3; 3270 -13.2; 3597 -13.8; 3957 -13.9; 4353 -13.4; 4788 -12.1; 5267 -10.3; 5793 -7.9; 6373 -5.6; 7010 -4.6; 7711 -6.4; 8482 -6.7; 9330 -7.8; 10263 -6.8; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-FX77-B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-FX77-B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.73 | 7.6 dB  |
| Peaking | 613 Hz   | 0.4  | 1.5 dB  |
| Peaking | 1335 Hz  | 0.96 | 3.2 dB  |
| Peaking | 3759 Hz  | 0.9  | -8.5 dB |
| Peaking | 6643 Hz  | 2.57 | 5.3 dB  |
| Peaking | 126 Hz   | 1.92 | -0.4 dB |
| Peaking | 198 Hz   | 5.14 | 0.6 dB  |
| Peaking | 420 Hz   | 7.28 | -0.4 dB |
| Peaking | 11947 Hz | 2.79 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | -8.1 dB |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JVC%20HA-FX77-B/JVC%20HA-FX77-B.png)