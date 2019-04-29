# Final Audio III
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.8; 23 -12.0; 25 -12.1; 28 -12.4; 31 -12.6; 34 -12.7; 37 -12.9; 41 -13.0; 45 -13.2; 49 -13.3; 54 -13.4; 60 -13.6; 66 -13.8; 72 -13.9; 79 -14.1; 87 -14.3; 96 -14.4; 106 -14.5; 116 -14.5; 128 -14.5; 141 -14.5; 155 -14.2; 170 -13.9; 187 -13.5; 206 -13.0; 227 -12.5; 249 -11.9; 274 -11.1; 302 -10.3; 332 -9.5; 365 -8.5; 402 -7.6; 442 -6.6; 486 -5.4; 535 -4.1; 588 -2.9; 647 -1.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.9; 3270 -4.2; 3597 -8.5; 3957 -11.3; 4353 -10.1; 4788 -8.6; 5267 -8.9; 5793 -11.9; 6373 -18.1; 7010 -16.1; 7711 -13.4; 8482 -12.4; 9330 -8.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio III GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio III ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 10 Hz    | 1.08 | -4.6 dB  |
| Peaking | 66 Hz    | 0.25 | -6.1 dB  |
| Peaking | 262 Hz   | 0.46 | -6.2 dB  |
| Peaking | 878 Hz   | 0.33 | 8.9 dB   |
| Peaking | 6606 Hz  | 1.86 | -12.0 dB |
| Peaking | 1258 Hz  | 2.75 | -1.0 dB  |
| Peaking | 2951 Hz  | 2.19 | 4.6 dB   |
| Peaking | 3852 Hz  | 2.83 | -7.3 dB  |
| Peaking | 5261 Hz  | 4.95 | 3.5 dB   |
| Peaking | 10453 Hz | 4.39 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.8 dB |
| Peaking | 8000 Hz  | 1.41 | -7.3 dB |
| Peaking | 16000 Hz | 1.41 | 1.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20III/Final%20Audio%20III.png)