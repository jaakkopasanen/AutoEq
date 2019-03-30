# Beyerdynamic Custom One Studio switch position 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.4; 25 -2.2; 28 -3.3; 31 -4.0; 34 -4.6; 37 -5.0; 41 -5.4; 45 -5.8; 49 -6.1; 54 -6.4; 60 -6.5; 66 -6.2; 72 -6.0; 79 -6.4; 87 -7.2; 96 -8.0; 106 -8.7; 116 -9.3; 128 -9.6; 141 -9.2; 155 -8.7; 170 -8.1; 187 -7.2; 206 -6.1; 227 -5.0; 249 -4.4; 274 -4.0; 302 -4.0; 332 -4.0; 365 -4.0; 402 -4.0; 442 -3.7; 486 -3.7; 535 -3.7; 588 -3.7; 647 -3.4; 712 -3.0; 783 -2.4; 861 -2.1; 947 -1.9; 1042 -1.7; 1146 -1.7; 1261 -1.8; 1387 -1.6; 1526 -1.4; 1678 -1.5; 1846 -1.9; 2031 -2.6; 2234 -3.0; 2457 -3.1; 2703 -3.0; 2973 -3.3; 3270 -3.5; 3597 -3.7; 3957 -2.7; 4353 -0.8; 4788 -0.6; 5267 -3.8; 5793 -6.8; 6373 -7.6; 7010 -5.9; 7711 -3.7; 8482 -3.9; 9330 -3.9; 10263 -3.9; 11289 -4.0; 12418 -4.7; 13660 -3.9; 15026 -3.9; 16529 -3.9; 18182 -3.9; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom One Studio switch position 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Studio switch position 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.6  | 4.5 dB  |
| Peaking | 48 Hz   | 1.2  | -1.9 dB |
| Peaking | 130 Hz  | 1.29 | -5.7 dB |
| Peaking | 1743 Hz | 0.31 | 1.9 dB  |
| Peaking | 6287 Hz | 4.98 | -5.2 dB |
| Peaking | 263 Hz  | 5.01 | 0.8 dB  |
| Peaking | 583 Hz  | 1.98 | -0.9 dB |
| Peaking | 1508 Hz | 0.75 | 1.6 dB  |
| Peaking | 2922 Hz | 0.68 | -2.0 dB |
| Peaking | 4583 Hz | 5.03 | 4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20Custom%20One%20Studio%20switch%20position%202/Beyerdynamic%20Custom%20One%20Studio%20switch%20position%202.png)