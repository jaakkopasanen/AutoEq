# AKG K712
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.3; 31 -1.9; 34 -2.3; 37 -2.7; 41 -3.2; 45 -3.6; 49 -3.9; 54 -4.3; 60 -4.7; 66 -5.1; 72 -5.5; 79 -5.9; 87 -6.3; 96 -6.8; 106 -7.1; 116 -7.3; 128 -7.5; 141 -7.5; 155 -7.8; 170 -8.1; 187 -7.6; 206 -7.8; 227 -7.9; 249 -8.1; 274 -7.9; 302 -7.7; 332 -7.4; 365 -7.1; 402 -6.9; 442 -6.7; 486 -6.4; 535 -5.8; 588 -5.3; 647 -5.0; 712 -4.9; 783 -4.8; 861 -4.8; 947 -4.6; 1042 -4.7; 1146 -4.3; 1261 -4.3; 1387 -5.1; 1526 -6.3; 1678 -7.6; 1846 -9.0; 2031 -9.5; 2234 -9.0; 2457 -6.9; 2703 -3.6; 2973 -1.9; 3270 -1.9; 3597 -3.3; 3957 -5.6; 4353 -7.7; 4788 -6.7; 5267 -4.7; 5793 -4.8; 6373 -6.6; 7010 -8.4; 7711 -9.4; 8482 -10.4; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -10.7; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.05 | 6.1 dB  |
| Peaking | 2112 Hz  | 4.07 | -4.5 dB |
| Peaking | 3066 Hz  | 2.77 | 5.4 dB  |
| Peaking | 8223 Hz  | 4.32 | -4.3 dB |
| Peaking | 18652 Hz | 1.88 | -4.9 dB |
| Peaking | 58 Hz    | 1.61 | 1.2 dB  |
| Peaking | 208 Hz   | 0.55 | -1.8 dB |
| Peaking | 1170 Hz  | 0.73 | 4.7 dB  |
| Peaking | 1651 Hz  | 0.82 | -3.4 dB |
| Peaking | 5619 Hz  | 8.91 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K712/AKG%20K712.png)