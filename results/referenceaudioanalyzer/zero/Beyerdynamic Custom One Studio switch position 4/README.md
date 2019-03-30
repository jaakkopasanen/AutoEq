# Beyerdynamic Custom One Studio switch position 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -2.1; 96 -5.9; 106 -8.8; 116 -10.9; 128 -12.1; 141 -12.7; 155 -12.8; 170 -12.5; 187 -11.8; 206 -11.2; 227 -10.5; 249 -10.0; 274 -9.5; 302 -9.1; 332 -8.7; 365 -8.1; 402 -7.6; 442 -7.3; 486 -6.9; 535 -6.6; 588 -6.2; 647 -5.9; 712 -5.2; 783 -4.4; 861 -4.0; 947 -3.8; 1042 -3.7; 1146 -3.5; 1261 -3.4; 1387 -3.4; 1526 -3.1; 1678 -3.2; 1846 -3.7; 2031 -4.3; 2234 -4.7; 2457 -4.7; 2703 -4.7; 2973 -5.0; 3270 -5.2; 3597 -5.4; 3957 -4.4; 4353 -2.5; 4788 -2.2; 5267 -5.4; 5793 -8.3; 6373 -9.2; 7010 -7.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom One Studio switch position 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Studio switch position 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 80 Hz   | 0.36 | 22.1 dB  |
| Peaking | 130 Hz  | 0.49 | -24.1 dB |
| Peaking | 1140 Hz | 0.58 | 4.2 dB   |
| Peaking | 4633 Hz | 4.45 | 4.8 dB   |
| Peaking | 6139 Hz | 4.29 | -3.8 dB  |
| Peaking | 18 Hz   | 1.14 | 1.6 dB   |
| Peaking | 60 Hz   | 1.73 | -0.9 dB  |
| Peaking | 83 Hz   | 6.04 | 2.0 dB   |
| Peaking | 103 Hz  | 5.66 | -0.9 dB  |
| Peaking | 2239 Hz | 7.21 | -0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 8.4 dB  |
| Peaking | 125 Hz   | 1.41 | -6.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20Custom%20One%20Studio%20switch%20position%204/Beyerdynamic%20Custom%20One%20Studio%20switch%20position%204.png)