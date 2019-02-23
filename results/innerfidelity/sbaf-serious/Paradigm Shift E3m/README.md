# Paradigm Shift E3m
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.2; 23 -12.2; 25 -12.2; 28 -12.3; 31 -12.4; 34 -12.5; 37 -12.6; 41 -12.7; 45 -12.9; 49 -13.1; 54 -13.3; 60 -13.5; 66 -13.8; 72 -14.1; 79 -14.5; 87 -14.9; 96 -15.2; 106 -15.4; 116 -15.7; 128 -15.9; 141 -16.1; 155 -16.2; 170 -16.2; 187 -16.1; 206 -16.1; 227 -15.8; 249 -15.6; 274 -15.2; 302 -14.8; 332 -14.3; 365 -13.7; 402 -13.0; 442 -12.2; 486 -11.4; 535 -10.5; 588 -9.3; 647 -8.3; 712 -7.3; 783 -6.2; 861 -5.5; 947 -4.9; 1042 -4.2; 1146 -3.9; 1261 -3.8; 1387 -4.2; 1526 -5.1; 1678 -3.5; 1846 -3.5; 2031 -2.6; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.8; 5267 -1.4; 5793 -2.7; 6373 -2.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Paradigm Shift E3m GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Paradigm Shift E3m ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  0.36 | -4.9 dB |
| Peaking | 105 Hz  |  0.57 | -3.5 dB |
| Peaking | 256 Hz  |  0.43 | -7.6 dB |
| Peaking | 926 Hz  |  1.15 | 3.5 dB  |
| Peaking | 3357 Hz |  0.79 | 6.8 dB  |
| Peaking | 1533 Hz | 10.18 | -1.3 dB |
| Peaking | 2335 Hz |  6.28 | 1.2 dB  |
| Peaking | 3373 Hz |  3.2  | -1.1 dB |
| Peaking | 6608 Hz |  1.3  | 3.0 dB  |
| Peaking | 7967 Hz |  1.46 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -7.6 dB |
| Peaking | 250 Hz   | 1.41 | -8.0 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Paradigm%20Shift%20E3m/Paradigm%20Shift%20E3m.png)