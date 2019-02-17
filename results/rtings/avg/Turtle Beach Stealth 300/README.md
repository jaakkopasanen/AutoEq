# Turtle Beach Stealth 300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.3; 25 -8.8; 28 -9.4; 31 -9.8; 34 -10.1; 37 -10.4; 41 -10.6; 45 -10.8; 49 -10.9; 54 -11.0; 60 -11.1; 66 -11.2; 72 -11.2; 79 -11.2; 87 -11.2; 96 -11.1; 106 -11.0; 116 -11.0; 128 -10.8; 141 -10.6; 155 -10.3; 170 -9.9; 187 -9.5; 206 -9.0; 227 -8.3; 249 -7.8; 274 -7.3; 302 -6.5; 332 -5.6; 365 -4.6; 402 -4.0; 442 -4.5; 486 -5.9; 535 -6.9; 588 -6.8; 647 -6.3; 712 -6.0; 783 -6.2; 861 -6.4; 947 -6.5; 1042 -6.4; 1146 -5.9; 1261 -5.2; 1387 -4.3; 1526 -3.4; 1678 -2.1; 1846 -1.6; 2031 -1.1; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.9; 3270 -2.3; 3597 -2.8; 3957 -7.1; 4353 -8.9; 4788 -7.3; 5267 -7.2; 5793 -6.7; 6373 -8.7; 7010 -6.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Stealth 300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Stealth 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 78 Hz   | 0.35 | -4.8 dB |
| Peaking | 381 Hz  | 2.59 | 3.7 dB  |
| Peaking | 2599 Hz | 1.08 | 7.3 dB  |
| Peaking | 4435 Hz | 2.08 | -4.6 dB |
| Peaking | 1051 Hz | 2.8  | -1.1 dB |
| Peaking | 1700 Hz | 3.51 | 1.1 dB  |
| Peaking | 2489 Hz | 6.93 | -0.8 dB |
| Peaking | 6446 Hz | 2.8  | 1.3 dB  |
| Peaking | 6521 Hz | 8.31 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Stealth%20300/Turtle%20Beach%20Stealth%20300.png)