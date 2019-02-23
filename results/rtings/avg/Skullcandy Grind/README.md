# Skullcandy Grind
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.9; 25 -5.3; 28 -5.9; 31 -6.3; 34 -6.5; 37 -6.7; 41 -6.8; 45 -6.9; 49 -7.0; 54 -7.1; 60 -7.3; 66 -7.5; 72 -7.6; 79 -7.7; 87 -7.7; 96 -7.8; 106 -7.9; 116 -7.9; 128 -7.9; 141 -7.8; 155 -7.7; 170 -7.7; 187 -7.6; 206 -7.5; 227 -7.4; 249 -7.3; 274 -7.4; 302 -7.6; 332 -7.0; 365 -6.5; 402 -5.9; 442 -5.3; 486 -4.8; 535 -4.1; 588 -3.4; 647 -2.3; 712 -1.2; 783 -0.5; 861 -0.5; 947 -0.6; 1042 -2.7; 1146 -5.0; 1261 -4.1; 1387 -5.9; 1526 -6.4; 1678 -6.7; 1846 -9.0; 2031 -11.0; 2234 -11.3; 2457 -10.5; 2703 -9.4; 2973 -8.4; 3270 -7.3; 3597 -6.3; 3957 -7.9; 4353 -6.1; 4788 -3.9; 5267 -2.0; 5793 -2.5; 6373 -6.6; 7010 -9.9; 7711 -11.9; 8482 -12.8; 9330 -11.3; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.5; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Grind GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Grind ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 3.14 | 2.0 dB  |
| Peaking | 827 Hz   | 1.74 | 6.8 dB  |
| Peaking | 2230 Hz  | 2.36 | -5.5 dB |
| Peaking | 5448 Hz  | 3.83 | 6.4 dB  |
| Peaking | 8149 Hz  | 2.63 | -7.1 dB |
| Peaking | 13 Hz    | 1.51 | -1.2 dB |
| Peaking | 115 Hz   | 0.73 | -1.5 dB |
| Peaking | 293 Hz   | 4.12 | -1.1 dB |
| Peaking | 9332 Hz  | 6.59 | -2.5 dB |
| Peaking | 10353 Hz | 2.93 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Grind/Skullcandy%20Grind.png)