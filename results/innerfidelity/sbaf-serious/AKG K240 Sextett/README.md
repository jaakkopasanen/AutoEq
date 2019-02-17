# AKG K240 Sextett
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.6; 41 -2.9; 45 -4.0; 49 -4.9; 54 -5.9; 60 -6.2; 66 -5.9; 72 -7.2; 79 -9.9; 87 -11.6; 96 -12.6; 106 -13.1; 116 -13.4; 128 -13.4; 141 -13.1; 155 -12.8; 170 -11.2; 187 -11.5; 206 -12.0; 227 -11.6; 249 -11.2; 274 -10.7; 302 -10.3; 332 -9.9; 365 -9.3; 402 -9.1; 442 -8.6; 486 -8.0; 535 -8.5; 588 -8.4; 647 -8.0; 712 -7.7; 783 -7.1; 861 -6.8; 947 -6.5; 1042 -6.6; 1146 -6.9; 1261 -7.1; 1387 -7.9; 1526 -8.7; 1678 -9.4; 1846 -9.9; 2031 -10.3; 2234 -9.6; 2457 -9.0; 2703 -6.6; 2973 -3.2; 3270 -4.4; 3597 -5.1; 3957 -7.9; 4353 -12.6; 4788 -11.3; 5267 -6.0; 5793 -4.5; 6373 -6.1; 7010 -9.7; 7711 -12.5; 8482 -15.7; 9330 -16.7; 10263 -12.5; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K240 Sextett GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 Sextett ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.65 | 6.6 dB   |
| Peaking | 109 Hz   | 1.28 | -6.4 dB  |
| Peaking | 231 Hz   | 0.73 | -3.9 dB  |
| Peaking | 1919 Hz  | 3.01 | -3.9 dB  |
| Peaking | 8966 Hz  | 3.14 | -11.4 dB |
| Peaking | 2495 Hz  | 3.37 | -3.4 dB  |
| Peaking | 3072 Hz  | 2.33 | 5.3 dB   |
| Peaking | 4486 Hz  | 4.8  | -8.3 dB  |
| Peaking | 5682 Hz  | 5.01 | 4.4 dB   |
| Peaking | 11795 Hz | 6.06 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -7.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K240%20Sextett/AKG%20K240%20Sextett.png)