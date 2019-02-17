# Westone W40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.2; 25 -3.7; 28 -4.4; 31 -4.9; 34 -5.4; 37 -5.8; 41 -6.3; 45 -6.7; 49 -7.1; 54 -7.5; 60 -8.1; 66 -8.5; 72 -9.0; 79 -9.5; 87 -10.0; 96 -10.6; 106 -11.0; 116 -11.2; 128 -11.6; 141 -11.9; 155 -12.0; 170 -12.2; 187 -12.3; 206 -12.3; 227 -12.2; 249 -12.2; 274 -12.0; 302 -11.9; 332 -11.6; 365 -11.3; 402 -11.0; 442 -10.4; 486 -10.1; 535 -9.6; 588 -8.8; 647 -8.2; 712 -7.7; 783 -7.0; 861 -6.7; 947 -6.5; 1042 -6.5; 1146 -6.5; 1261 -6.6; 1387 -6.9; 1526 -6.9; 1678 -6.6; 1846 -5.7; 2031 -4.6; 2234 -3.3; 2457 -2.0; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.8; 9330 -10.4; 10263 -9.7; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.88 | 4.6 dB  |
| Peaking | 103 Hz  | 0.86 | -1.8 dB |
| Peaking | 244 Hz  | 0.52 | -5.5 dB |
| Peaking | 4422 Hz | 0.71 | 7.1 dB  |
| Peaking | 9363 Hz | 2.5  | -6.5 dB |
| Peaking | 874 Hz  | 2.49 | 1.0 dB  |
| Peaking | 1640 Hz | 2.29 | -1.8 dB |
| Peaking | 2832 Hz | 1.96 | 2.6 dB  |
| Peaking | 3740 Hz | 0.81 | -1.4 dB |
| Peaking | 6079 Hz | 5.15 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W40/Westone%20W40.png)