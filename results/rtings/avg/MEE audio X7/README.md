# MEE audio X7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.2; 60 -1.9; 66 -2.5; 72 -3.0; 79 -3.5; 87 -4.1; 96 -4.7; 106 -5.5; 116 -6.1; 128 -6.6; 141 -7.0; 155 -7.3; 170 -7.4; 187 -7.5; 206 -7.5; 227 -7.4; 249 -7.0; 274 -6.6; 302 -6.2; 332 -5.7; 365 -5.1; 402 -4.5; 442 -4.1; 486 -3.5; 535 -2.8; 588 -2.7; 647 -2.4; 712 -2.0; 783 -1.9; 861 -2.3; 947 -2.9; 1042 -3.3; 1146 -3.8; 1261 -4.2; 1387 -4.4; 1526 -4.6; 1678 -5.1; 1846 -5.7; 2031 -6.2; 2234 -6.3; 2457 -6.7; 2703 -8.5; 2973 -11.1; 3270 -12.9; 3597 -13.8; 3957 -14.9; 4353 -17.9; 4788 -18.6; 5267 -12.4; 5793 -6.9; 6373 -4.6; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.0; 15026 -9.2; 16529 -8.8; 18182 -10.6; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio X7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio X7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.78 | 7.0 dB   |
| Peaking | 837 Hz   | 0.86 | 4.7 dB   |
| Peaking | 4618 Hz  | 1.81 | -16.3 dB |
| Peaking | 6185 Hz  | 1.86 | 8.8 dB   |
| Peaking | 18719 Hz | 0.73 | -4.3 dB  |
| Peaking | 68 Hz    | 1.84 | 1.2 dB   |
| Peaking | 178 Hz   | 1.37 | -2.0 dB  |
| Peaking | 2532 Hz  | 2.22 | 2.3 dB   |
| Peaking | 3110 Hz  | 2.87 | -3.0 dB  |
| Peaking | 4026 Hz  | 6.85 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB   |
| Peaking | 62 Hz    | 1.41 | 3.8 dB   |
| Peaking | 125 Hz   | 1.41 | -0.9 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 3.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 4000 Hz  | 1.41 | -11.1 dB |
| Peaking | 8000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 16000 Hz | 1.41 | -3.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20X7/MEE%20audio%20X7.png)