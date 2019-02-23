# VSonic GR07 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.0; 25 -5.4; 28 -5.8; 31 -6.2; 34 -6.5; 37 -6.7; 41 -7.0; 45 -7.2; 49 -7.4; 54 -7.6; 60 -7.9; 66 -8.1; 72 -8.4; 79 -8.7; 87 -9.0; 96 -9.3; 106 -9.4; 116 -9.5; 128 -9.6; 141 -9.7; 155 -9.7; 170 -9.7; 187 -9.6; 206 -9.6; 227 -9.4; 249 -9.3; 274 -9.1; 302 -8.9; 332 -8.6; 365 -8.4; 402 -8.2; 442 -7.8; 486 -7.7; 535 -7.4; 588 -6.9; 647 -6.6; 712 -6.5; 783 -6.2; 861 -6.3; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.1; 1387 -7.4; 1526 -8.2; 1678 -8.6; 1846 -8.7; 2031 -8.4; 2234 -7.9; 2457 -6.6; 2703 -4.7; 2973 -2.3; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -3.6; 4788 -6.2; 5267 -7.5; 5793 -6.2; 6373 -2.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic GR07 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR07 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.39 | 2.2 dB  |
| Peaking | 151 Hz   | 0.53 | -3.4 dB |
| Peaking | 1974 Hz  | 2.02 | -3.2 dB |
| Peaking | 3451 Hz  | 2.33 | 7.1 dB  |
| Peaking | 21804 Hz | 2.27 | 1.0 dB  |
| Peaking | 799 Hz   | 3.02 | 0.9 dB  |
| Peaking | 4064 Hz  | 8.15 | 2.0 dB  |
| Peaking | 5430 Hz  | 2.74 | -3.6 dB |
| Peaking | 6500 Hz  | 4.16 | 6.1 dB  |
| Peaking | 7538 Hz  | 2.83 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20GR07%20Classic/VSonic%20GR07%20Classic.png)