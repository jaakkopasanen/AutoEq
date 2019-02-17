# Beyerdynamic Custom One Pro switch position 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.3; 25 -6.7; 28 -7.2; 31 -7.7; 34 -8.0; 37 -8.2; 41 -8.4; 45 -8.6; 49 -8.6; 54 -8.2; 60 -7.7; 66 -7.5; 72 -7.9; 79 -7.3; 87 -4.7; 96 -2.8; 106 -4.6; 116 -7.2; 128 -9.2; 141 -10.0; 155 -8.7; 170 -7.8; 187 -8.9; 206 -8.7; 227 -8.5; 249 -8.6; 274 -8.6; 302 -8.5; 332 -8.4; 365 -8.2; 402 -8.1; 442 -7.9; 486 -7.9; 535 -7.8; 588 -7.5; 647 -7.5; 712 -7.5; 783 -6.6; 861 -6.3; 947 -6.5; 1042 -6.5; 1146 -6.4; 1261 -6.6; 1387 -7.2; 1526 -8.0; 1678 -8.8; 1846 -9.1; 2031 -9.0; 2234 -8.2; 2457 -6.1; 2703 -4.4; 2973 -2.6; 3270 -1.7; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom One Pro switch position 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Pro switch position 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 96 Hz   | 3.1  | 8.5 dB  |
| Peaking | 103 Hz  | 0.73 | -4.6 dB |
| Peaking | 379 Hz  | 1.05 | -1.2 dB |
| Peaking | 1964 Hz | 2.32 | -4.5 dB |
| Peaking | 4277 Hz | 1.07 | 7.1 dB  |
| Peaking | 42 Hz   | 2.23 | -1.0 dB |
| Peaking | 63 Hz   | 4.59 | 1.2 dB  |
| Peaking | 4455 Hz | 5.97 | -1.0 dB |
| Peaking | 6367 Hz | 2.67 | 4.3 dB  |
| Peaking | 7506 Hz | 1.76 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%203/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%203.png)