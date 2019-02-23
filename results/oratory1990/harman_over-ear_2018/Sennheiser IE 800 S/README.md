# Sennheiser IE 800 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.6; 25 -11.7; 28 -11.8; 31 -11.8; 34 -11.8; 37 -11.8; 41 -11.8; 45 -11.8; 49 -11.7; 54 -11.7; 60 -11.7; 66 -11.8; 72 -11.8; 79 -11.8; 87 -11.8; 96 -11.9; 106 -12.0; 116 -11.9; 128 -11.9; 141 -11.9; 155 -11.6; 170 -11.1; 187 -10.6; 206 -10.0; 227 -10.4; 249 -11.4; 274 -10.7; 302 -9.8; 332 -9.0; 365 -8.6; 402 -8.2; 442 -7.7; 486 -7.2; 535 -6.7; 588 -6.5; 647 -6.4; 712 -6.3; 783 -6.4; 861 -6.6; 947 -7.2; 1042 -7.9; 1146 -8.3; 1261 -8.3; 1387 -8.0; 1526 -8.0; 1678 -7.3; 1846 -6.0; 2031 -4.5; 2234 -2.9; 2457 -1.3; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -3.1; 5267 -6.6; 5793 -7.1; 6373 -2.6; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.8; 13660 -12.8; 15026 -14.5; 16529 -12.7; 18182 -10.7; 20000 -14.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.22 | -5.1 dB  |
| Peaking | 179 Hz   | 0.71 | -2.5 dB  |
| Peaking | 3364 Hz  | 1.18 | 8.6 dB   |
| Peaking | 12074 Hz | 0.36 | 28.9 dB  |
| Peaking | 13496 Hz | 0.3  | -32.9 dB |
| Peaking | 1452 Hz  | 2.58 | -2.0 dB  |
| Peaking | 2426 Hz  | 4.81 | 1.9 dB   |
| Peaking | 5609 Hz  | 7.16 | -4.1 dB  |
| Peaking | 6557 Hz  | 5.01 | 4.3 dB   |
| Peaking | 7860 Hz  | 2.85 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -9.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20IE%20800%20S/Sennheiser%20IE%20800%20S.png)