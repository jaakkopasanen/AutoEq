# Whizzer A-HE03 Kylin
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -8.9; 25 -9.1; 28 -9.3; 31 -9.4; 34 -9.5; 37 -9.7; 41 -9.8; 45 -10.0; 49 -10.1; 54 -10.3; 60 -10.5; 66 -10.7; 72 -11.0; 79 -11.2; 87 -11.5; 96 -11.8; 106 -12.1; 116 -12.4; 128 -12.6; 141 -12.7; 155 -12.7; 170 -12.7; 187 -12.6; 206 -12.4; 227 -12.1; 249 -11.8; 274 -11.4; 302 -10.9; 332 -10.4; 365 -9.9; 402 -9.3; 442 -8.6; 486 -7.9; 535 -7.2; 588 -6.4; 647 -5.5; 712 -4.6; 783 -3.7; 861 -2.9; 947 -2.4; 1042 -2.3; 1146 -2.9; 1261 -3.8; 1387 -4.4; 1526 -4.6; 1678 -4.3; 1846 -3.8; 2031 -3.5; 2234 -3.4; 2457 -3.4; 2703 -3.6; 2973 -3.7; 3270 -3.9; 3597 -4.3; 3957 -5.3; 4353 -6.2; 4788 -5.2; 5267 -2.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.4; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.4; 16529 -9.4; 18182 -9.8; 20000 -10.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Whizzer A-HE03 Kylin GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Whizzer A-HE03 Kylin ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.4  | -2.0 dB |
| Peaking | 173 Hz   | 0.46 | -6.1 dB |
| Peaking | 922 Hz   | 1.32 | 4.8 dB  |
| Peaking | 2479 Hz  | 1.53 | 2.9 dB  |
| Peaking | 5940 Hz  | 4.03 | 6.5 dB  |
| Peaking | 3511 Hz  | 4.32 | 1.1 dB  |
| Peaking | 4438 Hz  | 3.53 | -1.7 dB |
| Peaking | 5210 Hz  | 6.96 | 1.7 dB  |
| Peaking | 19455 Hz | 0.55 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Whizzer%20A-HE03%20Kylin/Whizzer%20A-HE03%20Kylin.png)