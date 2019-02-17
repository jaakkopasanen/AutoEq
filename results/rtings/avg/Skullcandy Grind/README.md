# Skullcandy Grind
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.5; 25 -6.0; 28 -6.5; 31 -6.9; 34 -7.2; 37 -7.3; 41 -7.5; 45 -7.6; 49 -7.7; 54 -7.8; 60 -8.0; 66 -8.1; 72 -8.2; 79 -8.3; 87 -8.4; 96 -8.5; 106 -8.5; 116 -8.6; 128 -8.5; 141 -8.4; 155 -8.4; 170 -8.3; 187 -8.2; 206 -8.1; 227 -8.1; 249 -8.0; 274 -8.1; 302 -8.2; 332 -7.7; 365 -7.2; 402 -6.6; 442 -6.0; 486 -5.4; 535 -4.8; 588 -4.0; 647 -3.0; 712 -1.8; 783 -0.9; 861 -0.5; 947 -1.1; 1042 -3.4; 1146 -5.7; 1261 -4.8; 1387 -6.6; 1526 -7.1; 1678 -7.4; 1846 -9.7; 2031 -11.7; 2234 -12.0; 2457 -11.1; 2703 -10.0; 2973 -9.0; 3270 -8.0; 3597 -6.9; 3957 -8.6; 4353 -6.7; 4788 -4.6; 5267 -2.6; 5793 -3.2; 6373 -7.2; 7010 -10.6; 7711 -12.5; 8482 -13.4; 9330 -11.9; 10263 -6.6; 11289 -2.3; 12418 -2.3; 13660 -2.3; 15026 -2.3; 16529 -4.2; 18182 -8.1; 20000 -8.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Grind GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Grind ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 55 Hz    | 0.41 | -5.3 dB  |
| Peaking | 165 Hz   | 0.94 | -3.4 dB  |
| Peaking | 324 Hz   | 1.79 | -3.8 dB  |
| Peaking | 2315 Hz  | 1.38 | -9.7 dB  |
| Peaking | 8307 Hz  | 2.5  | -12.0 dB |
| Peaking | 845 Hz   | 4.2  | 3.8 dB   |
| Peaking | 5477 Hz  | 3.5  | 7.8 dB   |
| Peaking | 5598 Hz  | 1.28 | -4.8 dB  |
| Peaking | 14372 Hz | 0.72 | 4.2 dB   |
| Peaking | 19049 Hz | 0.54 | -7.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.9 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -8.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Grind/Skullcandy%20Grind.png)