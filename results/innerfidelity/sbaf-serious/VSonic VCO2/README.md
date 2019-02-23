# VSonic VCO2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.6; 25 -3.7; 28 -3.7; 31 -3.7; 34 -3.8; 37 -3.9; 41 -4.0; 45 -4.2; 49 -4.3; 54 -4.5; 60 -4.8; 66 -5.0; 72 -5.3; 79 -5.7; 87 -6.1; 96 -6.3; 106 -6.7; 116 -6.9; 128 -7.2; 141 -7.5; 155 -7.7; 170 -7.8; 187 -7.9; 206 -8.0; 227 -8.0; 249 -8.0; 274 -7.9; 302 -7.9; 332 -7.9; 365 -7.8; 402 -7.7; 442 -7.3; 486 -7.4; 535 -7.3; 588 -6.9; 647 -6.8; 712 -6.9; 783 -6.8; 861 -7.1; 947 -7.6; 1042 -8.0; 1146 -8.4; 1261 -9.0; 1387 -9.6; 1526 -10.1; 1678 -10.3; 1846 -9.7; 2031 -7.7; 2234 -6.6; 2457 -4.9; 2703 -2.3; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.7; 4788 -4.9; 5267 -5.0; 5793 -6.3; 6373 -9.6; 7010 -11.8; 7711 -10.1; 8482 -7.4; 9330 -6.5; 10263 -7.5; 11289 -7.1; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VCO2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VCO2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.36 | 3.0 dB  |
| Peaking | 51 Hz    | 2.22 | 1.9 dB  |
| Peaking | 1783 Hz  | 1.05 | -6.1 dB |
| Peaking | 3206 Hz  | 1.18 | 8.9 dB  |
| Peaking | 6979 Hz  | 3.18 | -6.7 dB |
| Peaking | 84 Hz    | 0.62 | 1.5 dB  |
| Peaking | 175 Hz   | 0.47 | -2.1 dB |
| Peaking | 610 Hz   | 3.3  | 0.3 dB  |
| Peaking | 794 Hz   | 1.97 | 0.8 dB  |
| Peaking | 10709 Hz | 9.4  | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VCO2/VSonic%20VCO2.png)