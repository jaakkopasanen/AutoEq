# Bose AE2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.4; 25 -3.1; 28 -3.9; 31 -4.5; 34 -4.9; 37 -5.2; 41 -5.5; 45 -5.6; 49 -5.6; 54 -5.5; 60 -5.3; 66 -5.3; 72 -5.6; 79 -6.0; 87 -6.3; 96 -6.7; 106 -7.0; 116 -7.4; 128 -7.8; 141 -8.1; 155 -8.2; 170 -8.2; 187 -8.0; 206 -7.7; 227 -7.1; 249 -6.6; 274 -6.2; 302 -5.9; 332 -5.7; 365 -5.5; 402 -5.2; 442 -5.0; 486 -4.7; 535 -4.8; 588 -5.0; 647 -5.3; 712 -5.7; 783 -6.1; 861 -6.4; 947 -6.5; 1042 -6.1; 1146 -5.5; 1261 -4.7; 1387 -3.8; 1526 -2.8; 1678 -1.9; 1846 -1.3; 2031 -1.1; 2234 -0.7; 2457 -0.5; 2703 -1.5; 2973 -2.7; 3270 -3.7; 3597 -5.1; 3957 -7.1; 4353 -8.3; 4788 -7.9; 5267 -8.0; 5793 -8.4; 6373 -6.7; 7010 -5.1; 7711 -7.8; 8482 -11.7; 9330 -14.0; 10263 -13.7; 11289 -11.5; 12418 -7.4; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose AE2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose AE2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.3  | 5.1 dB  |
| Peaking | 156 Hz   | 1.62 | -2.6 dB |
| Peaking | 2287 Hz  | 1.31 | 5.9 dB  |
| Peaking | 4479 Hz  | 2.61 | -3.5 dB |
| Peaking | 9822 Hz  | 2.55 | -9.2 dB |
| Peaking | 490 Hz   | 1.9  | 1.2 dB  |
| Peaking | 932 Hz   | 3.12 | -1.6 dB |
| Peaking | 7057 Hz  | 5.02 | 5.1 dB  |
| Peaking | 7134 Hz  | 2.01 | -2.5 dB |
| Peaking | 12714 Hz | 4.28 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Bose%20AE2/Bose%20AE2.png)