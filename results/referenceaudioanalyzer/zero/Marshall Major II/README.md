# Marshall Major II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.4; 25 -5.8; 28 -6.3; 31 -6.7; 34 -7.1; 37 -7.3; 41 -7.6; 45 -7.7; 49 -7.8; 54 -7.9; 60 -8.3; 66 -8.4; 72 -7.9; 79 -7.2; 87 -7.5; 96 -8.4; 106 -9.0; 116 -9.1; 128 -8.8; 141 -8.2; 155 -7.5; 170 -6.6; 187 -5.5; 206 -4.3; 227 -3.4; 249 -3.6; 274 -4.7; 302 -5.5; 332 -5.9; 365 -6.4; 402 -6.9; 442 -7.4; 486 -7.8; 535 -8.3; 588 -8.7; 647 -9.1; 712 -9.1; 783 -9.1; 861 -8.8; 947 -8.5; 1042 -8.4; 1146 -8.5; 1261 -8.4; 1387 -7.9; 1526 -6.9; 1678 -5.7; 1846 -4.6; 2031 -3.6; 2234 -2.7; 2457 -1.9; 2703 -1.3; 2973 -0.8; 3270 -0.5; 3597 -0.7; 3957 -1.4; 4353 -2.9; 4788 -4.7; 5267 -6.1; 5793 -7.3; 6373 -9.1; 7010 -9.3; 7711 -6.4; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marshall Major II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marshall Major II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 82 Hz   | 0.9  | -2.9 dB |
| Peaking | 666 Hz  | 1.88 | -3.3 dB |
| Peaking | 1239 Hz | 1.48 | -3.4 dB |
| Peaking | 3129 Hz | 1.01 | 5.8 dB  |
| Peaking | 6422 Hz | 2.56 | -5.2 dB |
| Peaking | 14 Hz   | 0.81 | 2.1 dB  |
| Peaking | 33 Hz   | 1.47 | -1.0 dB |
| Peaking | 81 Hz   | 2.94 | 3.1 dB  |
| Peaking | 147 Hz  | 0.52 | -2.6 dB |
| Peaking | 227 Hz  | 1.82 | 5.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | 3.1 dB  |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -4.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Marshall%20Major%20II/Marshall%20Major%20II.png)