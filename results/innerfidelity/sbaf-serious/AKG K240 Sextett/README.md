# AKG K240 Sextett
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.1; 49 -2.0; 54 -2.9; 60 -3.3; 66 -2.9; 72 -4.3; 79 -6.9; 87 -8.7; 96 -9.7; 106 -10.2; 116 -10.5; 128 -10.5; 141 -10.2; 155 -9.8; 170 -8.3; 187 -8.5; 206 -9.1; 227 -8.7; 249 -8.3; 274 -7.8; 302 -7.4; 332 -7.0; 365 -6.4; 402 -6.2; 442 -5.7; 486 -5.1; 535 -5.6; 588 -5.4; 647 -5.0; 712 -4.8; 783 -4.2; 861 -3.9; 947 -3.6; 1042 -3.7; 1146 -4.0; 1261 -4.2; 1387 -5.0; 1526 -5.8; 1678 -6.5; 1846 -7.0; 2031 -7.3; 2234 -6.6; 2457 -6.0; 2703 -3.7; 2973 -0.6; 3270 -1.5; 3597 -2.2; 3957 -5.0; 4353 -9.7; 4788 -8.4; 5267 -3.1; 5793 -1.5; 6373 -3.2; 7010 -6.8; 7711 -9.6; 8482 -12.8; 9330 -13.8; 10263 -9.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K240 Sextett GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 Sextett ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 82 Hz   | 0.14 | 12.8 dB  |
| Peaking | 136 Hz  | 0.4  | -16.4 dB |
| Peaking | 3154 Hz | 4.7  | 6.2 dB   |
| Peaking | 5922 Hz | 5.75 | 6.2 dB   |
| Peaking | 8945 Hz | 3.36 | -8.3 dB  |
| Peaking | 97 Hz   | 4.99 | -1.5 dB  |
| Peaking | 172 Hz  | 8.55 | 2.1 dB   |
| Peaking | 2043 Hz | 1.56 | -5.5 dB  |
| Peaking | 2199 Hz | 0.66 | 3.7 dB   |
| Peaking | 4482 Hz | 7.53 | -6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K240%20Sextett/AKG%20K240%20Sextett.png)