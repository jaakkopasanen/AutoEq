# Turtle Beach Elite Pro 2 SuperAmp
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -8.8; 25 -8.9; 28 -8.9; 31 -9.0; 34 -8.9; 37 -8.9; 41 -8.7; 45 -8.7; 49 -8.6; 54 -8.6; 60 -8.6; 66 -8.8; 72 -8.9; 79 -9.0; 87 -9.2; 96 -9.3; 106 -9.3; 116 -9.3; 128 -9.4; 141 -9.6; 155 -9.7; 170 -9.7; 187 -9.6; 206 -8.7; 227 -7.7; 249 -6.3; 274 -4.6; 302 -4.7; 332 -3.5; 365 -1.2; 402 -1.4; 442 -3.8; 486 -6.2; 535 -8.1; 588 -8.9; 647 -8.3; 712 -6.5; 783 -5.3; 861 -4.6; 947 -5.0; 1042 -5.8; 1146 -6.2; 1261 -6.6; 1387 -6.6; 1526 -6.5; 1678 -6.6; 1846 -6.9; 2031 -7.3; 2234 -7.1; 2457 -5.9; 2703 -5.4; 2973 -4.9; 3270 -4.8; 3597 -6.3; 3957 -7.8; 4353 -6.4; 4788 -3.3; 5267 -0.5; 5793 -0.7; 6373 -2.4; 7010 -4.6; 7711 -10.0; 8482 -13.6; 9330 -11.3; 10263 -7.9; 11289 -9.2; 12418 -10.2; 13660 -7.4; 15026 -6.4; 16529 -6.4; 18182 -6.8; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Elite Pro 2 SuperAmp GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Elite Pro 2 SuperAmp ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 104 Hz   | 0.2  | -3.0 dB  |
| Peaking | 364 Hz   | 2.48 | 7.6 dB   |
| Peaking | 4082 Hz  | 4.63 | -4.9 dB  |
| Peaking | 6189 Hz  | 1.21 | 11.5 dB  |
| Peaking | 8257 Hz  | 1.54 | -12.5 dB |
| Peaking | 421 Hz   | 5.6  | 1.4 dB   |
| Peaking | 585 Hz   | 3.07 | -2.9 dB  |
| Peaking | 848 Hz   | 3.05 | 2.8 dB   |
| Peaking | 2055 Hz  | 4.94 | -1.5 dB  |
| Peaking | 22049 Hz | 2.2  | 0.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Elite%20Pro%202%20SuperAmp/Turtle%20Beach%20Elite%20Pro%202%20SuperAmp.png)