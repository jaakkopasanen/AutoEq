# Rose BR5 Mk2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.9; 28 -1.2; 31 -1.4; 34 -1.6; 37 -1.8; 41 -2.0; 45 -2.1; 49 -2.3; 54 -2.5; 60 -2.8; 66 -3.1; 72 -3.5; 79 -3.9; 87 -4.3; 96 -4.8; 106 -5.2; 116 -5.6; 128 -5.9; 141 -6.3; 155 -6.5; 170 -6.7; 187 -6.8; 206 -6.9; 227 -6.9; 249 -6.9; 274 -6.8; 302 -6.7; 332 -6.6; 365 -6.4; 402 -6.3; 442 -6.1; 486 -5.8; 535 -5.6; 588 -5.2; 647 -4.9; 712 -4.5; 783 -4.0; 861 -3.5; 947 -3.0; 1042 -2.9; 1146 -3.4; 1261 -4.4; 1387 -5.2; 1526 -5.2; 1678 -4.8; 1846 -4.4; 2031 -4.1; 2234 -4.0; 2457 -3.8; 2703 -3.7; 2973 -3.6; 3270 -4.0; 3597 -4.6; 3957 -5.3; 4353 -4.8; 4788 -3.7; 5267 -3.1; 5793 -3.4; 6373 -5.4; 7010 -5.6; 7711 -6.0; 8482 -6.0; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -7.0; 15026 -11.9; 16529 -11.9; 18182 -9.6; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rose BR5 Mk2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rose BR5 Mk2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.58 | 4.4 dB  |
| Peaking | 57 Hz    | 1.17 | 1.4 dB  |
| Peaking | 236 Hz   | 0.64 | -2.8 dB |
| Peaking | 2903 Hz  | 0.08 | 1.2 dB  |
| Peaking | 17227 Hz | 0.7  | -7.4 dB |
| Peaking | 1003 Hz  | 3.2  | 1.8 dB  |
| Peaking | 1453 Hz  | 3.86 | -1.5 dB |
| Peaking | 5530 Hz  | 3.44 | 3.8 dB  |
| Peaking | 6061 Hz  | 1.46 | -2.6 dB |
| Peaking | 12316 Hz | 3.52 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -7.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Rose%20BR5%20Mk2/Rose%20BR5%20Mk2.png)