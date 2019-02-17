# Paradigm Shift E3m
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.1; 23 -14.1; 25 -14.1; 28 -14.2; 31 -14.3; 34 -14.4; 37 -14.5; 41 -14.6; 45 -14.8; 49 -15.0; 54 -15.2; 60 -15.4; 66 -15.7; 72 -16.0; 79 -16.4; 87 -16.8; 96 -17.1; 106 -17.3; 116 -17.6; 128 -17.8; 141 -18.0; 155 -18.1; 170 -18.1; 187 -18.0; 206 -18.0; 227 -17.7; 249 -17.5; 274 -17.1; 302 -16.7; 332 -16.2; 365 -15.6; 402 -14.9; 442 -14.1; 486 -13.3; 535 -12.4; 588 -11.2; 647 -10.2; 712 -9.2; 783 -8.1; 861 -7.4; 947 -6.8; 1042 -6.1; 1146 -5.8; 1261 -5.7; 1387 -6.1; 1526 -7.0; 1678 -5.4; 1846 -5.4; 2031 -4.5; 2234 -2.8; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.0; 4788 -2.7; 5267 -3.3; 5793 -4.6; 6373 -4.7; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Paradigm Shift E3m GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Paradigm Shift E3m ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.16 | -7.2 dB |
| Peaking | 171 Hz   | 0.59 | -6.1 dB |
| Peaking | 376 Hz   | 0.89 | -4.8 dB |
| Peaking | 1855 Hz  | 1.7  | -4.8 dB |
| Peaking | 2642 Hz  | 0.75 | 8.3 dB  |
| Peaking | 1021 Hz  | 3.54 | 0.6 dB  |
| Peaking | 3976 Hz  | 1.47 | -0.9 dB |
| Peaking | 4129 Hz  | 3.85 | 2.2 dB  |
| Peaking | 8292 Hz  | 5.51 | -1.0 dB |
| Peaking | 10330 Hz | 1.76 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.3 dB |
| Peaking | 125 Hz   | 1.41 | -9.0 dB |
| Peaking | 250 Hz   | 1.41 | -9.5 dB |
| Peaking | 500 Hz   | 1.41 | -5.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Paradigm%20Shift%20E3m/Paradigm%20Shift%20E3m.png)