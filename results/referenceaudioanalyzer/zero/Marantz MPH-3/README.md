# Marantz MPH-3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -3.4; 25 -4.2; 28 -5.1; 31 -5.9; 34 -6.5; 37 -7.0; 41 -7.6; 45 -8.1; 49 -8.5; 54 -9.0; 60 -9.3; 66 -9.3; 72 -9.3; 79 -9.4; 87 -9.8; 96 -10.2; 106 -10.8; 116 -11.2; 128 -11.6; 141 -11.8; 155 -12.0; 170 -12.2; 187 -12.4; 206 -12.5; 227 -12.2; 249 -12.2; 274 -12.2; 302 -12.2; 332 -12.0; 365 -11.7; 402 -11.2; 442 -10.7; 486 -10.4; 535 -10.1; 588 -10.0; 647 -9.8; 712 -9.6; 783 -9.4; 861 -8.9; 947 -8.0; 1042 -7.3; 1146 -6.7; 1261 -5.7; 1387 -4.4; 1526 -3.0; 1678 -1.7; 1846 -0.6; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -1.7; 2973 -2.8; 3270 -2.5; 3597 -2.0; 3957 -4.0; 4353 -4.9; 4788 -1.8; 5267 -0.5; 5793 -0.5; 6373 -2.0; 7010 -5.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marantz MPH-3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marantz MPH-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 21 Hz   |  1.72 | 4.5 dB  |
| Peaking | 233 Hz  |  0.31 | -5.8 dB |
| Peaking | 1866 Hz |  1.67 | 5.3 dB  |
| Peaking | 2733 Hz |  1.33 | 3.3 dB  |
| Peaking | 5577 Hz |  3.37 | 6.1 dB  |
| Peaking | 54 Hz   |  3.4  | -0.5 dB |
| Peaking | 493 Hz  |  3.3  | 0.6 dB  |
| Peaking | 796 Hz  |  4.01 | -0.6 dB |
| Peaking | 6225 Hz | 11.25 | 1.9 dB  |
| Peaking | 7724 Hz |  1.87 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Marantz%20MPH-3/Marantz%20MPH-3.png)