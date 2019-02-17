# Turtle Beach Elite Pro 2 SuperAmp
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -9.9; 25 -10.0; 28 -10.0; 31 -10.1; 34 -10.0; 37 -9.9; 41 -9.8; 45 -9.7; 49 -9.7; 54 -9.6; 60 -9.7; 66 -9.9; 72 -10.0; 79 -10.2; 87 -10.3; 96 -10.4; 106 -10.5; 116 -10.5; 128 -10.5; 141 -10.7; 155 -10.8; 170 -10.8; 187 -10.6; 206 -9.7; 227 -8.7; 249 -7.4; 274 -5.4; 302 -5.7; 332 -4.5; 365 -2.1; 402 -2.3; 442 -4.7; 486 -7.1; 535 -8.9; 588 -9.7; 647 -9.1; 712 -7.3; 783 -6.1; 861 -5.4; 947 -5.7; 1042 -6.6; 1146 -7.0; 1261 -7.3; 1387 -7.4; 1526 -7.2; 1678 -7.3; 1846 -7.5; 2031 -7.7; 2234 -7.2; 2457 -5.7; 2703 -5.7; 2973 -5.6; 3270 -5.8; 3597 -7.4; 3957 -9.1; 4353 -7.5; 4788 -3.9; 5267 -0.5; 5793 -1.5; 6373 -4.3; 7010 -5.4; 7711 -10.1; 8482 -14.9; 9330 -13.9; 10263 -9.3; 11289 -9.0; 12418 -10.8; 13660 -9.1; 15026 -6.4; 16529 -6.3; 18182 -7.7; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Elite Pro 2 SuperAmp GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Elite Pro 2 SuperAmp ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.84 | -2.9 dB |
| Peaking | 181 Hz   | 0.29 | -4.6 dB |
| Peaking | 358 Hz   | 2.07 | 8.0 dB  |
| Peaking | 5612 Hz  | 3.87 | 7.4 dB  |
| Peaking | 8902 Hz  | 2.54 | -9.2 dB |
| Peaking | 415 Hz   | 6.51 | 1.6 dB  |
| Peaking | 592 Hz   | 3.03 | -3.0 dB |
| Peaking | 846 Hz   | 2.47 | 2.9 dB  |
| Peaking | 1559 Hz  | 1.26 | -0.8 dB |
| Peaking | 20122 Hz | 1.12 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Elite%20Pro%202%20SuperAmp/Turtle%20Beach%20Elite%20Pro%202%20SuperAmp.png)