# Audeo PFE 121 Gray Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.2; 28 -1.6; 31 -1.9; 34 -2.2; 37 -2.5; 41 -2.8; 45 -3.1; 49 -3.3; 54 -3.7; 60 -4.1; 66 -4.4; 72 -4.8; 79 -5.3; 87 -5.8; 96 -6.2; 106 -6.5; 116 -6.6; 128 -7.0; 141 -7.3; 155 -7.4; 170 -7.6; 187 -7.6; 206 -7.7; 227 -7.5; 249 -7.5; 274 -7.4; 302 -7.2; 332 -7.0; 365 -6.8; 402 -6.6; 442 -6.1; 486 -6.0; 535 -5.8; 588 -5.3; 647 -5.1; 712 -5.2; 783 -5.1; 861 -5.5; 947 -6.0; 1042 -6.5; 1146 -7.0; 1261 -7.5; 1387 -8.3; 1526 -9.1; 1678 -9.5; 1846 -9.5; 2031 -9.3; 2234 -9.0; 2457 -7.9; 2703 -7.0; 2973 -5.0; 3270 -2.9; 3597 -2.0; 3957 -2.7; 4353 -5.0; 4788 -5.6; 5267 -4.0; 5793 -2.6; 6373 -1.6; 7010 -3.8; 7711 -6.0; 8482 -6.9; 9330 -9.3; 10263 -9.0; 11289 -6.3; 12418 -6.3; 13660 -7.1; 15026 -11.1; 16529 -7.1; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeo PFE 121 Gray Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 121 Gray Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.85 | 5.5 dB  |
| Peaking | 1890 Hz  | 1.87 | -3.6 dB |
| Peaking | 3562 Hz  | 3.11 | 5.7 dB  |
| Peaking | 6301 Hz  | 2.98 | 6.5 dB  |
| Peaking | 10288 Hz | 0.33 | -2.1 dB |
| Peaking | 200 Hz   | 1.05 | -1.6 dB |
| Peaking | 694 Hz   | 2.04 | 1.7 dB  |
| Peaking | 9671 Hz  | 4.23 | -3.4 dB |
| Peaking | 14249 Hz | 0.9  | 4.6 dB  |
| Peaking | 15075 Hz | 2.6  | -7.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -3.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeo%20PFE%20121%20Gray%20Filter/Audeo%20PFE%20121%20Gray%20Filter.png)