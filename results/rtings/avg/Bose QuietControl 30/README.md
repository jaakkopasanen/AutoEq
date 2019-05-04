# Bose QuietControl 30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.4; 25 -5.5; 28 -5.5; 31 -5.4; 34 -5.2; 37 -5.0; 41 -4.6; 45 -4.3; 49 -4.1; 54 -3.9; 60 -3.8; 66 -3.9; 72 -4.0; 79 -4.1; 87 -4.3; 96 -4.5; 106 -4.6; 116 -4.7; 128 -4.8; 141 -4.7; 155 -4.6; 170 -4.4; 187 -4.1; 206 -3.9; 227 -3.7; 249 -3.5; 274 -3.4; 302 -3.3; 332 -3.3; 365 -3.3; 402 -3.1; 442 -2.6; 486 -2.0; 535 -1.3; 588 -0.9; 647 -0.7; 712 -0.5; 783 -0.5; 861 -0.8; 947 -1.6; 1042 -2.3; 1146 -2.5; 1261 -2.6; 1387 -2.6; 1526 -3.0; 1678 -4.0; 1846 -5.1; 2031 -5.5; 2234 -4.8; 2457 -3.6; 2703 -2.8; 2973 -2.6; 3270 -2.6; 3597 -2.9; 3957 -4.1; 4353 -6.4; 4788 -6.4; 5267 -5.4; 5793 -3.3; 6373 -2.0; 7010 -0.8; 7711 -2.4; 8482 -2.6; 9330 -2.7; 10263 -3.3; 11289 -2.7; 12418 -2.7; 13660 -2.7; 15026 -5.1; 16529 -4.5; 18182 -2.7; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietControl 30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietControl 30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 1.03 | -2.9 dB |
| Peaking | 135 Hz   | 0.68 | -1.9 dB |
| Peaking | 706 Hz   | 1.77 | 2.6 dB  |
| Peaking | 1981 Hz  | 3.76 | -3.2 dB |
| Peaking | 4650 Hz  | 4.64 | -4.5 dB |
| Peaking | 215 Hz   | 4.77 | 0.2 dB  |
| Peaking | 3242 Hz  | 3.28 | 0.8 dB  |
| Peaking | 5944 Hz  | 1.31 | -1.0 dB |
| Peaking | 6853 Hz  | 3.54 | 2.7 dB  |
| Peaking | 15751 Hz | 4.19 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietControl%2030/Bose%20QuietControl%2030.png)