# Paradigm Shift E1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.5; 25 -12.5; 28 -12.7; 31 -12.8; 34 -12.9; 37 -12.9; 41 -13.0; 45 -13.1; 49 -13.2; 54 -13.4; 60 -13.7; 66 -13.9; 72 -14.2; 79 -14.5; 87 -14.8; 96 -15.2; 106 -15.3; 116 -15.4; 128 -15.6; 141 -15.7; 155 -15.7; 170 -15.6; 187 -15.4; 206 -15.2; 227 -14.8; 249 -14.5; 274 -14.0; 302 -13.4; 332 -12.8; 365 -12.1; 402 -11.4; 442 -10.4; 486 -9.8; 535 -9.0; 588 -8.1; 647 -7.4; 712 -7.1; 783 -6.4; 861 -6.4; 947 -6.4; 1042 -6.5; 1146 -6.1; 1261 -5.0; 1387 -4.8; 1526 -4.2; 1678 -3.9; 1846 -2.7; 2031 -1.1; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.2; 5267 -1.9; 5793 -2.5; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Paradigm Shift E1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Paradigm Shift E1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.21 | -5.6 dB |
| Peaking | 129 Hz  | 0.7  | -4.5 dB |
| Peaking | 270 Hz  | 0.8  | -4.8 dB |
| Peaking | 3185 Hz | 0.71 | 6.8 dB  |
| Peaking | 2201 Hz | 3.15 | 2.5 dB  |
| Peaking | 2358 Hz | 1.02 | -1.3 dB |
| Peaking | 4781 Hz | 2.47 | 1.7 dB  |
| Peaking | 6453 Hz | 4.92 | 4.2 dB  |
| Peaking | 7280 Hz | 1.2  | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB |
| Peaking | 62 Hz    | 1.41 | -5.1 dB |
| Peaking | 125 Hz   | 1.41 | -7.6 dB |
| Peaking | 250 Hz   | 1.41 | -7.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Paradigm%20Shift%20E1/Paradigm%20Shift%20E1.png)