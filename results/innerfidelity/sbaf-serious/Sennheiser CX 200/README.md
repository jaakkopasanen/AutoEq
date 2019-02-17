# Sennheiser CX 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.3; 25 -8.6; 28 -8.9; 31 -9.3; 34 -9.5; 37 -9.6; 41 -9.8; 45 -10.0; 49 -10.2; 54 -10.4; 60 -10.5; 66 -10.8; 72 -10.9; 79 -11.1; 87 -11.3; 96 -11.4; 106 -11.4; 116 -11.3; 128 -11.4; 141 -11.3; 155 -11.1; 170 -10.9; 187 -10.6; 206 -10.3; 227 -9.9; 249 -9.6; 274 -9.2; 302 -8.8; 332 -8.4; 365 -8.0; 402 -7.7; 442 -7.2; 486 -7.0; 535 -6.7; 588 -6.2; 647 -6.0; 712 -6.0; 783 -5.7; 861 -6.0; 947 -6.4; 1042 -6.7; 1146 -7.3; 1261 -7.5; 1387 -8.1; 1526 -8.6; 1678 -8.7; 1846 -8.2; 2031 -7.4; 2234 -6.1; 2457 -4.2; 2703 -2.8; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -2.7; 4788 -4.2; 5267 -4.5; 5793 -5.4; 6373 -6.6; 7010 -6.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -7.1; 11289 -7.8; 12418 -6.5; 13660 -7.2; 15026 -8.9; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 69 Hz    |  0.48 | -3.9 dB |
| Peaking | 170 Hz   |  0.91 | -2.7 dB |
| Peaking | 1719 Hz  |  2.27 | -3.3 dB |
| Peaking | 3386 Hz  |  1.75 | 7.0 dB  |
| Peaking | 26 Hz    |  1.71 | -0.4 dB |
| Peaking | 740 Hz   |  2.05 | 1.2 dB  |
| Peaking | 1259 Hz  |  3.14 | -0.5 dB |
| Peaking | 4020 Hz  | 12.59 | 1.2 dB  |
| Peaking | 13755 Hz |  0.76 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20CX%20200/Sennheiser%20CX%20200.png)