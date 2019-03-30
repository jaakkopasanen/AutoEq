# Beyerdynamic DTX 101 iE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.0; 49 -1.5; 54 -1.9; 60 -2.3; 66 -2.6; 72 -2.9; 79 -3.2; 87 -3.4; 96 -3.6; 106 -3.7; 116 -3.9; 128 -4.0; 141 -4.2; 155 -4.2; 170 -4.2; 187 -4.4; 206 -4.6; 227 -4.6; 249 -4.8; 274 -5.1; 302 -5.3; 332 -5.6; 365 -5.8; 402 -6.0; 442 -6.3; 486 -6.5; 535 -6.8; 588 -6.9; 647 -7.2; 712 -7.1; 783 -6.8; 861 -6.8; 947 -6.9; 1042 -7.3; 1146 -7.5; 1261 -7.9; 1387 -8.3; 1526 -8.5; 1678 -8.4; 1846 -8.2; 2031 -8.1; 2234 -7.8; 2457 -7.4; 2703 -6.6; 2973 -6.2; 3270 -5.8; 3597 -5.3; 3957 -4.9; 4353 -5.0; 4788 -6.2; 5267 -9.3; 5793 -13.2; 6373 -13.9; 7010 -11.0; 7711 -6.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DTX 101 iE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DTX 101 iE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 12 Hz   |  0.1  | 5.8 dB   |
| Peaking | 1757 Hz |  0.95 | -2.6 dB  |
| Peaking | 2834 Hz |  1.43 | -0.9 dB  |
| Peaking | 4569 Hz |  0.73 | 4.5 dB   |
| Peaking | 6121 Hz |  2.77 | -11.5 dB |
| Peaking | 41 Hz   |  1.14 | 1.2 dB   |
| Peaking | 70 Hz   |  0.79 | -1.0 dB  |
| Peaking | 220 Hz  |  1.19 | 0.8 dB   |
| Peaking | 596 Hz  |  2.97 | -0.6 dB  |
| Peaking | 7907 Hz | 11.04 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.7 dB  |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DTX%20101%20iE/Beyerdynamic%20DTX%20101%20iE.png)