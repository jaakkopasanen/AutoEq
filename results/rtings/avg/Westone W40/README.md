# Westone W40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -1.3; 66 -2.1; 72 -2.7; 79 -3.5; 87 -4.3; 96 -5.2; 106 -6.2; 116 -7.1; 128 -7.9; 141 -8.7; 155 -9.4; 170 -9.9; 187 -10.5; 206 -10.9; 227 -11.0; 249 -11.0; 274 -10.9; 302 -10.7; 332 -10.6; 365 -10.5; 402 -10.2; 442 -9.8; 486 -9.2; 535 -8.4; 588 -7.7; 647 -6.9; 712 -6.3; 783 -5.9; 861 -5.8; 947 -6.1; 1042 -6.8; 1146 -7.4; 1261 -7.6; 1387 -7.4; 1526 -7.0; 1678 -6.3; 1846 -5.5; 2031 -4.5; 2234 -2.7; 2457 -1.1; 2703 -0.6; 2973 -1.4; 3270 -2.3; 3597 -2.5; 3957 -2.2; 4353 -1.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.1; 9330 -12.8; 10263 -12.3; 11289 -8.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.1; 18182 -6.9; 20000 -7.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 38 Hz   |  0.4  | 6.9 dB  |
| Peaking | 214 Hz  |  0.63 | -5.9 dB |
| Peaking | 2637 Hz |  2.88 | 5.2 dB  |
| Peaking | 5405 Hz |  1.29 | 6.6 dB  |
| Peaking | 9631 Hz |  3.13 | -8.7 dB |
| Peaking | 16 Hz   |  2.42 | 1.1 dB  |
| Peaking | 469 Hz  |  1.38 | -2.3 dB |
| Peaking | 866 Hz  |  0.67 | 3.4 dB  |
| Peaking | 1271 Hz |  1.44 | -3.7 dB |
| Peaking | 7406 Hz | 12.69 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Westone%20W40/Westone%20W40.png)