# Beyerdynamic Custom Pro One switch position 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -0.6; 60 -0.8; 66 -0.6; 72 -0.5; 79 -0.5; 87 -0.5; 96 -2.3; 106 -8.2; 116 -9.6; 128 -11.0; 141 -11.5; 155 -10.8; 170 -10.9; 187 -12.1; 206 -11.7; 227 -11.2; 249 -10.8; 274 -10.4; 302 -9.9; 332 -9.5; 365 -9.0; 402 -8.5; 442 -8.0; 486 -7.8; 535 -7.4; 588 -6.9; 647 -6.7; 712 -6.7; 783 -5.5; 861 -5.5; 947 -5.7; 1042 -5.5; 1146 -5.4; 1261 -5.5; 1387 -6.1; 1526 -7.0; 1678 -8.0; 1846 -8.7; 2031 -9.0; 2234 -8.8; 2457 -7.3; 2703 -6.0; 2973 -4.4; 3270 -3.6; 3597 -2.9; 3957 -1.8; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom Pro One switch position 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom Pro One switch position 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 81 Hz   | 0.37 | 23.2 dB  |
| Peaking | 133 Hz  | 0.41 | -23.2 dB |
| Peaking | 1357 Hz | 0.46 | 4.0 dB   |
| Peaking | 1980 Hz | 1.65 | -6.2 dB  |
| Peaking | 4926 Hz | 1.58 | 6.2 dB   |
| Peaking | 21 Hz   | 1.98 | 1.6 dB   |
| Peaking | 93 Hz   | 7.03 | 4.9 dB   |
| Peaking | 99 Hz   | 3.34 | -2.9 dB  |
| Peaking | 6412 Hz | 4.7  | 3.3 dB   |
| Peaking | 7735 Hz | 1.68 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 7.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20Custom%20Pro%20One%20switch%20position%201/Beyerdynamic%20Custom%20Pro%20One%20switch%20position%201.png)