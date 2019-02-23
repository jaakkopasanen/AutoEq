# Yamaha Pro300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.6; 87 -0.8; 96 -1.5; 106 -2.4; 116 -1.7; 128 -2.4; 141 -3.0; 155 -3.5; 170 -3.6; 187 -4.2; 206 -4.7; 227 -5.0; 249 -4.7; 274 -4.6; 302 -5.2; 332 -5.6; 365 -6.4; 402 -6.9; 442 -7.5; 486 -8.4; 535 -8.5; 588 -7.0; 647 -7.2; 712 -8.1; 783 -8.3; 861 -8.9; 947 -9.5; 1042 -10.3; 1146 -11.0; 1261 -11.9; 1387 -13.5; 1526 -14.3; 1678 -15.4; 1846 -15.4; 2031 -13.8; 2234 -11.2; 2457 -8.5; 2703 -6.3; 2973 -4.4; 3270 -3.3; 3597 -1.1; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.1; 5793 -6.2; 6373 -6.2; 7010 -6.9; 7711 -7.9; 8482 -8.0; 9330 -8.2; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha Pro300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha Pro300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.14 | 6.0 dB  |
| Peaking | 77 Hz   | 1.37 | 1.1 dB  |
| Peaking | 492 Hz  | 4.13 | -2.1 dB |
| Peaking | 1695 Hz | 1.31 | -9.9 dB |
| Peaking | 3925 Hz | 1.71 | 8.3 dB  |
| Peaking | 2043 Hz | 5.32 | -1.2 dB |
| Peaking | 2786 Hz | 2.23 | 1.8 dB  |
| Peaking | 3579 Hz | 1.76 | -1.1 dB |
| Peaking | 5057 Hz | 6.49 | 3.7 dB  |
| Peaking | 7795 Hz | 1.47 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | 3.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -9.3 dB |
| Peaking | 4000 Hz  | 1.41 | 9.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20Pro300/Yamaha%20Pro300.png)