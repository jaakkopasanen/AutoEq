# Turtle Beach Stealth 300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.9; 25 -8.4; 28 -9.0; 31 -9.4; 34 -9.8; 37 -10.0; 41 -10.2; 45 -10.4; 49 -10.5; 54 -10.6; 60 -10.7; 66 -10.8; 72 -10.8; 79 -10.8; 87 -10.8; 96 -10.7; 106 -10.6; 116 -10.5; 128 -10.4; 141 -10.2; 155 -9.9; 170 -9.5; 187 -9.1; 206 -8.6; 227 -8.0; 249 -7.5; 274 -7.0; 302 -6.3; 332 -5.4; 365 -4.3; 402 -3.8; 442 -4.3; 486 -5.8; 535 -6.7; 588 -6.6; 647 -6.1; 712 -5.9; 783 -6.1; 861 -6.3; 947 -6.4; 1042 -6.4; 1146 -5.8; 1261 -5.1; 1387 -4.3; 1526 -3.3; 1678 -2.1; 1846 -1.7; 2031 -1.4; 2234 -0.8; 2457 -0.5; 2703 -0.8; 2973 -0.9; 3270 -1.8; 3597 -2.6; 3957 -6.7; 4353 -8.2; 4788 -7.5; 5267 -7.4; 5793 -6.5; 6373 -7.4; 7010 -6.3; 7711 -5.4; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Stealth 300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Stealth 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 152 Hz  | 0.15 | -5.5 dB |
| Peaking | 374 Hz  | 1.06 | 6.1 dB  |
| Peaking | 2883 Hz | 0.76 | 8.5 dB  |
| Peaking | 4466 Hz | 1.34 | -7.4 dB |
| Peaking | 17 Hz   | 2.11 | 0.8 dB  |
| Peaking | 422 Hz  | 4.71 | 1.6 dB  |
| Peaking | 575 Hz  | 1.43 | -1.7 dB |
| Peaking | 687 Hz  | 2.95 | 2.1 dB  |
| Peaking | 5052 Hz | 7.24 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Stealth%20300/Turtle%20Beach%20Stealth%20300.png)