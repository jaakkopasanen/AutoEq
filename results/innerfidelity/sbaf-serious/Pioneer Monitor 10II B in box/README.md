# Pioneer Monitor 10II B in box
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.7; 23 -12.8; 25 -12.8; 28 -12.8; 31 -12.8; 34 -12.9; 37 -12.9; 41 -12.8; 45 -12.7; 49 -12.7; 54 -12.8; 60 -12.7; 66 -12.7; 72 -12.7; 79 -12.6; 87 -12.4; 96 -11.9; 106 -10.8; 116 -9.2; 128 -9.1; 141 -13.5; 155 -15.1; 170 -11.2; 187 -14.6; 206 -14.9; 227 -15.1; 249 -14.8; 274 -13.9; 302 -13.2; 332 -12.2; 365 -11.1; 402 -9.8; 442 -8.4; 486 -7.2; 535 -5.7; 588 -3.8; 647 -2.6; 712 -2.0; 783 -2.4; 861 -3.4; 947 -3.5; 1042 -3.7; 1146 -2.5; 1261 -4.1; 1387 -7.6; 1526 -12.5; 1678 -16.8; 1846 -17.7; 2031 -12.3; 2234 -6.5; 2457 -4.0; 2703 -6.1; 2973 -3.9; 3270 -0.7; 3597 -1.4; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer Monitor 10II B in box GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer Monitor 10II B in box ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 28 Hz   |  0.62 | -6.3 dB  |
| Peaking | 69 Hz   |  1.82 | -2.9 dB  |
| Peaking | 255 Hz  |  0.79 | -10.6 dB |
| Peaking | 1611 Hz |  0.3  | 10.6 dB  |
| Peaking | 1767 Hz |  2.29 | -23.0 dB |
| Peaking | 124 Hz  |  7.15 | 3.2 dB   |
| Peaking | 149 Hz  |  9.96 | -3.7 dB  |
| Peaking | 2791 Hz | 12.05 | -3.8 dB  |
| Peaking | 6419 Hz |  1.21 | 8.5 dB   |
| Peaking | 7509 Hz |  1.19 | -8.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -9.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.6 dB |
| Peaking | 4000 Hz  | 1.41 | 10.0 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20Monitor%2010II%20B%20in%20box/Pioneer%20Monitor%2010II%20B%20in%20box.png)