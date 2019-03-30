# Beyerdynamic DX 120
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -14.0; 25 -14.2; 28 -14.3; 31 -14.4; 34 -14.4; 37 -14.4; 41 -14.4; 45 -14.4; 49 -14.4; 54 -14.2; 60 -14.1; 66 -14.0; 72 -13.9; 79 -13.7; 87 -13.6; 96 -13.4; 106 -13.1; 116 -12.8; 128 -12.6; 141 -12.2; 155 -11.9; 170 -11.5; 187 -11.1; 206 -10.5; 227 -10.0; 249 -9.4; 274 -8.7; 302 -8.3; 332 -8.3; 365 -8.1; 402 -7.6; 442 -7.0; 486 -6.4; 535 -5.9; 588 -5.4; 647 -5.0; 712 -4.6; 783 -4.4; 861 -4.1; 947 -4.0; 1042 -4.3; 1146 -4.5; 1261 -4.8; 1387 -5.1; 1526 -5.6; 1678 -5.9; 1846 -6.1; 2031 -6.0; 2234 -5.6; 2457 -4.7; 2703 -3.6; 2973 -2.3; 3270 -1.2; 3597 -0.5; 3957 -0.5; 4353 -1.2; 4788 -2.1; 5267 -3.6; 5793 -6.8; 6373 -10.4; 7010 -10.5; 7711 -6.8; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DX 120 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DX 120 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.2  | -8.2 dB |
| Peaking | 798 Hz  | 1.21 | 2.7 dB  |
| Peaking | 3966 Hz | 1.57 | 6.5 dB  |
| Peaking | 6683 Hz | 3.66 | -6.7 dB |
| Peaking | 8017 Hz | 6.94 | 1.2 dB  |
| Peaking | 769 Hz  | 2.92 | -0.7 dB |
| Peaking | 1647 Hz | 0.61 | 1.3 dB  |
| Peaking | 1978 Hz | 1.37 | -2.4 dB |
| Peaking | 3026 Hz | 2.39 | 0.9 dB  |
| Peaking | 3998 Hz | 6.19 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DX%20120/Beyerdynamic%20DX%20120.png)