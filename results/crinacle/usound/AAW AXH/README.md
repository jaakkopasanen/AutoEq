# AAW AXH
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.5; 25 -3.5; 28 -3.6; 31 -3.8; 34 -4.0; 37 -4.1; 41 -4.2; 45 -4.4; 49 -4.5; 54 -4.6; 60 -4.6; 66 -4.8; 72 -4.9; 79 -5.1; 87 -5.4; 96 -5.7; 106 -5.8; 116 -6.0; 128 -6.3; 141 -6.4; 155 -6.7; 170 -6.8; 187 -7.0; 206 -7.0; 227 -7.1; 249 -7.1; 274 -7.2; 302 -7.3; 332 -7.3; 365 -7.4; 402 -7.5; 442 -7.5; 486 -7.5; 535 -7.4; 588 -7.4; 647 -7.2; 712 -6.9; 783 -6.6; 861 -6.3; 947 -6.2; 1042 -6.4; 1146 -6.9; 1261 -7.3; 1387 -7.4; 1526 -6.9; 1678 -6.1; 1846 -5.5; 2031 -5.4; 2234 -5.7; 2457 -5.4; 2703 -4.1; 2973 -2.3; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.7; 5267 -7.8; 5793 -9.9; 6373 -14.3; 7010 -18.4; 7711 -14.9; 8482 -8.4; 9330 -6.5; 10263 -6.5; 11289 -6.9; 12418 -9.2; 13660 -12.1; 15026 -16.0; 16529 -19.4; 18182 -17.6; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AAW AXH GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AAW AXH ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.93 | 3.0 dB   |
| Peaking | 63 Hz    | 1.85 | 1.3 dB   |
| Peaking | 3897 Hz  | 1.78 | 7.8 dB   |
| Peaking | 6903 Hz  | 3.91 | -13.4 dB |
| Peaking | 17168 Hz | 1.13 | -14.4 dB |
| Peaking | 386 Hz   | 0.9  | -1.1 dB  |
| Peaking | 1357 Hz  | 5.39 | -1.3 dB  |
| Peaking | 7629 Hz  | 7.6  | -3.4 dB  |
| Peaking | 9989 Hz  | 1.85 | 3.2 dB   |
| Peaking | 14966 Hz | 2.81 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB   |
| Peaking | 62 Hz    | 1.41 | 1.4 dB   |
| Peaking | 125 Hz   | 1.41 | 0.1 dB   |
| Peaking | 250 Hz   | 1.41 | -0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -6.6 dB  |
| Peaking | 16000 Hz | 1.41 | -12.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/AAW%20AXH/AAW%20AXH.png)