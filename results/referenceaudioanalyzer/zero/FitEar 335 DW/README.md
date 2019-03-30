# FitEar 335 DW
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.9; 25 -11.0; 28 -11.2; 31 -11.3; 34 -11.4; 37 -11.5; 41 -11.6; 45 -11.7; 49 -11.7; 54 -11.6; 60 -11.5; 66 -11.3; 72 -11.3; 79 -11.3; 87 -11.1; 96 -11.0; 106 -10.8; 116 -10.7; 128 -10.4; 141 -10.2; 155 -10.0; 170 -9.7; 187 -9.4; 206 -9.1; 227 -8.8; 249 -8.5; 274 -8.1; 302 -7.7; 332 -7.2; 365 -6.8; 402 -6.3; 442 -5.8; 486 -5.3; 535 -4.9; 588 -4.3; 647 -3.8; 712 -3.4; 783 -2.9; 861 -2.5; 947 -2.1; 1042 -1.9; 1146 -1.9; 1261 -2.1; 1387 -2.6; 1526 -3.3; 1678 -3.8; 1846 -3.6; 2031 -3.0; 2234 -2.9; 2457 -2.9; 2703 -2.3; 2973 -1.7; 3270 -1.8; 3597 -1.9; 3957 -1.8; 4353 -0.6; 4788 -0.5; 5267 -3.7; 5793 -5.5; 6373 -4.0; 7010 -2.3; 7711 -4.5; 8482 -4.8; 9330 -7.6; 10263 -8.8; 11289 -6.3; 12418 -4.8; 13660 -4.8; 15026 -4.8; 16529 -4.8; 18182 -4.8; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar 335 DW GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar 335 DW ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.44 | -4.0 dB |
| Peaking | 98 Hz    | 0.31 | -5.3 dB |
| Peaking | 955 Hz   | 1.01 | 3.2 dB  |
| Peaking | 3893 Hz  | 1.2  | 3.5 dB  |
| Peaking | 10088 Hz | 4.32 | -4.9 dB |
| Peaking | 1702 Hz  | 3.92 | -1.7 dB |
| Peaking | 1755 Hz  | 1.67 | 1.0 dB  |
| Peaking | 4744 Hz  | 6.61 | 3.2 dB  |
| Peaking | 5831 Hz  | 2.54 | -3.3 dB |
| Peaking | 6774 Hz  | 6.3  | 4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/FitEar%20335%20DW/FitEar%20335%20DW.png)