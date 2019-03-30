# Beyerdynamic DTX 910
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.5; 60 -2.5; 66 -3.4; 72 -4.2; 79 -5.1; 87 -5.8; 96 -6.5; 106 -7.0; 116 -7.4; 128 -7.7; 141 -8.0; 155 -8.3; 170 -8.4; 187 -8.4; 206 -8.1; 227 -8.0; 249 -7.8; 274 -7.5; 302 -7.4; 332 -7.2; 365 -6.9; 402 -6.7; 442 -6.4; 486 -6.1; 535 -5.9; 588 -5.8; 647 -5.8; 712 -5.5; 783 -5.5; 861 -5.5; 947 -5.4; 1042 -5.4; 1146 -5.8; 1261 -6.4; 1387 -6.9; 1526 -7.3; 1678 -8.0; 1846 -9.0; 2031 -9.7; 2234 -9.5; 2457 -8.6; 2703 -7.2; 2973 -5.8; 3270 -5.1; 3597 -4.3; 3957 -2.1; 4353 -0.5; 4788 -1.4; 5267 -1.6; 5793 -0.6; 6373 -1.0; 7010 -5.5; 7711 -10.4; 8482 -12.9; 9330 -13.3; 10263 -11.5; 11289 -8.4; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DTX 910 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DTX 910 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 39 Hz    |  0.4  | 7.7 dB   |
| Peaking | 119 Hz   |  0.54 | -4.8 dB  |
| Peaking | 2196 Hz  |  0.99 | -9.2 dB  |
| Peaking | 6372 Hz  |  0.39 | 23.7 dB  |
| Peaking | 8528 Hz  |  0.76 | -26.9 dB |
| Peaking | 3565 Hz  |  6.52 | -1.0 dB  |
| Peaking | 4165 Hz  | 10.21 | 1.4 dB   |
| Peaking | 10333 Hz |  4.97 | -1.7 dB  |
| Peaking | 12034 Hz |  2.39 | 1.7 dB   |
| Peaking | 17775 Hz |  0.57 | -0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DTX%20910/Beyerdynamic%20DTX%20910.png)