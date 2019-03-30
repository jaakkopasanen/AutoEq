# Roland RH-200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -2.6; 25 -3.6; 28 -5.0; 31 -6.0; 34 -6.9; 37 -7.6; 41 -8.3; 45 -8.9; 49 -9.3; 54 -9.5; 60 -9.5; 66 -9.7; 72 -10.0; 79 -10.0; 87 -10.0; 96 -10.1; 106 -10.3; 116 -10.3; 128 -10.1; 141 -9.9; 155 -9.7; 170 -9.3; 187 -8.9; 206 -8.2; 227 -7.4; 249 -6.2; 274 -4.8; 302 -3.1; 332 -1.5; 365 -0.9; 402 -1.4; 442 -2.6; 486 -3.8; 535 -4.8; 588 -5.5; 647 -6.0; 712 -6.1; 783 -6.2; 861 -6.4; 947 -6.5; 1042 -6.7; 1146 -7.0; 1261 -7.4; 1387 -7.8; 1526 -8.0; 1678 -8.3; 1846 -8.8; 2031 -9.3; 2234 -9.9; 2457 -10.3; 2703 -9.7; 2973 -8.7; 3270 -7.6; 3597 -7.4; 3957 -7.5; 4353 -6.1; 4788 -2.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.3; 7711 -7.9; 8482 -9.2; 9330 -9.6; 10263 -10.7; 11289 -11.7; 12418 -11.3; 13660 -9.5; 15026 -7.2; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Roland RH-200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Roland RH-200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.89 | 8.7 dB  |
| Peaking | 226 Hz   | 0.08 | -5.6 dB |
| Peaking | 412 Hz   | 0.72 | 10.0 dB |
| Peaking | 5742 Hz  | 2.41 | 8.9 dB  |
| Peaking | 10932 Hz | 1.16 | -5.4 dB |
| Peaking | 203 Hz   | 1.58 | -1.1 dB |
| Peaking | 352 Hz   | 2.58 | 2.7 dB  |
| Peaking | 548 Hz   | 1.36 | -2.8 dB |
| Peaking | 1035 Hz  | 0.82 | 2.1 dB  |
| Peaking | 2451 Hz  | 2.67 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Roland%20RH-200/Roland%20RH-200.png)