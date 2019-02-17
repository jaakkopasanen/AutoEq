# Turtle Beach Elite 800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -8.6; 25 -8.5; 28 -8.4; 31 -8.3; 34 -8.3; 37 -8.4; 41 -8.4; 45 -8.6; 49 -8.8; 54 -9.1; 60 -9.4; 66 -9.8; 72 -10.1; 79 -10.3; 87 -10.5; 96 -10.6; 106 -10.5; 116 -10.5; 128 -10.3; 141 -10.2; 155 -10.1; 170 -9.8; 187 -9.5; 206 -9.0; 227 -8.5; 249 -8.0; 274 -7.5; 302 -6.7; 332 -5.5; 365 -3.6; 402 -1.2; 442 -0.5; 486 -1.8; 535 -3.2; 588 -4.0; 647 -4.7; 712 -5.2; 783 -5.5; 861 -5.7; 947 -6.1; 1042 -6.7; 1146 -7.3; 1261 -8.0; 1387 -8.9; 1526 -9.9; 1678 -11.6; 1846 -13.4; 2031 -12.9; 2234 -11.3; 2457 -10.2; 2703 -10.3; 2973 -12.1; 3270 -14.9; 3597 -15.2; 3957 -11.0; 4353 -7.2; 4788 -4.7; 5267 -4.0; 5793 -6.4; 6373 -2.6; 7010 -4.8; 7711 -8.4; 8482 -11.6; 9330 -12.0; 10263 -8.3; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.9; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Elite 800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Elite 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 115 Hz   | 0.37 | -4.2 dB |
| Peaking | 440 Hz   | 1.74 | 7.3 dB  |
| Peaking | 1902 Hz  | 2.37 | -6.9 dB |
| Peaking | 3407 Hz  | 4.5  | -9.3 dB |
| Peaking | 21085 Hz | 2.16 | -2.9 dB |
| Peaking | 20 Hz    | 2.07 | -1.4 dB |
| Peaking | 857 Hz   | 5.05 | 0.7 dB  |
| Peaking | 3797 Hz  | 6.24 | -2.5 dB |
| Peaking | 6775 Hz  | 1.21 | 5.0 dB  |
| Peaking | 8712 Hz  | 2.68 | -9.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 5.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.5 dB |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Elite%20800/Turtle%20Beach%20Elite%20800.png)