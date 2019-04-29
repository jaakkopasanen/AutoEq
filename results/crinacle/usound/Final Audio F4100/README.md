# Final Audio F4100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.9; 41 -1.5; 45 -2.1; 49 -2.6; 54 -3.1; 60 -3.8; 66 -4.4; 72 -5.0; 79 -5.5; 87 -6.0; 96 -6.7; 106 -7.4; 116 -7.8; 128 -8.3; 141 -8.8; 155 -9.1; 170 -9.4; 187 -9.6; 206 -9.7; 227 -9.8; 249 -9.8; 274 -9.8; 302 -9.7; 332 -9.7; 365 -9.6; 402 -9.4; 442 -9.2; 486 -8.9; 535 -8.6; 588 -8.2; 647 -7.7; 712 -7.1; 783 -6.6; 861 -6.1; 947 -5.7; 1042 -5.7; 1146 -6.2; 1261 -6.6; 1387 -6.7; 1526 -6.3; 1678 -5.5; 1846 -4.7; 2031 -4.2; 2234 -4.2; 2457 -4.9; 2703 -6.7; 2973 -9.4; 3270 -9.5; 3597 -5.7; 3957 -1.7; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.1; 7711 -10.0; 8482 -11.0; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio F4100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio F4100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.51 | 6.5 dB   |
| Peaking | 226 Hz   | 0.49 | -3.9 dB  |
| Peaking | 3184 Hz  | 3.21 | -10.1 dB |
| Peaking | 4537 Hz  | 0.74 | 8.5 dB   |
| Peaking | 8193 Hz  | 3.57 | -9.1 dB  |
| Peaking | 969 Hz   | 1.66 | 3.4 dB   |
| Peaking | 1250 Hz  | 0.81 | -3.0 dB  |
| Peaking | 2008 Hz  | 2.02 | 2.1 dB   |
| Peaking | 6450 Hz  | 7.5  | 1.8 dB   |
| Peaking | 21130 Hz | 0.08 | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20F4100/Final%20Audio%20F4100.png)