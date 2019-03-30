# Dunu Falcon-C
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.2; 25 -9.4; 28 -9.6; 31 -9.7; 34 -9.8; 37 -9.9; 41 -9.9; 45 -9.8; 49 -9.7; 54 -9.5; 60 -9.4; 66 -9.2; 72 -9.0; 79 -8.7; 87 -8.4; 96 -8.0; 106 -7.9; 116 -7.7; 128 -7.5; 141 -7.2; 155 -7.0; 170 -6.9; 187 -6.6; 206 -6.3; 227 -6.1; 249 -5.9; 274 -5.7; 302 -5.4; 332 -5.3; 365 -5.0; 402 -5.0; 442 -4.7; 486 -4.7; 535 -4.6; 588 -4.3; 647 -4.3; 712 -4.3; 783 -4.0; 861 -4.0; 947 -4.0; 1042 -3.8; 1146 -3.6; 1261 -3.4; 1387 -3.1; 1526 -2.6; 1678 -2.2; 1846 -1.8; 2031 -1.4; 2234 -1.0; 2457 -0.7; 2703 -0.5; 2973 -0.9; 3270 -1.5; 3597 -2.4; 3957 -3.6; 4353 -5.4; 4788 -7.5; 5267 -8.8; 5793 -9.9; 6373 -9.8; 7010 -7.3; 7711 -4.1; 8482 -4.3; 9330 -4.3; 10263 -4.3; 11289 -4.3; 12418 -4.3; 13660 -4.3; 15026 -4.3; 16529 -4.3; 18182 -4.3; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu Falcon-C GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Falcon-C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.24 | -5.3 dB |
| Peaking | 2800 Hz  | 0.94 | 4.8 dB  |
| Peaking | 6049 Hz  | 1.49 | -8.8 dB |
| Peaking | 7674 Hz  | 2.01 | 4.1 dB  |
| Peaking | 15 Hz    | 0.74 | 0.5 dB  |
| Peaking | 58 Hz    | 0.36 | -0.4 dB |
| Peaking | 92 Hz    | 1.41 | 0.6 dB  |
| Peaking | 6116 Hz  | 1.18 | -0.1 dB |
| Peaking | 11653 Hz | 1.35 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Dunu%20Falcon-C/Dunu%20Falcon-C.png)