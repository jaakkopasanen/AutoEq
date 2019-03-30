# AKG Y30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.1; 72 -1.4; 79 -1.7; 87 -2.1; 96 -2.4; 106 -2.7; 116 -3.0; 128 -3.4; 141 -3.7; 155 -3.8; 170 -4.2; 187 -4.3; 206 -4.3; 227 -4.3; 249 -4.3; 274 -4.3; 302 -4.3; 332 -4.3; 365 -4.3; 402 -4.2; 442 -4.2; 486 -4.3; 535 -4.3; 588 -4.3; 647 -4.3; 712 -4.3; 783 -4.5; 861 -4.7; 947 -4.9; 1042 -5.2; 1146 -5.7; 1261 -6.1; 1387 -6.8; 1526 -7.5; 1678 -8.3; 1846 -9.3; 2031 -10.7; 2234 -12.2; 2457 -13.8; 2703 -15.0; 2973 -15.3; 3270 -13.9; 3597 -11.2; 3957 -8.4; 4353 -6.2; 4788 -5.6; 5267 -8.2; 5793 -11.1; 6373 -11.8; 7010 -10.1; 7711 -6.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -7.8; 13660 -6.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Y30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Y30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.31 | 6.2 dB  |
| Peaking | 592 Hz   | 0.62 | 2.3 dB  |
| Peaking | 2724 Hz  | 1.99 | -9.6 dB |
| Peaking | 6344 Hz  | 5.35 | -5.5 dB |
| Peaking | 22050 Hz | 1.95 | 0.5 dB  |
| Peaking | 3351 Hz  | 5.98 | -2.0 dB |
| Peaking | 3829 Hz  | 2.68 | -0.3 dB |
| Peaking | 4622 Hz  | 3.16 | 3.6 dB  |
| Peaking | 5644 Hz  | 6.33 | -2.5 dB |
| Peaking | 21028 Hz | 1.29 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 2.0 dB  |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | -3.0 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20Y30/AKG%20Y30.png)