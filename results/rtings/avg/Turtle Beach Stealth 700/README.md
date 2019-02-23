# Turtle Beach Stealth 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.7; 25 -9.9; 28 -10.2; 31 -10.4; 34 -10.4; 37 -10.4; 41 -10.5; 45 -10.5; 49 -10.5; 54 -10.5; 60 -10.6; 66 -10.8; 72 -10.9; 79 -11.1; 87 -11.2; 96 -11.1; 106 -11.4; 116 -11.7; 128 -12.0; 141 -12.2; 155 -12.3; 170 -12.4; 187 -12.5; 206 -12.3; 227 -12.1; 249 -11.8; 274 -11.3; 302 -10.5; 332 -9.7; 365 -8.9; 402 -8.1; 442 -7.2; 486 -6.2; 535 -5.5; 588 -5.6; 647 -6.3; 712 -6.9; 783 -7.0; 861 -6.5; 947 -5.5; 1042 -4.8; 1146 -4.1; 1261 -3.6; 1387 -3.1; 1526 -2.2; 1678 -1.5; 1846 -1.2; 2031 -2.2; 2234 -3.2; 2457 -3.3; 2703 -3.6; 2973 -3.3; 3270 -2.6; 3597 -0.5; 3957 -2.9; 4353 -5.9; 4788 -5.8; 5267 -4.9; 5793 -3.4; 6373 -3.2; 7010 -4.5; 7711 -6.2; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Stealth 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Stealth 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 52 Hz    | 0.3  | -4.0 dB |
| Peaking | 202 Hz   | 0.99 | -4.5 dB |
| Peaking | 1790 Hz  | 1.02 | 4.7 dB  |
| Peaking | 3615 Hz  | 5.39 | 4.9 dB  |
| Peaking | 21424 Hz | 2.22 | 1.2 dB  |
| Peaking | 308 Hz   | 3.18 | -0.7 dB |
| Peaking | 539 Hz   | 2.89 | 1.9 dB  |
| Peaking | 772 Hz   | 3.48 | -1.6 dB |
| Peaking | 4455 Hz  | 5.92 | -1.6 dB |
| Peaking | 6148 Hz  | 4.38 | 3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Stealth%20700/Turtle%20Beach%20Stealth%20700.png)