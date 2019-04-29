# Final Audio F7200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.8; 34 -1.3; 37 -1.9; 41 -2.5; 45 -3.0; 49 -3.4; 54 -3.8; 60 -4.4; 66 -4.9; 72 -5.5; 79 -6.0; 87 -6.5; 96 -7.2; 106 -7.8; 116 -8.2; 128 -8.7; 141 -9.1; 155 -9.4; 170 -9.7; 187 -9.9; 206 -10.0; 227 -10.0; 249 -10.1; 274 -10.1; 302 -10.0; 332 -9.9; 365 -9.7; 402 -9.6; 442 -9.4; 486 -9.1; 535 -8.8; 588 -8.3; 647 -7.9; 712 -7.3; 783 -6.7; 861 -6.1; 947 -5.7; 1042 -5.8; 1146 -6.2; 1261 -6.7; 1387 -6.7; 1526 -6.3; 1678 -5.5; 1846 -4.7; 2031 -4.2; 2234 -4.1; 2457 -4.8; 2703 -6.6; 2973 -9.4; 3270 -9.7; 3597 -5.7; 3957 -1.8; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -9.4; 8482 -10.4; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.6; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio F7200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio F7200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.5  | 6.3 dB   |
| Peaking | 229 Hz   | 0.49 | -4.1 dB  |
| Peaking | 3197 Hz  | 3.2  | -10.4 dB |
| Peaking | 4430 Hz  | 0.75 | 8.5 dB   |
| Peaking | 8176 Hz  | 3.79 | -8.3 dB  |
| Peaking | 975 Hz   | 1.71 | 3.2 dB   |
| Peaking | 1352 Hz  | 0.77 | -3.1 dB  |
| Peaking | 1983 Hz  | 1.78 | 2.5 dB   |
| Peaking | 6369 Hz  | 7.74 | 1.6 dB   |
| Peaking | 19970 Hz | 1.72 | -5.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20F7200/Final%20Audio%20F7200.png)