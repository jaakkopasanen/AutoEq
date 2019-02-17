# Sony MDR-Z1R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.4; 25 -9.6; 28 -9.7; 31 -9.8; 34 -9.8; 37 -9.9; 41 -9.9; 45 -9.7; 49 -9.5; 54 -9.5; 60 -9.6; 66 -9.8; 72 -9.9; 79 -10.1; 87 -10.8; 96 -11.4; 106 -11.6; 116 -11.7; 128 -12.0; 141 -12.0; 155 -11.7; 170 -11.0; 187 -10.6; 206 -10.1; 227 -9.5; 249 -9.0; 274 -8.6; 302 -8.2; 332 -7.8; 365 -7.5; 402 -7.3; 442 -7.2; 486 -7.0; 535 -6.4; 588 -6.4; 647 -6.6; 712 -6.7; 783 -6.8; 861 -6.9; 947 -6.7; 1042 -6.2; 1146 -5.6; 1261 -5.3; 1387 -5.2; 1526 -5.4; 1678 -6.0; 1846 -6.9; 2031 -7.8; 2234 -7.7; 2457 -7.9; 2703 -6.2; 2973 -5.1; 3270 -11.7; 3597 -6.1; 3957 -0.5; 4353 -0.5; 4788 -1.2; 5267 -3.0; 5793 -1.2; 6373 -3.7; 7010 -7.0; 7711 -6.3; 8482 -6.5; 9330 -8.2; 10263 -11.3; 11289 -10.5; 12418 -9.5; 13660 -10.6; 15026 -11.5; 16529 -8.4; 18182 -6.7; 20000 -15.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z1R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z1R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 29 Hz    |  0.62 | -2.9 dB |
| Peaking | 133 Hz   |  0.85 | -5.3 dB |
| Peaking | 3315 Hz  |  7.89 | -8.8 dB |
| Peaking | 4565 Hz  |  1.52 | 7.2 dB  |
| Peaking | 13183 Hz |  0.69 | -4.6 dB |
| Peaking | 1384 Hz  |  2.71 | 1.6 dB  |
| Peaking | 2278 Hz  |  2.62 | -2.6 dB |
| Peaking | 2891 Hz  | 10.08 | 2.6 dB  |
| Peaking | 17820 Hz |  2.47 | 3.0 dB  |
| Peaking | 20013 Hz |  1.9  | -8.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -5.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20MDR-Z1R/Sony%20MDR-Z1R.png)