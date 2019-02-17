# Nocs NS800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -6.8; 25 -6.8; 28 -6.8; 31 -6.9; 34 -6.9; 37 -7.0; 41 -7.1; 45 -7.2; 49 -7.4; 54 -7.6; 60 -7.9; 66 -8.0; 72 -8.2; 79 -8.5; 87 -8.8; 96 -8.9; 106 -9.2; 116 -9.2; 128 -9.5; 141 -9.5; 155 -9.8; 170 -9.7; 187 -9.8; 206 -9.7; 227 -9.6; 249 -9.6; 274 -9.3; 302 -9.1; 332 -8.8; 365 -8.5; 402 -8.2; 442 -7.9; 486 -7.7; 535 -7.3; 588 -7.0; 647 -6.7; 712 -6.2; 783 -6.1; 861 -6.2; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -7.6; 1526 -8.1; 1678 -8.2; 1846 -8.0; 2031 -7.7; 2234 -7.5; 2457 -7.3; 2703 -7.5; 2973 -7.0; 3270 -3.8; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 130 Hz  | 0.66 | -2.7 dB |
| Peaking | 267 Hz  | 1.2  | -1.7 dB |
| Peaking | 1831 Hz | 1.86 | -2.6 dB |
| Peaking | 2827 Hz | 4.11 | -3.7 dB |
| Peaking | 4413 Hz | 1.2  | 7.3 dB  |
| Peaking | 798 Hz  | 3.27 | 0.9 dB  |
| Peaking | 3563 Hz | 7.86 | 2.2 dB  |
| Peaking | 6259 Hz | 0.93 | -2.6 dB |
| Peaking | 6296 Hz | 2.61 | 5.2 dB  |
| Peaking | 7516 Hz | 3.21 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Nocs%20NS800/Nocs%20NS800.png)