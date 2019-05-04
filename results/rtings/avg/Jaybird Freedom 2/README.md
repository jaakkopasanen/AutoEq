# Jaybird Freedom 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.6; 23 -13.8; 25 -13.9; 28 -14.1; 31 -14.3; 34 -14.4; 37 -14.5; 41 -14.5; 45 -14.6; 49 -14.6; 54 -14.7; 60 -14.6; 66 -14.6; 72 -14.6; 79 -14.5; 87 -14.4; 96 -14.3; 106 -14.0; 116 -13.7; 128 -13.3; 141 -12.9; 155 -12.7; 170 -12.6; 187 -12.0; 206 -11.2; 227 -10.4; 249 -9.7; 274 -8.9; 302 -8.2; 332 -7.4; 365 -6.6; 402 -5.8; 442 -5.0; 486 -4.2; 535 -3.4; 588 -2.6; 647 -1.7; 712 -0.9; 783 -0.5; 861 -0.7; 947 -1.2; 1042 -1.9; 1146 -2.9; 1261 -3.5; 1387 -3.8; 1526 -4.0; 1678 -4.1; 1846 -4.8; 2031 -5.8; 2234 -7.1; 2457 -7.9; 2703 -7.4; 2973 -5.0; 3270 -2.7; 3597 -1.5; 3957 -1.1; 4353 -1.4; 4788 -2.2; 5267 -3.0; 5793 -4.7; 6373 -9.4; 7010 -13.7; 7711 -10.7; 8482 -6.3; 9330 -6.2; 10263 -8.8; 11289 -13.0; 12418 -10.1; 13660 -6.3; 15026 -7.3; 16529 -8.3; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Freedom 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Freedom 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.38 | -5.6 dB |
| Peaking | 110 Hz   | 0.34 | -6.9 dB |
| Peaking | 819 Hz   | 0.63 | 7.6 dB  |
| Peaking | 4237 Hz  | 1.37 | 12.9 dB |
| Peaking | 4694 Hz  | 0.36 | -7.7 dB |
| Peaking | 2560 Hz  | 6.94 | -2.3 dB |
| Peaking | 7109 Hz  | 4.68 | -8.7 dB |
| Peaking | 9114 Hz  | 2.43 | 2.0 dB  |
| Peaking | 9227 Hz  | 0.83 | 4.1 dB  |
| Peaking | 11279 Hz | 3.55 | -8.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Freedom%202/Jaybird%20Freedom%202.png)