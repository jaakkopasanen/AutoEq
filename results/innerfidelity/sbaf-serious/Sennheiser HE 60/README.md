# Sennheiser HE 60
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.0; 34 -1.3; 37 -1.4; 41 -1.5; 45 -1.5; 49 -1.5; 54 -1.4; 60 -1.6; 66 -2.0; 72 -2.4; 79 -4.3; 87 -5.1; 96 -5.1; 106 -5.1; 116 -5.1; 128 -5.4; 141 -5.4; 155 -5.6; 170 -5.8; 187 -5.8; 206 -6.0; 227 -6.0; 249 -6.1; 274 -6.1; 302 -6.1; 332 -6.1; 365 -6.1; 402 -6.2; 442 -6.2; 486 -6.3; 535 -5.9; 588 -5.1; 647 -5.2; 712 -5.9; 783 -5.4; 861 -5.4; 947 -6.7; 1042 -7.1; 1146 -7.0; 1261 -6.8; 1387 -7.2; 1526 -7.9; 1678 -8.0; 1846 -8.2; 2031 -7.8; 2234 -7.3; 2457 -6.6; 2703 -6.4; 2973 -6.5; 3270 -6.4; 3597 -5.1; 3957 -5.2; 4353 -6.3; 4788 -7.5; 5267 -9.8; 5793 -11.0; 6373 -8.7; 7010 -5.0; 7711 -6.2; 8482 -7.2; 9330 -9.7; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.2; 20000 -11.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HE 60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HE 60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.4  | 5.9 dB  |
| Peaking | 59 Hz    | 2.77 | 2.1 dB  |
| Peaking | 1765 Hz  | 3.42 | -1.9 dB |
| Peaking | 5727 Hz  | 5.68 | -5.0 dB |
| Peaking | 19965 Hz | 1.81 | -5.2 dB |
| Peaking | 641 Hz   | 2.61 | 1.4 dB  |
| Peaking | 3870 Hz  | 2.78 | 3.0 dB  |
| Peaking | 4424 Hz  | 1.19 | -1.5 dB |
| Peaking | 7141 Hz  | 6.43 | 2.6 dB  |
| Peaking | 9242 Hz  | 8.33 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HE%2060/Sennheiser%20HE%2060.png)