# Westone 4R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.6; 25 -4.1; 28 -4.7; 31 -5.2; 34 -5.7; 37 -6.1; 41 -6.5; 45 -6.9; 49 -7.3; 54 -7.7; 60 -8.2; 66 -8.7; 72 -9.2; 79 -9.6; 87 -10.2; 96 -10.7; 106 -10.9; 116 -11.3; 128 -11.6; 141 -11.9; 155 -12.0; 170 -12.2; 187 -12.3; 206 -12.3; 227 -12.2; 249 -12.1; 274 -12.0; 302 -11.7; 332 -11.5; 365 -11.1; 402 -10.7; 442 -10.2; 486 -9.8; 535 -9.3; 588 -8.4; 647 -7.7; 712 -7.2; 783 -6.4; 861 -6.1; 947 -6.0; 1042 -6.2; 1146 -6.5; 1261 -6.7; 1387 -7.1; 1526 -7.2; 1678 -6.9; 1846 -6.1; 2031 -5.0; 2234 -4.1; 2457 -2.8; 2703 -2.0; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.9; 9330 -12.2; 10263 -13.5; 11289 -8.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone 4R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone 4R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.86 | 4.1 dB  |
| Peaking | 143 Hz  | 0.58 | -4.8 dB |
| Peaking | 326 Hz  | 0.93 | -3.0 dB |
| Peaking | 4553 Hz | 0.8  | 7.1 dB  |
| Peaking | 9909 Hz | 2.99 | -9.6 dB |
| Peaking | 876 Hz  | 2.95 | 1.3 dB  |
| Peaking | 1592 Hz | 2.3  | -1.9 dB |
| Peaking | 2911 Hz | 2.88 | 1.8 dB  |
| Peaking | 5930 Hz | 1.47 | -2.1 dB |
| Peaking | 6175 Hz | 3.93 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%204R/Westone%204R.png)