# Audeo PFE 121 Green Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.2; 25 -8.3; 28 -8.4; 31 -8.5; 34 -8.6; 37 -8.7; 41 -8.9; 45 -9.1; 49 -9.3; 54 -9.5; 60 -9.8; 66 -10.0; 72 -10.3; 79 -10.6; 87 -11.0; 96 -11.4; 106 -11.6; 116 -11.8; 128 -12.0; 141 -12.2; 155 -12.3; 170 -12.3; 187 -12.2; 206 -12.1; 227 -11.9; 249 -11.8; 274 -11.5; 302 -11.2; 332 -10.8; 365 -10.5; 402 -10.1; 442 -9.5; 486 -9.0; 535 -8.5; 588 -7.8; 647 -7.3; 712 -7.0; 783 -6.5; 861 -6.4; 947 -6.4; 1042 -6.4; 1146 -6.2; 1261 -6.2; 1387 -6.3; 1526 -6.4; 1678 -6.1; 1846 -5.2; 2031 -4.2; 2234 -3.3; 2457 -1.8; 2703 -1.8; 2973 -2.3; 3270 -1.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.6; 9330 -11.3; 10263 -8.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.4; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeo PFE 121 Green Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 121 Green Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 81 Hz    | 0.32 | -2.5 dB |
| Peaking | 205 Hz   | 0.56 | -4.1 dB |
| Peaking | 3624 Hz  | 0.93 | 5.5 dB  |
| Peaking | 5882 Hz  | 2.29 | 3.8 dB  |
| Peaking | 9225 Hz  | 3.47 | -6.3 dB |
| Peaking | 791 Hz   | 3.06 | 0.8 dB  |
| Peaking | 1630 Hz  | 3.24 | -1.1 dB |
| Peaking | 2518 Hz  | 3.58 | 1.4 dB  |
| Peaking | 3037 Hz  | 6.57 | -1.4 dB |
| Peaking | 14987 Hz | 6.6  | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeo%20PFE%20121%20Green%20Filter/Audeo%20PFE%20121%20Green%20Filter.png)