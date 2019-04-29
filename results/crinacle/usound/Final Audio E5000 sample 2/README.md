# Final Audio E5000 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.4; 25 -10.8; 28 -11.3; 31 -11.7; 34 -12.0; 37 -12.2; 41 -12.4; 45 -12.4; 49 -12.4; 54 -12.5; 60 -12.6; 66 -12.7; 72 -12.8; 79 -12.8; 87 -12.8; 96 -12.9; 106 -12.9; 116 -12.8; 128 -12.6; 141 -12.6; 155 -12.3; 170 -12.0; 187 -11.6; 206 -11.4; 227 -11.1; 249 -10.8; 274 -10.4; 302 -10.0; 332 -9.5; 365 -9.2; 402 -8.8; 442 -8.4; 486 -8.1; 535 -7.7; 588 -7.3; 647 -6.9; 712 -6.2; 783 -6.1; 861 -6.0; 947 -5.8; 1042 -6.0; 1146 -6.4; 1261 -7.0; 1387 -7.2; 1526 -7.0; 1678 -6.6; 1846 -6.0; 2031 -5.5; 2234 -5.1; 2457 -5.1; 2703 -5.3; 2973 -5.6; 3270 -5.5; 3597 -4.8; 3957 -3.5; 4353 -1.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.7; 16529 -7.3; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E5000 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E5000 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 48 Hz    | 0.39 | -5.3 dB |
| Peaking | 172 Hz   | 0.62 | -3.7 dB |
| Peaking | 2256 Hz  | 4.94 | 0.9 dB  |
| Peaking | 5548 Hz  | 1.53 | 7.4 dB  |
| Peaking | 8022 Hz  | 1.71 | -2.4 dB |
| Peaking | 890 Hz   | 2.15 | 1.2 dB  |
| Peaking | 1397 Hz  | 3.86 | -1.1 dB |
| Peaking | 3406 Hz  | 4.7  | -0.8 dB |
| Peaking | 4486 Hz  | 8.91 | 1.2 dB  |
| Peaking | 15630 Hz | 3.76 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20E5000%20sample%202/Final%20Audio%20E5000%20sample%202.png)