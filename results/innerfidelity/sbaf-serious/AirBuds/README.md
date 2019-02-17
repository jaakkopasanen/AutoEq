# AirBuds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -8.3; 25 -8.8; 28 -9.0; 31 -9.1; 34 -9.6; 37 -10.1; 41 -10.6; 45 -10.9; 49 -11.4; 54 -11.8; 60 -12.4; 66 -12.9; 72 -13.4; 79 -13.9; 87 -14.4; 96 -14.9; 106 -15.3; 116 -15.5; 128 -15.9; 141 -16.1; 155 -16.3; 170 -16.4; 187 -16.4; 206 -16.3; 227 -16.1; 249 -16.0; 274 -15.7; 302 -15.3; 332 -14.9; 365 -14.4; 402 -13.9; 442 -13.1; 486 -12.6; 535 -11.9; 588 -10.9; 647 -10.1; 712 -9.4; 783 -8.3; 861 -7.5; 947 -6.9; 1042 -6.3; 1146 -3.6; 1261 -3.1; 1387 -1.1; 1526 -0.5; 1678 -0.7; 1846 -3.4; 2031 -4.6; 2234 -3.4; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.8; 4353 -4.6; 4788 -8.2; 5267 -11.0; 5793 -10.7; 6373 -7.1; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AirBuds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AirBuds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 87 Hz   |  0.46 | -4.7 dB |
| Peaking | 256 Hz  |  0.46 | -7.7 dB |
| Peaking | 1430 Hz |  2.21 | 6.1 dB  |
| Peaking | 3434 Hz |  1.18 | 7.2 dB  |
| Peaking | 5287 Hz |  3.51 | -8.6 dB |
| Peaking | 875 Hz  |  3.26 | 0.7 dB  |
| Peaking | 1691 Hz |  5.18 | 2.8 dB  |
| Peaking | 2063 Hz |  1.79 | -3.1 dB |
| Peaking | 2485 Hz |  4.16 | 3.1 dB  |
| Peaking | 6892 Hz | 11.47 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -7.7 dB |
| Peaking | 250 Hz   | 1.41 | -8.0 dB |
| Peaking | 500 Hz   | 1.41 | -5.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AirBuds/AirBuds.png)