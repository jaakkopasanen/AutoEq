# Sennheiser CX 870
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -10.1; 25 -10.7; 28 -11.5; 31 -12.1; 34 -12.6; 37 -12.9; 41 -13.2; 45 -13.5; 49 -13.7; 54 -13.8; 60 -13.8; 66 -13.8; 72 -13.8; 79 -13.8; 87 -13.6; 96 -13.4; 106 -13.2; 116 -12.9; 128 -12.5; 141 -12.2; 155 -11.8; 170 -11.3; 187 -10.9; 206 -10.4; 227 -9.9; 249 -9.5; 274 -9.0; 302 -8.4; 332 -7.7; 365 -7.1; 402 -6.4; 442 -5.7; 486 -5.1; 535 -4.5; 588 -3.9; 647 -3.2; 712 -2.7; 783 -2.2; 861 -1.7; 947 -1.4; 1042 -1.1; 1146 -0.9; 1261 -0.8; 1387 -0.5; 1526 -0.6; 1678 -1.0; 1846 -1.5; 2031 -2.0; 2234 -2.5; 2457 -2.9; 2703 -3.1; 2973 -3.4; 3270 -3.7; 3597 -3.3; 3957 -3.1; 4353 -3.4; 4788 -4.4; 5267 -6.3; 5793 -8.1; 6373 -8.6; 7010 -7.0; 7711 -5.4; 8482 -5.6; 9330 -7.4; 10263 -8.9; 11289 -6.0; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 870 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 870 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 70 Hz    | 0.28 | -8.3 dB |
| Peaking | 1215 Hz  | 0.55 | 5.4 dB  |
| Peaking | 4480 Hz  | 1.99 | 5.3 dB  |
| Peaking | 5428 Hz  | 1.33 | -5.5 dB |
| Peaking | 16 Hz    | 2.2  | 1.4 dB  |
| Peaking | 7935 Hz  | 4.94 | 1.9 dB  |
| Peaking | 10146 Hz | 6.2  | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20CX%20870/Sennheiser%20CX%20870.png)