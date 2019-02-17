# Westone ADV Alpha
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.7; 23 -13.8; 25 -13.8; 28 -13.8; 31 -13.9; 34 -14.0; 37 -14.0; 41 -14.1; 45 -14.1; 49 -14.2; 54 -14.4; 60 -14.6; 66 -14.8; 72 -15.0; 79 -15.2; 87 -15.4; 96 -15.7; 106 -15.7; 116 -15.7; 128 -15.7; 141 -15.7; 155 -15.5; 170 -15.4; 187 -15.0; 206 -14.8; 227 -14.2; 249 -13.9; 274 -13.3; 302 -12.7; 332 -12.2; 365 -11.5; 402 -10.9; 442 -10.1; 486 -9.6; 535 -8.9; 588 -8.0; 647 -7.5; 712 -7.1; 783 -6.6; 861 -6.4; 947 -6.4; 1042 -6.5; 1146 -6.5; 1261 -6.6; 1387 -6.9; 1526 -7.1; 1678 -6.4; 1846 -5.8; 2031 -5.0; 2234 -4.2; 2457 -2.9; 2703 -1.7; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -3.3; 4353 -8.0; 4788 -10.4; 5267 -7.2; 5793 -3.3; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone ADV Alpha GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone ADV Alpha ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.2  | -6.9 dB |
| Peaking | 138 Hz   | 0.67 | -5.3 dB |
| Peaking | 287 Hz   | 1.08 | -3.1 dB |
| Peaking | 3061 Hz  | 2.42 | 6.8 dB  |
| Peaking | 21542 Hz | 2.25 | 2.6 dB  |
| Peaking | 842 Hz   | 2.69 | 0.9 dB  |
| Peaking | 1493 Hz  | 5.41 | -0.9 dB |
| Peaking | 3758 Hz  | 6.12 | 3.2 dB  |
| Peaking | 4708 Hz  | 4.13 | -6.2 dB |
| Peaking | 6250 Hz  | 4.61 | 6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.2 dB |
| Peaking | 62 Hz    | 1.41 | -5.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.7 dB |
| Peaking | 250 Hz   | 1.41 | -6.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20ADV%20Alpha/Westone%20ADV%20Alpha.png)