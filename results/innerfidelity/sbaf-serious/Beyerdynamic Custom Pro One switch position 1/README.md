# Beyerdynamic Custom Pro One switch position 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.0; 45 -1.4; 49 -1.5; 54 -1.5; 60 -1.7; 66 -1.4; 72 -0.6; 79 -0.5; 87 -0.5; 96 -3.2; 106 -9.1; 116 -10.5; 128 -11.9; 141 -12.4; 155 -11.8; 170 -11.8; 187 -13.0; 206 -12.6; 227 -12.2; 249 -11.7; 274 -11.3; 302 -10.8; 332 -10.4; 365 -9.9; 402 -9.5; 442 -8.9; 486 -8.7; 535 -8.4; 588 -7.8; 647 -7.6; 712 -7.6; 783 -6.4; 861 -6.4; 947 -6.6; 1042 -6.4; 1146 -6.3; 1261 -6.4; 1387 -7.0; 1526 -8.0; 1678 -8.9; 1846 -9.6; 2031 -10.0; 2234 -9.7; 2457 -8.2; 2703 -7.0; 2973 -5.4; 3270 -4.6; 3597 -3.8; 3957 -2.7; 4353 -1.2; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom Pro One switch position 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom Pro One switch position 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 39 Hz   |  0.42 | 8.5 dB   |
| Peaking | 84 Hz   |  2.26 | 9.8 dB   |
| Peaking | 127 Hz  |  0.54 | -10.8 dB |
| Peaking | 2078 Hz |  2.8  | -4.3 dB  |
| Peaking | 5005 Hz |  1.69 | 6.8 dB   |
| Peaking | 162 Hz  | 10.39 | 2.0 dB   |
| Peaking | 1073 Hz |  1.46 | 1.0 dB   |
| Peaking | 1652 Hz |  5.23 | -1.2 dB  |
| Peaking | 6397 Hz |  4.81 | 2.1 dB   |
| Peaking | 8472 Hz |  1.99 | -1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 7.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20Custom%20Pro%20One%20switch%20position%201/Beyerdynamic%20Custom%20Pro%20One%20switch%20position%201.png)