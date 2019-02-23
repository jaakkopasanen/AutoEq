# Sol Republic Tracks
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -10.1; 25 -10.7; 28 -11.4; 31 -12.0; 34 -12.4; 37 -12.8; 41 -13.2; 45 -13.5; 49 -13.6; 54 -13.8; 60 -13.8; 66 -13.9; 72 -14.0; 79 -14.1; 87 -13.9; 96 -13.6; 106 -13.6; 116 -13.7; 128 -13.9; 141 -14.1; 155 -14.1; 170 -13.5; 187 -13.8; 206 -13.4; 227 -12.6; 249 -11.6; 274 -9.8; 302 -7.8; 332 -5.8; 365 -3.3; 402 -0.6; 442 -0.5; 486 -1.6; 535 -3.7; 588 -5.3; 647 -6.9; 712 -8.1; 783 -8.7; 861 -9.0; 947 -9.0; 1042 -9.0; 1146 -8.4; 1261 -7.7; 1387 -7.4; 1526 -6.3; 1678 -6.6; 1846 -7.4; 2031 -6.7; 2234 -5.5; 2457 -4.1; 2703 -2.8; 2973 -2.0; 3270 -1.3; 3597 -0.9; 3957 -1.0; 4353 -3.5; 4788 -4.9; 5267 -4.5; 5793 -2.7; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sol Republic Tracks GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sol Republic Tracks ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 131 Hz  | 0.19 | -8.3 dB |
| Peaking | 428 Hz  | 1.65 | 13.0 dB |
| Peaking | 892 Hz  | 2.12 | -1.5 dB |
| Peaking | 3401 Hz | 1.82 | 6.1 dB  |
| Peaking | 6315 Hz | 5.37 | 4.6 dB  |
| Peaking | 101 Hz  | 3.34 | 0.8 dB  |
| Peaking | 210 Hz  | 4.11 | -1.1 dB |
| Peaking | 1604 Hz | 7.61 | 2.6 dB  |
| Peaking | 1766 Hz | 3.47 | -1.7 dB |
| Peaking | 2581 Hz | 6.68 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.9 dB |
| Peaking | 62 Hz    | 1.41 | -5.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | 6.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.8 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sol%20Republic%20Tracks/Sol%20Republic%20Tracks.png)