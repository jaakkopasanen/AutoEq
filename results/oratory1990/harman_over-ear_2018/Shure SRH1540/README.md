# Shure SRH1540
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.2; 25 -1.7; 28 -2.2; 31 -2.6; 34 -3.0; 37 -3.5; 41 -4.2; 45 -4.7; 49 -4.9; 54 -5.6; 60 -7.0; 66 -8.0; 72 -8.5; 79 -8.6; 87 -8.7; 96 -8.4; 106 -7.9; 116 -7.5; 128 -7.4; 141 -7.1; 155 -6.5; 170 -5.8; 187 -5.5; 206 -5.1; 227 -4.6; 249 -4.2; 274 -3.8; 302 -4.2; 332 -4.5; 365 -4.0; 402 -3.5; 442 -3.3; 486 -3.1; 535 -2.8; 588 -2.5; 647 -2.3; 712 -2.5; 783 -2.6; 861 -2.8; 947 -2.6; 1042 -3.0; 1146 -3.3; 1261 -3.4; 1387 -3.6; 1526 -4.2; 1678 -4.9; 1846 -5.7; 2031 -6.6; 2234 -7.1; 2457 -7.5; 2703 -7.9; 2973 -8.0; 3270 -7.3; 3597 -5.7; 3957 -3.3; 4353 -2.6; 4788 -2.7; 5267 -1.6; 5793 -0.8; 6373 -0.5; 7010 -2.2; 7711 -4.1; 8482 -4.3; 9330 -4.3; 10263 -6.5; 11289 -8.2; 12418 -4.9; 13660 -4.3; 15026 -4.8; 16529 -9.0; 18182 -7.6; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1540 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.62 | 4.4 dB  |
| Peaking | 84 Hz    | 1.1  | -5.0 dB |
| Peaking | 2790 Hz  | 2.23 | -4.6 dB |
| Peaking | 5828 Hz  | 1.52 | 4.8 dB  |
| Peaking | 15806 Hz | 0.31 | -2.5 dB |
| Peaking | 743 Hz   | 0.88 | 2.1 dB  |
| Peaking | 2018 Hz  | 3.91 | -1.4 dB |
| Peaking | 11116 Hz | 4.67 | -4.0 dB |
| Peaking | 14101 Hz | 1.32 | 3.3 dB  |
| Peaking | 16905 Hz | 2.35 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Shure%20SRH1540/Shure%20SRH1540.png)