# JVC HA-SR500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -1.0; 365 -1.8; 402 -2.8; 442 -3.8; 486 -5.0; 535 -6.2; 588 -7.2; 647 -8.2; 712 -9.2; 783 -10.1; 861 -10.7; 947 -11.0; 1042 -11.0; 1146 -11.0; 1261 -10.5; 1387 -10.5; 1526 -11.6; 1678 -12.6; 1846 -12.7; 2031 -12.3; 2234 -11.4; 2457 -11.4; 2703 -13.4; 2973 -14.2; 3270 -12.7; 3597 -10.0; 3957 -8.0; 4353 -7.1; 4788 -6.8; 5267 -7.0; 5793 -8.8; 6373 -11.4; 7010 -12.6; 7711 -13.3; 8482 -13.1; 9330 -11.2; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-SR500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-SR500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 344 Hz   | 0.03 | 6.5 dB   |
| Peaking | 823 Hz   | 1.04 | -8.6 dB  |
| Peaking | 1795 Hz  | 1.1  | -8.9 dB  |
| Peaking | 3032 Hz  | 2.53 | -8.7 dB  |
| Peaking | 7659 Hz  | 1.43 | -11.1 dB |
| Peaking | 15 Hz    | 2.13 | 0.6 dB   |
| Peaking | 308 Hz   | 1.13 | 3.8 dB   |
| Peaking | 336 Hz   | 0.65 | -2.8 dB  |
| Peaking | 772 Hz   | 3.49 | 1.1 dB   |
| Peaking | 15840 Hz | 2.39 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 4.3 dB  |
| Peaking | 250 Hz   | 1.41 | 6.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.2 dB |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JVC%20HA-SR500/JVC%20HA-SR500.png)