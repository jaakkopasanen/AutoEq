# Grado RS1e S Cushions
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.5; 34 -2.4; 37 -3.3; 41 -4.2; 45 -5.0; 49 -5.8; 54 -6.6; 60 -7.5; 66 -8.2; 72 -8.9; 79 -9.4; 87 -10.1; 96 -10.6; 106 -11.0; 116 -11.2; 128 -11.4; 141 -11.6; 155 -11.7; 170 -11.6; 187 -11.5; 206 -11.2; 227 -10.9; 249 -10.7; 274 -10.6; 302 -10.5; 332 -10.1; 365 -9.8; 402 -9.4; 442 -9.0; 486 -8.8; 535 -8.6; 588 -8.1; 647 -7.9; 712 -7.9; 783 -7.6; 861 -7.7; 947 -7.6; 1042 -7.6; 1146 -7.6; 1261 -7.3; 1387 -7.3; 1526 -6.6; 1678 -8.6; 1846 -14.4; 2031 -13.7; 2234 -11.0; 2457 -7.7; 2703 -4.9; 2973 -2.6; 3270 -1.4; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1e S Cushions GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e S Cushions ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 25 Hz   |  0.6  | 7.3 dB  |
| Peaking | 134 Hz  |  0.37 | -5.7 dB |
| Peaking | 1967 Hz |  3.8  | -9.6 dB |
| Peaking | 3688 Hz |  1.62 | 6.5 dB  |
| Peaking | 5871 Hz |  3.52 | 4.9 dB  |
| Peaking | 1576 Hz | 10.9  | 2.7 dB  |
| Peaking | 2314 Hz |  9.13 | -1.5 dB |
| Peaking | 8274 Hz |  4.12 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1e%20S%20Cushions/Grado%20RS1e%20S%20Cushions.png)