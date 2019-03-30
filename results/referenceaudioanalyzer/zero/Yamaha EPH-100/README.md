# Yamaha EPH-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.8; 23 -16.2; 25 -16.5; 28 -16.9; 31 -17.1; 34 -17.3; 37 -17.4; 41 -17.5; 45 -17.6; 49 -17.6; 54 -17.6; 60 -17.5; 66 -17.3; 72 -17.1; 79 -16.9; 87 -16.7; 96 -16.4; 106 -16.0; 116 -15.6; 128 -15.3; 141 -14.7; 155 -14.3; 170 -13.8; 187 -13.3; 206 -12.8; 227 -12.2; 249 -11.6; 274 -11.1; 302 -10.5; 332 -10.0; 365 -9.4; 402 -9.0; 442 -8.4; 486 -8.0; 535 -7.6; 588 -7.2; 647 -6.9; 712 -6.6; 783 -6.4; 861 -6.2; 947 -6.2; 1042 -6.3; 1146 -6.5; 1261 -6.5; 1387 -6.6; 1526 -7.1; 1678 -8.0; 1846 -9.0; 2031 -10.0; 2234 -10.8; 2457 -11.0; 2703 -10.2; 2973 -8.4; 3270 -5.9; 3597 -3.3; 3957 -1.0; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha EPH-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha EPH-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.56 | -7.1 dB |
| Peaking | 92 Hz   | 0.41 | -8.6 dB |
| Peaking | 2471 Hz | 2.14 | -6.5 dB |
| Peaking | 4699 Hz | 1.4  | 7.5 dB  |
| Peaking | 888 Hz  | 1.33 | 1.1 dB  |
| Peaking | 1884 Hz | 5.81 | -1.0 dB |
| Peaking | 4939 Hz | 6.86 | -1.2 dB |
| Peaking | 6442 Hz | 2.94 | 3.7 dB  |
| Peaking | 7513 Hz | 1.95 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.6 dB |
| Peaking | 62 Hz    | 1.41 | -8.5 dB  |
| Peaking | 125 Hz   | 1.41 | -7.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Yamaha%20EPH-100/Yamaha%20EPH-100.png)