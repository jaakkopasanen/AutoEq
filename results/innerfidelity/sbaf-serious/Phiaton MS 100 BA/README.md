# Phiaton MS 100 BA
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.5; 25 -5.6; 28 -5.8; 31 -6.0; 34 -6.2; 37 -6.3; 41 -6.6; 45 -6.8; 49 -7.0; 54 -7.2; 60 -7.6; 66 -8.0; 72 -8.3; 79 -8.7; 87 -9.1; 96 -9.6; 106 -9.9; 116 -10.1; 128 -10.4; 141 -10.6; 155 -10.8; 170 -10.9; 187 -10.9; 206 -11.0; 227 -10.9; 249 -10.8; 274 -10.6; 302 -10.4; 332 -10.1; 365 -9.8; 402 -9.4; 442 -8.9; 486 -8.6; 535 -8.1; 588 -7.4; 647 -7.0; 712 -6.7; 783 -6.3; 861 -6.3; 947 -6.3; 1042 -6.6; 1146 -6.7; 1261 -6.9; 1387 -7.4; 1526 -7.8; 1678 -8.2; 1846 -8.0; 2031 -7.6; 2234 -6.7; 2457 -4.6; 2703 -3.0; 2973 -1.8; 3270 -1.3; 3597 -0.9; 3957 -0.6; 4353 -1.2; 4788 -0.8; 5267 -0.5; 5793 -1.4; 6373 -5.5; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton MS 100 BA GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 100 BA ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.7  | 1.4 dB  |
| Peaking | 151 Hz  | 0.66 | -4.0 dB |
| Peaking | 315 Hz  | 1.26 | -2.1 dB |
| Peaking | 1858 Hz | 2.26 | -3.4 dB |
| Peaking | 3902 Hz | 1.09 | 6.6 dB  |
| Peaking | 819 Hz  | 3.03 | 0.8 dB  |
| Peaking | 2873 Hz | 3.45 | 1.4 dB  |
| Peaking | 5497 Hz | 0.54 | -1.2 dB |
| Peaking | 5518 Hz | 3.86 | 4.7 dB  |
| Peaking | 6069 Hz | 2.24 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20MS%20100%20BA/Phiaton%20MS%20100%20BA.png)