# Turtle Beach Stealth 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.5; 25 -9.8; 28 -10.0; 31 -10.2; 34 -10.3; 37 -10.3; 41 -10.3; 45 -10.3; 49 -10.4; 54 -10.4; 60 -10.5; 66 -10.7; 72 -10.8; 79 -10.9; 87 -11.0; 96 -11.0; 106 -11.2; 116 -11.5; 128 -11.8; 141 -12.0; 155 -12.2; 170 -12.3; 187 -12.3; 206 -12.2; 227 -12.1; 249 -11.8; 274 -11.3; 302 -10.5; 332 -9.7; 365 -8.9; 402 -8.1; 442 -7.2; 486 -6.3; 535 -5.6; 588 -5.7; 647 -6.5; 712 -7.1; 783 -7.2; 861 -6.6; 947 -5.6; 1042 -4.9; 1146 -4.3; 1261 -3.8; 1387 -3.3; 1526 -2.5; 1678 -1.8; 1846 -1.6; 2031 -2.7; 2234 -4.0; 2457 -4.3; 2703 -4.1; 2973 -3.4; 3270 -2.3; 3597 -0.5; 3957 -2.7; 4353 -5.7; 4788 -6.2; 5267 -5.3; 5793 -3.4; 6373 -2.5; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Stealth 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Stealth 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 53 Hz    | 0.31 | -3.9 dB |
| Peaking | 204 Hz   | 1.04 | -4.4 dB |
| Peaking | 1682 Hz  | 1.38 | 4.6 dB  |
| Peaking | 3578 Hz  | 3.88 | 5.4 dB  |
| Peaking | 21305 Hz | 2.29 | 1.4 dB  |
| Peaking | 307 Hz   | 3.29 | -0.8 dB |
| Peaking | 538 Hz   | 2.8  | 1.9 dB  |
| Peaking | 755 Hz   | 4.02 | -1.4 dB |
| Peaking | 4594 Hz  | 4.95 | -1.6 dB |
| Peaking | 6211 Hz  | 4.87 | 4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Stealth%20700/Turtle%20Beach%20Stealth%20700.png)