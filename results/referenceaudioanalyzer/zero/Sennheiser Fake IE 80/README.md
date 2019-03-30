# Sennheiser Fake IE 80
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.5; 31 -2.6; 34 -3.5; 37 -4.4; 41 -5.3; 45 -6.2; 49 -6.9; 54 -7.6; 60 -8.3; 66 -8.8; 72 -9.2; 79 -9.7; 87 -10.1; 96 -10.5; 106 -10.8; 116 -10.9; 128 -10.9; 141 -11.2; 155 -11.2; 170 -11.2; 187 -11.3; 206 -11.5; 227 -11.7; 249 -11.5; 274 -11.8; 302 -11.8; 332 -11.5; 365 -11.2; 402 -10.7; 442 -10.1; 486 -9.4; 535 -8.7; 588 -7.9; 647 -7.1; 712 -6.2; 783 -5.3; 861 -4.4; 947 -3.6; 1042 -2.9; 1146 -2.3; 1261 -2.1; 1387 -2.1; 1526 -2.3; 1678 -2.5; 1846 -2.2; 2031 -1.4; 2234 -0.6; 2457 -0.5; 2703 -0.8; 2973 -1.6; 3270 -2.8; 3597 -4.5; 3957 -5.6; 4353 -6.4; 4788 -8.0; 5267 -10.6; 5793 -11.8; 6373 -10.2; 7010 -5.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Fake IE 80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Fake IE 80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.02 | 6.9 dB  |
| Peaking | 273 Hz  | 0.24 | -5.9 dB |
| Peaking | 1086 Hz | 0.79 | 6.7 dB  |
| Peaking | 2567 Hz | 1.63 | 5.3 dB  |
| Peaking | 5632 Hz | 3.83 | -6.6 dB |
| Peaking | 176 Hz  | 3.77 | 0.5 dB  |
| Peaking | 317 Hz  | 3.85 | -0.5 dB |
| Peaking | 6340 Hz | 8.87 | -1.9 dB |
| Peaking | 7083 Hz | 6.82 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20Fake%20IE%2080/Sennheiser%20Fake%20IE%2080.png)