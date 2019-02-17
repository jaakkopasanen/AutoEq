# Fiio FH1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.6; 23 -13.2; 25 -13.5; 28 -13.2; 31 -13.0; 34 -13.1; 37 -13.0; 41 -13.0; 45 -13.0; 49 -13.0; 54 -13.3; 60 -13.3; 66 -13.7; 72 -13.6; 79 -13.8; 87 -13.9; 96 -13.4; 106 -13.6; 116 -13.3; 128 -13.3; 141 -12.9; 155 -12.7; 170 -12.5; 187 -12.2; 206 -11.9; 227 -11.4; 249 -11.0; 274 -10.5; 302 -10.0; 332 -9.6; 365 -9.1; 402 -8.6; 442 -8.1; 486 -7.7; 535 -7.2; 588 -6.7; 647 -6.3; 712 -5.8; 783 -5.4; 861 -5.2; 947 -5.3; 1042 -6.1; 1146 -7.1; 1261 -8.2; 1387 -9.0; 1526 -9.5; 1678 -9.7; 1846 -9.7; 2031 -9.5; 2234 -8.7; 2457 -7.4; 2703 -6.2; 2973 -5.4; 3270 -5.0; 3597 -4.1; 3957 -1.1; 4353 -0.5; 4788 -4.3; 5267 -2.2; 5793 -0.5; 6373 -0.5; 7010 -3.2; 7711 -8.9; 8482 -12.3; 9330 -9.3; 10263 -5.8; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.9; 18182 -8.2; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fiio FH1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fiio FH1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 0.22 | -8.3 dB |
| Peaking | 1793 Hz | 2.08 | -4.5 dB |
| Peaking | 4118 Hz | 5.92 | 5.6 dB  |
| Peaking | 6257 Hz | 2.63 | 6.7 dB  |
| Peaking | 8373 Hz | 3.91 | -8.7 dB |
| Peaking | 23 Hz   | 1.69 | -1.2 dB |
| Peaking | 43 Hz   | 1.28 | 1.0 dB  |
| Peaking | 223 Hz  | 0.84 | -0.6 dB |
| Peaking | 871 Hz  | 1.39 | 2.0 dB  |
| Peaking | 1298 Hz | 3.26 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Fiio%20FH1/Fiio%20FH1.png)