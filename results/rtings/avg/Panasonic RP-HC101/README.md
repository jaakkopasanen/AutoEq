# Panasonic RP-HC101
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.1; 45 -2.2; 49 -3.3; 54 -4.4; 60 -5.3; 66 -6.0; 72 -6.5; 79 -6.9; 87 -7.3; 96 -7.6; 106 -7.9; 116 -8.2; 128 -8.5; 141 -8.7; 155 -8.8; 170 -8.8; 187 -8.8; 206 -8.6; 227 -8.6; 249 -8.6; 274 -8.7; 302 -8.9; 332 -9.3; 365 -10.2; 402 -11.2; 442 -11.8; 486 -11.8; 535 -11.3; 588 -10.6; 647 -9.6; 712 -8.5; 783 -7.3; 861 -6.1; 947 -5.3; 1042 -4.7; 1146 -4.5; 1261 -4.8; 1387 -5.4; 1526 -6.5; 1678 -7.8; 1846 -8.8; 2031 -8.7; 2234 -7.2; 2457 -4.8; 2703 -2.9; 2973 -2.2; 3270 -2.1; 3597 -1.4; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.9; 6373 -3.2; 7010 -8.3; 7711 -11.7; 8482 -7.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.3; 16529 -12.1; 18182 -13.7; 20000 -15.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC101 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC101 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.59 | 8.0 dB  |
| Peaking | 93 Hz   | 0.41 | -3.5 dB |
| Peaking | 475 Hz  | 1.98 | -5.3 dB |
| Peaking | 4709 Hz | 1.2  | 7.2 dB  |
| Peaking | 7643 Hz | 4.55 | -8.2 dB |
| Peaking | 464 Hz  | 0.13 | -0.2 dB |
| Peaking | 658 Hz  | 3.47 | -1.5 dB |
| Peaking | 1171 Hz | 1.32 | 3.2 dB  |
| Peaking | 1936 Hz | 1.95 | -4.8 dB |
| Peaking | 2775 Hz | 3.04 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -6.0 dB |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -4.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC101/Panasonic%20RP-HC101.png)