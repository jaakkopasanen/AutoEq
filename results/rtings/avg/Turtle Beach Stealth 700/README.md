# Turtle Beach Stealth 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.3; 25 -10.6; 28 -10.8; 31 -11.0; 34 -11.1; 37 -11.1; 41 -11.1; 45 -11.1; 49 -11.1; 54 -11.1; 60 -11.3; 66 -11.4; 72 -11.6; 79 -11.7; 87 -11.8; 96 -11.8; 106 -12.0; 116 -12.3; 128 -12.6; 141 -12.8; 155 -13.0; 170 -13.0; 187 -13.1; 206 -13.0; 227 -12.7; 249 -12.5; 274 -11.9; 302 -11.2; 332 -10.4; 365 -9.6; 402 -8.7; 442 -7.8; 486 -6.8; 535 -6.1; 588 -6.2; 647 -7.0; 712 -7.6; 783 -7.7; 861 -7.2; 947 -6.1; 1042 -5.4; 1146 -4.7; 1261 -4.2; 1387 -3.7; 1526 -2.8; 1678 -2.2; 1846 -1.9; 2031 -2.8; 2234 -3.8; 2457 -3.9; 2703 -4.2; 2973 -3.9; 3270 -3.3; 3597 -0.5; 3957 -3.6; 4353 -6.5; 4788 -6.4; 5267 -5.5; 5793 -4.1; 6373 -3.8; 7010 -4.9; 7711 -5.4; 8482 -6.0; 9330 -5.9; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -6.0; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Stealth 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Stealth 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.25 | -5.1 dB |
| Peaking | 152 Hz  | 0.99 | -2.5 dB |
| Peaking | 252 Hz  | 1.14 | -3.7 dB |
| Peaking | 1769 Hz | 1.97 | 4.0 dB  |
| Peaking | 3606 Hz | 6.98 | 5.2 dB  |
| Peaking | 540 Hz  | 4.58 | 1.4 dB  |
| Peaking | 770 Hz  | 3.85 | -1.8 dB |
| Peaking | 3948 Hz | 2.51 | 1.3 dB  |
| Peaking | 4417 Hz | 4    | -2.9 dB |
| Peaking | 6131 Hz | 5.5  | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -6.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Stealth%20700/Turtle%20Beach%20Stealth%20700.png)