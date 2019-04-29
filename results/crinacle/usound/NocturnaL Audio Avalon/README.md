# NocturnaL Audio Avalon
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.2; 25 -6.5; 28 -6.9; 31 -7.2; 34 -7.4; 37 -7.6; 41 -7.8; 45 -8.1; 49 -8.3; 54 -8.6; 60 -8.8; 66 -9.2; 72 -9.4; 79 -9.8; 87 -10.2; 96 -10.5; 106 -10.9; 116 -11.3; 128 -11.5; 141 -11.7; 155 -11.8; 170 -11.9; 187 -12.0; 206 -12.0; 227 -11.9; 249 -11.7; 274 -11.5; 302 -11.3; 332 -11.0; 365 -10.7; 402 -10.3; 442 -9.8; 486 -9.3; 535 -8.8; 588 -8.2; 647 -7.5; 712 -6.8; 783 -5.9; 861 -5.1; 947 -4.5; 1042 -4.2; 1146 -4.3; 1261 -4.3; 1387 -4.1; 1526 -3.4; 1678 -2.5; 1846 -1.7; 2031 -1.5; 2234 -2.4; 2457 -3.6; 2703 -2.6; 2973 -1.2; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -4.0; 5793 -8.3; 6373 -9.8; 7010 -11.1; 7711 -6.9; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -9.5; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NocturnaL Audio Avalon GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NocturnaL Audio Avalon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 116 Hz   | 0.59 | -2.1 dB |
| Peaking | 312 Hz   | 0.39 | -5.1 dB |
| Peaking | 1413 Hz  | 0.4  | 4.3 dB  |
| Peaking | 4492 Hz  | 1.33 | 6.4 dB  |
| Peaking | 6397 Hz  | 2.42 | -8.2 dB |
| Peaking | 19 Hz    | 2.05 | 1.2 dB  |
| Peaking | 1432 Hz  | 2.66 | -2.3 dB |
| Peaking | 1775 Hz  | 1.19 | 1.9 dB  |
| Peaking | 2453 Hz  | 5.79 | -2.5 dB |
| Peaking | 14908 Hz | 4.28 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/NocturnaL%20Audio%20Avalon/NocturnaL%20Audio%20Avalon.png)