# Turtle Beach Elite Pro 2 SuperAmp
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.1; 25 -9.1; 28 -9.2; 31 -9.2; 34 -9.2; 37 -9.1; 41 -9.0; 45 -8.9; 49 -8.8; 54 -8.8; 60 -8.8; 66 -9.0; 72 -9.2; 79 -9.3; 87 -9.5; 96 -9.6; 106 -9.6; 116 -9.6; 128 -9.7; 141 -9.8; 155 -9.9; 170 -10.0; 187 -9.8; 206 -8.9; 227 -7.9; 249 -6.5; 274 -4.5; 302 -4.8; 332 -3.7; 365 -1.3; 402 -1.5; 442 -3.9; 486 -6.2; 535 -8.1; 588 -8.9; 647 -8.2; 712 -6.5; 783 -5.2; 861 -4.6; 947 -4.9; 1042 -5.7; 1146 -6.2; 1261 -6.4; 1387 -6.5; 1526 -6.4; 1678 -6.4; 1846 -6.6; 2031 -6.8; 2234 -6.3; 2457 -4.9; 2703 -4.9; 2973 -4.7; 3270 -5.0; 3597 -6.6; 3957 -8.3; 4353 -6.7; 4788 -3.1; 5267 -0.5; 5793 -0.9; 6373 -3.5; 7010 -4.6; 7711 -9.2; 8482 -14.0; 9330 -13.1; 10263 -8.5; 11289 -8.2; 12418 -10.0; 13660 -8.2; 15026 -6.5; 16529 -6.5; 18182 -7.0; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Elite Pro 2 SuperAmp GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Elite Pro 2 SuperAmp ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.23 | -2.6 dB |
| Peaking | 158 Hz   | 1.68 | -2.3 dB |
| Peaking | 370 Hz   | 3.42 | 6.4 dB  |
| Peaking | 5675 Hz  | 2.87 | 7.0 dB  |
| Peaking | 8810 Hz  | 3.22 | -9.0 dB |
| Peaking | 593 Hz   | 4.44 | -3.3 dB |
| Peaking | 863 Hz   | 3.57 | 2.3 dB  |
| Peaking | 2913 Hz  | 3.09 | 1.8 dB  |
| Peaking | 4038 Hz  | 6.73 | -3.5 dB |
| Peaking | 19972 Hz | 1.35 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Elite%20Pro%202%20SuperAmp/Turtle%20Beach%20Elite%20Pro%202%20SuperAmp.png)