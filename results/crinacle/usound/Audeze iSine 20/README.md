# Audeze iSine 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.2; 25 -1.3; 28 -1.4; 31 -1.5; 34 -1.7; 37 -1.8; 41 -1.9; 45 -2.1; 49 -2.3; 54 -2.5; 60 -2.8; 66 -3.2; 72 -3.6; 79 -3.9; 87 -4.4; 96 -5.0; 106 -5.4; 116 -5.8; 128 -6.3; 141 -6.7; 155 -7.0; 170 -7.3; 187 -7.6; 206 -7.9; 227 -8.1; 249 -8.3; 274 -8.5; 302 -8.7; 332 -8.9; 365 -9.1; 402 -9.5; 442 -9.7; 486 -10.0; 535 -10.4; 588 -10.9; 647 -11.4; 712 -12.0; 783 -12.8; 861 -13.3; 947 -12.8; 1042 -12.2; 1146 -12.5; 1261 -13.2; 1387 -13.9; 1526 -13.3; 1678 -11.4; 1846 -8.3; 2031 -4.4; 2234 -2.1; 2457 -0.9; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.3; 7010 -4.8; 7711 -6.2; 8482 -7.5; 9330 -8.8; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.8; 15026 -7.3; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze iSine 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.73 | 5.1 dB  |
| Peaking | 60 Hz    | 1.27 | 2.4 dB  |
| Peaking | 904 Hz   | 0.56 | -7.1 dB |
| Peaking | 1514 Hz  | 2.29 | -7.1 dB |
| Peaking | 2845 Hz  | 0.69 | 9.4 dB  |
| Peaking | 2249 Hz  | 5.55 | 1.1 dB  |
| Peaking | 3188 Hz  | 3.07 | -1.1 dB |
| Peaking | 5667 Hz  | 2.93 | 3.2 dB  |
| Peaking | 8910 Hz  | 2.25 | -3.6 dB |
| Peaking | 14445 Hz | 5.61 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -8.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Audeze%20iSine%2020/Audeze%20iSine%2020.png)