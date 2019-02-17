# Pioneer SE-MJ31
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.1; 72 -2.6; 79 -4.3; 87 -5.7; 96 -6.6; 106 -7.1; 116 -7.2; 128 -7.5; 141 -7.7; 155 -7.7; 170 -7.5; 187 -7.1; 206 -7.0; 227 -6.8; 249 -6.7; 274 -6.4; 302 -6.4; 332 -6.5; 365 -6.3; 402 -6.4; 442 -6.5; 486 -6.7; 535 -7.0; 588 -6.9; 647 -7.1; 712 -7.3; 783 -7.2; 861 -6.8; 947 -6.2; 1042 -6.9; 1146 -8.5; 1261 -10.7; 1387 -13.2; 1526 -12.9; 1678 -14.1; 1846 -14.0; 2031 -10.7; 2234 -7.1; 2457 -4.7; 2703 -2.5; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.3; 7010 -9.3; 7711 -7.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.7; 16529 -7.2; 18182 -7.8; 20000 -9.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer SE-MJ31 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE-MJ31 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 50 Hz    | 0.38 | 8.2 dB   |
| Peaking | 113 Hz   | 0.82 | -6.4 dB  |
| Peaking | 1714 Hz  | 1.75 | -11.9 dB |
| Peaking | 3588 Hz  | 0.7  | 8.3 dB   |
| Peaking | 7374 Hz  | 5.37 | -6.4 dB  |
| Peaking | 987 Hz   | 5.65 | 1.6 dB   |
| Peaking | 1347 Hz  | 8.68 | -1.9 dB  |
| Peaking | 3929 Hz  | 5.75 | -1.0 dB  |
| Peaking | 5943 Hz  | 7.69 | 2.7 dB   |
| Peaking | 20017 Hz | 0.4  | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -6.6 dB |
| Peaking | 4000 Hz  | 1.41 | 10.3 dB |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20SE-MJ31/Pioneer%20SE-MJ31.png)