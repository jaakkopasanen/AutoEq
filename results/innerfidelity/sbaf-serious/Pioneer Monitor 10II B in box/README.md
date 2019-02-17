# Pioneer Monitor 10II B in box
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.5; 23 -15.6; 25 -15.6; 28 -15.6; 31 -15.6; 34 -15.7; 37 -15.7; 41 -15.6; 45 -15.5; 49 -15.5; 54 -15.6; 60 -15.5; 66 -15.5; 72 -15.5; 79 -15.4; 87 -15.2; 96 -14.7; 106 -13.6; 116 -12.0; 128 -11.9; 141 -16.3; 155 -17.9; 170 -14.0; 187 -17.4; 206 -17.7; 227 -18.0; 249 -17.6; 274 -16.7; 302 -16.0; 332 -15.0; 365 -13.9; 402 -12.6; 442 -11.2; 486 -10.0; 535 -8.5; 588 -6.6; 647 -5.4; 712 -4.8; 783 -5.2; 861 -6.2; 947 -6.3; 1042 -6.5; 1146 -5.3; 1261 -6.9; 1387 -10.4; 1526 -15.3; 1678 -19.6; 1846 -20.5; 2031 -15.2; 2234 -9.3; 2457 -6.8; 2703 -8.9; 2973 -6.7; 3270 -3.5; 3597 -4.2; 3957 -0.8; 4353 -0.5; 4788 -0.9; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -7.4; 11289 -7.7; 12418 -6.5; 13660 -6.5; 15026 -7.2; 16529 -6.6; 18182 -6.5; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer Monitor 10II B in box GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer Monitor 10II B in box ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 0.87 | -5.5 dB  |
| Peaking | 57 Hz   | 0.48 | -7.7 dB  |
| Peaking | 240 Hz  | 1.21 | -10.2 dB |
| Peaking | 1798 Hz | 4.12 | -16.4 dB |
| Peaking | 4809 Hz | 1.44 | 6.5 dB   |
| Peaking | 255 Hz  | 3.36 | 2.2 dB   |
| Peaking | 373 Hz  | 1    | -2.3 dB  |
| Peaking | 682 Hz  | 2.05 | 4.1 dB   |
| Peaking | 1187 Hz | 4.5  | 3.1 dB   |
| Peaking | 1529 Hz | 5.83 | -3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.4 dB  |
| Peaking | 62 Hz    | 1.41 | -6.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -11.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -12.4 dB |
| Peaking | 4000 Hz  | 1.41 | 9.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20Monitor%2010II%20B%20in%20box/Pioneer%20Monitor%2010II%20B%20in%20box.png)