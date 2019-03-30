# Beyerdynamic DTX 710
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.1; 45 -2.0; 49 -2.8; 54 -3.6; 60 -4.3; 66 -4.9; 72 -5.4; 79 -5.8; 87 -6.3; 96 -6.8; 106 -7.2; 116 -7.6; 128 -7.8; 141 -8.0; 155 -8.0; 170 -8.0; 187 -7.9; 206 -7.7; 227 -7.5; 249 -7.3; 274 -7.1; 302 -7.0; 332 -6.7; 365 -6.4; 402 -6.1; 442 -6.0; 486 -5.7; 535 -5.3; 588 -5.0; 647 -4.7; 712 -4.4; 783 -4.4; 861 -4.5; 947 -4.9; 1042 -5.1; 1146 -5.5; 1261 -6.7; 1387 -8.3; 1526 -9.5; 1678 -10.5; 1846 -11.0; 2031 -10.9; 2234 -10.0; 2457 -8.5; 2703 -6.9; 2973 -5.5; 3270 -4.6; 3597 -3.7; 3957 -1.9; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.8; 7010 -7.5; 7711 -11.1; 8482 -13.1; 9330 -13.6; 10263 -12.1; 11289 -9.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DTX 710 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DTX 710 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 1.17 | 7.1 dB   |
| Peaking | 883 Hz   | 1.34 | 3.0 dB   |
| Peaking | 1928 Hz  | 1.38 | -6.5 dB  |
| Peaking | 5361 Hz  | 0.96 | 9.6 dB   |
| Peaking | 8589 Hz  | 1.66 | -11.8 dB |
| Peaking | 50 Hz    | 1.62 | 1.2 dB   |
| Peaking | 152 Hz   | 0.88 | -1.9 dB  |
| Peaking | 545 Hz   | 2.22 | 0.6 dB   |
| Peaking | 10471 Hz | 4.25 | -2.3 dB  |
| Peaking | 12109 Hz | 1.9  | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DTX%20710/Beyerdynamic%20DTX%20710.png)