# Sol Republic Tracks
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.6; 25 -8.3; 28 -9.0; 31 -9.6; 34 -10.0; 37 -10.4; 41 -10.8; 45 -11.0; 49 -11.2; 54 -11.4; 60 -11.4; 66 -11.4; 72 -11.5; 79 -11.6; 87 -11.5; 96 -11.1; 106 -11.2; 116 -11.3; 128 -11.5; 141 -11.6; 155 -11.6; 170 -11.1; 187 -11.3; 206 -11.0; 227 -10.2; 249 -9.1; 274 -7.4; 302 -5.3; 332 -3.3; 365 -0.9; 402 -0.5; 442 -0.5; 486 -0.5; 535 -1.3; 588 -2.9; 647 -4.4; 712 -5.7; 783 -6.3; 861 -6.6; 947 -6.5; 1042 -6.6; 1146 -5.9; 1261 -5.3; 1387 -5.0; 1526 -3.8; 1678 -4.1; 1846 -5.0; 2031 -4.2; 2234 -3.1; 2457 -1.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.2; 4788 -2.5; 5267 -2.0; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sol Republic Tracks GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sol Republic Tracks ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 161 Hz  | 0.22 | -6.3 dB |
| Peaking | 427 Hz  | 1.3  | 11.8 dB |
| Peaking | 2569 Hz | 0.99 | 2.9 dB  |
| Peaking | 3601 Hz | 1.46 | 4.4 dB  |
| Peaking | 6030 Hz | 4.4  | 4.7 dB  |
| Peaking | 20 Hz   | 2.53 | 1.5 dB  |
| Peaking | 213 Hz  | 5.2  | -1.1 dB |
| Peaking | 1599 Hz | 5.67 | 2.7 dB  |
| Peaking | 1797 Hz | 4.49 | -2.0 dB |
| Peaking | 8368 Hz | 3.72 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 7.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sol%20Republic%20Tracks/Sol%20Republic%20Tracks.png)