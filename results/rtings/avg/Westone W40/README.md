# Westone W40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.9; 60 -1.7; 66 -2.5; 72 -3.1; 79 -3.9; 87 -4.7; 96 -5.6; 106 -6.6; 116 -7.5; 128 -8.3; 141 -9.1; 155 -9.7; 170 -10.3; 187 -10.9; 206 -11.3; 227 -11.4; 249 -11.4; 274 -11.3; 302 -11.1; 332 -11.0; 365 -10.9; 402 -10.6; 442 -10.2; 486 -9.6; 535 -8.8; 588 -8.1; 647 -7.3; 712 -6.7; 783 -6.3; 861 -6.2; 947 -6.5; 1042 -7.2; 1146 -7.8; 1261 -8.0; 1387 -7.8; 1526 -7.4; 1678 -6.7; 1846 -5.9; 2031 -4.9; 2234 -3.1; 2457 -1.5; 2703 -1.0; 2973 -1.7; 3270 -2.7; 3597 -2.9; 3957 -2.6; 4353 -1.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.5; 9330 -13.2; 10263 -12.7; 11289 -8.4; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -7.5; 18182 -7.3; 20000 -7.8
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
| Peaking | 37 Hz   |  0.4  | 7.0 dB  |
| Peaking | 215 Hz  |  0.57 | -6.3 dB |
| Peaking | 2645 Hz |  3.11 | 5.0 dB  |
| Peaking | 5469 Hz |  1.37 | 6.8 dB  |
| Peaking | 9627 Hz |  3.1  | -9.1 dB |
| Peaking | 13 Hz   |  2.49 | 0.9 dB  |
| Peaking | 469 Hz  |  1.4  | -2.0 dB |
| Peaking | 914 Hz  |  0.65 | 3.5 dB  |
| Peaking | 1275 Hz |  1.39 | -4.2 dB |
| Peaking | 7361 Hz | 12.06 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Westone%20W40/Westone%20W40.png)