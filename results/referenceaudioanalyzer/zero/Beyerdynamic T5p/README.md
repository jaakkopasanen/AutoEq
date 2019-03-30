# Beyerdynamic T5p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.2; 25 -3.6; 28 -4.1; 31 -4.5; 34 -4.7; 37 -4.7; 41 -4.6; 45 -4.3; 49 -3.8; 54 -3.2; 60 -3.0; 66 -3.4; 72 -4.2; 79 -5.2; 87 -5.9; 96 -6.3; 106 -6.6; 116 -6.5; 128 -6.2; 141 -5.6; 155 -5.0; 170 -4.5; 187 -3.9; 206 -3.3; 227 -2.5; 249 -1.8; 274 -1.3; 302 -1.0; 332 -0.8; 365 -0.8; 402 -0.8; 442 -0.9; 486 -1.3; 535 -1.8; 588 -1.5; 647 -0.7; 712 -0.9; 783 -1.8; 861 -2.1; 947 -2.1; 1042 -2.1; 1146 -3.2; 1261 -4.7; 1387 -5.5; 1526 -5.4; 1678 -5.2; 1846 -4.8; 2031 -3.9; 2234 -2.8; 2457 -2.1; 2703 -2.1; 2973 -2.8; 3270 -4.0; 3597 -4.0; 3957 -2.9; 4353 -1.7; 4788 -0.5; 5267 -1.3; 5793 -4.5; 6373 -5.4; 7010 -6.9; 7711 -10.7; 8482 -12.6; 9330 -11.6; 10263 -9.8; 11289 -8.8; 12418 -8.1; 13660 -6.9; 15026 -4.2; 16529 -3.7; 18182 -3.7; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T5p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 115 Hz   | 1.52 | -3.3 dB |
| Peaking | 341 Hz   | 1.23 | 3.2 dB  |
| Peaking | 692 Hz   | 2.75 | 2.3 dB  |
| Peaking | 5002 Hz  | 2.29 | 5.3 dB  |
| Peaking | 8922 Hz  | 1.19 | -8.9 dB |
| Peaking | 61 Hz    | 5.44 | 1.5 dB  |
| Peaking | 1052 Hz  | 2.77 | 2.6 dB  |
| Peaking | 1398 Hz  | 1.41 | -2.8 dB |
| Peaking | 2486 Hz  | 3.66 | 2.5 dB  |
| Peaking | 13010 Hz | 5.99 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | 2.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20T5p/Beyerdynamic%20T5p.png)