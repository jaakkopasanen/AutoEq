# Final Audio E2000 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.2; 28 -2.1; 31 -2.9; 34 -3.5; 37 -4.1; 41 -4.7; 45 -5.2; 49 -5.7; 54 -6.3; 60 -6.9; 66 -7.5; 72 -8.0; 79 -8.5; 87 -9.1; 96 -9.6; 106 -10.1; 116 -10.4; 128 -10.7; 141 -10.9; 155 -11.1; 170 -11.1; 187 -11.0; 206 -10.9; 227 -10.7; 249 -10.4; 274 -10.1; 302 -9.7; 332 -9.2; 365 -8.7; 402 -8.4; 442 -8.1; 486 -7.6; 535 -7.0; 588 -6.5; 647 -6.0; 712 -5.3; 783 -4.8; 861 -3.9; 947 -3.7; 1042 -3.8; 1146 -4.5; 1261 -5.3; 1387 -5.9; 1526 -5.9; 1678 -5.6; 1846 -5.3; 2031 -5.2; 2234 -5.4; 2457 -5.7; 2703 -5.7; 2973 -4.9; 3270 -3.6; 3597 -2.2; 3957 -1.5; 4353 -1.0; 4788 -1.2; 5267 -2.0; 5793 -4.1; 6373 -7.0; 7010 -6.2; 7711 -6.2; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -7.3; 16529 -10.4; 18182 -8.0; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E2000 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E2000 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.61 | 6.6 dB  |
| Peaking | 165 Hz   | 0.52 | -5.0 dB |
| Peaking | 915 Hz   | 1.63 | 3.3 dB  |
| Peaking | 4332 Hz  | 2.05 | 5.9 dB  |
| Peaking | 16814 Hz | 2.31 | -4.4 dB |
| Peaking | 1420 Hz  | 5.6  | -0.5 dB |
| Peaking | 1926 Hz  | 5.37 | 0.6 dB  |
| Peaking | 4366 Hz  | 7.74 | -1.0 dB |
| Peaking | 5380 Hz  | 3.31 | 1.6 dB  |
| Peaking | 6338 Hz  | 5.54 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20E2000%20sample%202/Final%20Audio%20E2000%20sample%202.png)