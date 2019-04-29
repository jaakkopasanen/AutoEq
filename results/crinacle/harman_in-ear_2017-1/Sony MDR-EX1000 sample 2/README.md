# Sony MDR-EX1000 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -0.8; 31 -1.1; 34 -1.3; 37 -1.5; 41 -1.8; 45 -2.1; 49 -2.3; 54 -2.6; 60 -3.1; 66 -3.5; 72 -3.9; 79 -4.3; 87 -4.7; 96 -5.3; 106 -5.7; 116 -6.3; 128 -6.7; 141 -7.1; 155 -7.5; 170 -7.7; 187 -8.0; 206 -8.1; 227 -8.3; 249 -8.5; 274 -8.6; 302 -8.6; 332 -8.5; 365 -8.6; 402 -8.4; 442 -8.4; 486 -8.2; 535 -8.0; 588 -7.7; 647 -7.1; 712 -6.6; 783 -6.0; 861 -5.5; 947 -5.3; 1042 -5.7; 1146 -6.4; 1261 -7.0; 1387 -7.2; 1526 -7.3; 1678 -7.4; 1846 -7.6; 2031 -7.7; 2234 -7.7; 2457 -7.4; 2703 -6.3; 2973 -4.5; 3270 -2.6; 3597 -1.5; 3957 -1.3; 4353 -2.4; 4788 -5.0; 5267 -9.7; 5793 -9.6; 6373 -4.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.9; 13660 -10.2; 15026 -9.6; 16529 -10.4; 18182 -14.3; 20000 -17.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX1000 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX1000 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.61 | 5.7 dB   |
| Peaking | 57 Hz    | 0.93 | 2.0 dB   |
| Peaking | 272 Hz   | 0.74 | -2.4 dB  |
| Peaking | 3772 Hz  | 3.7  | 6.2 dB   |
| Peaking | 19564 Hz | 0.64 | -10.8 dB |
| Peaking | 921 Hz   | 3.45 | 1.9 dB   |
| Peaking | 2056 Hz  | 1.45 | -1.7 dB  |
| Peaking | 5125 Hz  | 1.15 | 2.4 dB   |
| Peaking | 5512 Hz  | 5.05 | -7.6 dB  |
| Peaking | 6658 Hz  | 7.46 | 3.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -5.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20MDR-EX1000%20sample%202/Sony%20MDR-EX1000%20sample%202.png)