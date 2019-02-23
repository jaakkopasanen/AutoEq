# Klipsch Image One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.5; 34 -2.2; 37 -2.9; 41 -3.6; 45 -4.3; 49 -4.8; 54 -5.4; 60 -5.9; 66 -6.3; 72 -6.6; 79 -7.1; 87 -7.6; 96 -8.0; 106 -8.2; 116 -8.6; 128 -8.6; 141 -8.9; 155 -9.1; 170 -9.0; 187 -9.2; 206 -8.9; 227 -8.5; 249 -8.1; 274 -7.8; 302 -7.7; 332 -7.4; 365 -6.9; 402 -6.7; 442 -6.7; 486 -6.2; 535 -5.4; 588 -4.3; 647 -3.2; 712 -2.8; 783 -3.3; 861 -4.1; 947 -4.9; 1042 -4.2; 1146 -5.7; 1261 -6.4; 1387 -7.2; 1526 -7.6; 1678 -8.3; 1846 -9.0; 2031 -9.5; 2234 -9.7; 2457 -10.3; 2703 -11.2; 2973 -10.9; 3270 -9.4; 3597 -6.8; 3957 -3.9; 4353 -2.9; 4788 -3.1; 5267 -3.3; 5793 -4.3; 6373 -4.1; 7010 -5.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 24 Hz   |  0.78 | 6.3 dB  |
| Peaking | 156 Hz  |  0.59 | -2.9 dB |
| Peaking | 746 Hz  |  1.43 | 4.2 dB  |
| Peaking | 3078 Hz |  1.07 | -9.2 dB |
| Peaking | 4214 Hz |  1.34 | 9.4 dB  |
| Peaking | 475 Hz  |  3.33 | -1.1 dB |
| Peaking | 485 Hz  |  1.6  | 0.7 dB  |
| Peaking | 3867 Hz |  7.04 | 0.5 dB  |
| Peaking | 6166 Hz | 13.03 | 2.6 dB  |
| Peaking | 6922 Hz |  0.83 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20One/Klipsch%20Image%20One.png)