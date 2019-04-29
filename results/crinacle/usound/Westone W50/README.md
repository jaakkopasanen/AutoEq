# Westone W50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.7; 25 -9.0; 28 -9.4; 31 -9.7; 34 -9.9; 37 -10.1; 41 -10.4; 45 -10.7; 49 -10.8; 54 -11.0; 60 -11.4; 66 -11.7; 72 -12.1; 79 -12.4; 87 -12.8; 96 -13.3; 106 -13.6; 116 -14.0; 128 -14.2; 141 -14.4; 155 -14.6; 170 -14.7; 187 -14.7; 206 -14.6; 227 -14.4; 249 -14.3; 274 -14.0; 302 -13.7; 332 -13.4; 365 -12.9; 402 -12.4; 442 -11.9; 486 -11.4; 535 -10.7; 588 -10.1; 647 -9.3; 712 -8.4; 783 -7.6; 861 -6.8; 947 -6.3; 1042 -6.2; 1146 -6.7; 1261 -7.4; 1387 -7.9; 1526 -7.6; 1678 -6.6; 1846 -4.8; 2031 -2.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -1.2; 3270 -1.2; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -8.4; 16529 -6.7; 18182 -7.5; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 70 Hz    | 0.35 | -3.8 dB |
| Peaking | 158 Hz   | 0.74 | -4.1 dB |
| Peaking | 346 Hz   | 0.82 | -4.3 dB |
| Peaking | 2493 Hz  | 2.39 | 5.5 dB  |
| Peaking | 4732 Hz  | 1.38 | 6.4 dB  |
| Peaking | 949 Hz   | 3.54 | 1.5 dB  |
| Peaking | 1455 Hz  | 4.15 | -2.2 dB |
| Peaking | 6375 Hz  | 4.24 | 3.6 dB  |
| Peaking | 7548 Hz  | 1.76 | -2.3 dB |
| Peaking | 20079 Hz | 0.93 | -5.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.8 dB |
| Peaking | 500 Hz   | 1.41 | -3.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Westone%20W50/Westone%20W50.png)