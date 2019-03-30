# MB Quart QP 400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -2.1; 25 -3.2; 28 -4.5; 31 -5.5; 34 -6.3; 37 -7.0; 41 -7.6; 45 -8.1; 49 -8.5; 54 -8.9; 60 -9.2; 66 -9.5; 72 -9.6; 79 -9.7; 87 -9.9; 96 -10.0; 106 -10.0; 116 -10.0; 128 -9.9; 141 -9.6; 155 -9.6; 170 -9.5; 187 -9.3; 206 -9.3; 227 -9.0; 249 -8.9; 274 -8.6; 302 -8.4; 332 -8.1; 365 -8.0; 402 -7.8; 442 -7.4; 486 -7.0; 535 -6.7; 588 -6.4; 647 -6.1; 712 -5.7; 783 -5.4; 861 -4.9; 947 -4.2; 1042 -3.4; 1146 -2.9; 1261 -3.1; 1387 -2.5; 1526 -0.6; 1678 -0.5; 1846 -1.9; 2031 -3.9; 2234 -5.4; 2457 -6.3; 2703 -6.5; 2973 -6.3; 3270 -5.6; 3597 -4.1; 3957 -1.9; 4353 -0.5; 4788 -1.2; 5267 -3.0; 5793 -5.7; 6373 -9.1; 7010 -11.6; 7711 -13.1; 8482 -12.8; 9330 -10.5; 10263 -8.2; 11289 -8.2; 12418 -9.1; 13660 -7.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MB Quart QP 400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MB Quart QP 400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.31 | 7.0 dB  |
| Peaking | 103 Hz   | 0.38 | -3.7 dB |
| Peaking | 1480 Hz  | 1.63 | 5.7 dB  |
| Peaking | 4644 Hz  | 2.63 | 7.6 dB  |
| Peaking | 7835 Hz  | 1.69 | -7.5 dB |
| Peaking | 1350 Hz  | 5.21 | -2.7 dB |
| Peaking | 1726 Hz  | 6.33 | 0.9 dB  |
| Peaking | 1930 Hz  | 0.61 | 1.8 dB  |
| Peaking | 2496 Hz  | 1.93 | -3.3 dB |
| Peaking | 12926 Hz | 6.37 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/MB%20Quart%20QP%20400/MB%20Quart%20QP%20400.png)