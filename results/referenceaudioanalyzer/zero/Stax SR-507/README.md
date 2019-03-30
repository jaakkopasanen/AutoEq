# Stax SR-507
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.5; 45 -3.8; 49 -6.1; 54 -8.6; 60 -11.3; 66 -13.0; 72 -13.5; 79 -12.8; 87 -11.3; 96 -9.8; 106 -8.6; 116 -7.6; 128 -6.8; 141 -6.1; 155 -5.6; 170 -5.1; 187 -4.8; 206 -4.5; 227 -4.3; 249 -4.0; 274 -3.8; 302 -4.2; 332 -4.9; 365 -5.2; 402 -4.9; 442 -4.8; 486 -4.9; 535 -4.7; 588 -4.5; 647 -4.5; 712 -4.8; 783 -5.0; 861 -5.3; 947 -5.8; 1042 -6.2; 1146 -6.8; 1261 -7.3; 1387 -8.1; 1526 -9.1; 1678 -9.6; 1846 -9.6; 2031 -8.9; 2234 -7.4; 2457 -6.0; 2703 -5.2; 2973 -4.6; 3270 -4.0; 3597 -4.0; 3957 -5.6; 4353 -7.5; 4788 -8.7; 5267 -8.5; 5793 -9.5; 6373 -12.2; 7010 -13.6; 7711 -11.9; 8482 -8.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-507 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-507 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 0.64 | 8.6 dB   |
| Peaking | 69 Hz   | 1.27 | -13.0 dB |
| Peaking | 860 Hz  | 0.06 | 2.5 dB   |
| Peaking | 1646 Hz | 1.63 | -5.7 dB  |
| Peaking | 6833 Hz | 2.17 | -9.0 dB  |
| Peaking | 251 Hz  | 1.44 | 2.8 dB   |
| Peaking | 276 Hz  | 0.88 | -2.2 dB  |
| Peaking | 2062 Hz | 4.99 | -1.3 dB  |
| Peaking | 3782 Hz | 1.44 | 2.6 dB   |
| Peaking | 4522 Hz | 3.43 | -3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 10.2 dB |
| Peaking | 62 Hz    | 1.41 | -8.4 dB |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | 2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Stax%20SR-507/Stax%20SR-507.png)