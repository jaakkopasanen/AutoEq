# Turtle Beach Stealth 300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.9; 25 -9.3; 28 -9.9; 31 -10.4; 34 -10.7; 37 -10.9; 41 -11.2; 45 -11.3; 49 -11.5; 54 -11.6; 60 -11.6; 66 -11.7; 72 -11.7; 79 -11.7; 87 -11.8; 96 -11.7; 106 -11.6; 116 -11.5; 128 -11.4; 141 -11.1; 155 -10.9; 170 -10.5; 187 -10.1; 206 -9.5; 227 -8.9; 249 -8.4; 274 -7.8; 302 -7.1; 332 -6.2; 365 -5.2; 402 -4.6; 442 -5.1; 486 -6.5; 535 -7.4; 588 -7.4; 647 -6.8; 712 -6.5; 783 -6.7; 861 -6.9; 947 -7.0; 1042 -7.0; 1146 -6.4; 1261 -5.7; 1387 -4.9; 1526 -3.9; 1678 -2.7; 1846 -2.2; 2031 -1.7; 2234 -0.9; 2457 -0.5; 2703 -1.1; 2973 -1.5; 3270 -2.9; 3597 -3.3; 3957 -7.6; 4353 -9.5; 4788 -7.9; 5267 -7.8; 5793 -7.3; 6373 -9.2; 7010 -7.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Stealth 300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Stealth 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 66 Hz   | 0.39 | -3.1 dB |
| Peaking | 233 Hz  | 0.12 | -2.6 dB |
| Peaking | 384 Hz  | 1.68 | 4.5 dB  |
| Peaking | 2734 Hz | 0.81 | 9.3 dB  |
| Peaking | 4416 Hz | 1.3  | -6.9 dB |
| Peaking | 546 Hz  | 4.24 | -1.5 dB |
| Peaking | 662 Hz  | 1.6  | 1.1 dB  |
| Peaking | 1047 Hz | 3.18 | -1.0 dB |
| Peaking | 6488 Hz | 2.77 | 2.0 dB  |
| Peaking | 6574 Hz | 7.98 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Stealth%20300/Turtle%20Beach%20Stealth%20300.png)