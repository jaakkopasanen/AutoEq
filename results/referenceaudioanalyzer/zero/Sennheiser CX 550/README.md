# Sennheiser CX 550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.4; 25 -10.6; 28 -10.9; 31 -11.1; 34 -11.3; 37 -11.4; 41 -11.6; 45 -11.7; 49 -11.8; 54 -11.9; 60 -11.9; 66 -12.0; 72 -12.0; 79 -12.0; 87 -12.0; 96 -12.0; 106 -11.9; 116 -11.9; 128 -11.8; 141 -11.6; 155 -11.4; 170 -11.2; 187 -11.0; 206 -10.8; 227 -10.5; 249 -10.1; 274 -9.8; 302 -9.6; 332 -9.6; 365 -9.2; 402 -8.7; 442 -8.2; 486 -7.8; 535 -7.4; 588 -6.8; 647 -6.2; 712 -5.6; 783 -4.9; 861 -4.3; 947 -3.7; 1042 -3.1; 1146 -2.6; 1261 -2.0; 1387 -1.5; 1526 -1.0; 1678 -0.7; 1846 -0.5; 2031 -0.7; 2234 -1.0; 2457 -1.3; 2703 -1.7; 2973 -2.1; 3270 -2.3; 3597 -2.6; 3957 -3.0; 4353 -3.5; 4788 -3.8; 5267 -4.1; 5793 -5.6; 6373 -9.0; 7010 -9.9; 7711 -6.7; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.28 | -4.5 dB |
| Peaking | 371 Hz   | 0.17 | -4.4 dB |
| Peaking | 1617 Hz  | 0.47 | 7.8 dB  |
| Peaking | 6799 Hz  | 4.43 | -6.0 dB |
| Peaking | 11606 Hz | 1.93 | -0.2 dB |
| Peaking | 2862 Hz  | 5.43 | -0.3 dB |
| Peaking | 5265 Hz  | 9.65 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20CX%20550/Sennheiser%20CX%20550.png)