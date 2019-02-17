# Sennheiser IE 800 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.4; 23 -10.5; 25 -10.6; 28 -10.6; 31 -10.7; 34 -10.7; 37 -10.7; 41 -10.7; 45 -10.7; 49 -10.6; 54 -10.6; 60 -10.6; 66 -10.6; 72 -10.7; 79 -10.7; 87 -10.7; 96 -10.8; 106 -10.8; 116 -10.8; 128 -10.8; 141 -10.8; 155 -10.5; 170 -10.0; 187 -9.5; 206 -8.9; 227 -9.3; 249 -10.3; 274 -9.6; 302 -8.7; 332 -7.9; 365 -7.5; 402 -7.1; 442 -6.6; 486 -6.1; 535 -5.6; 588 -5.4; 647 -5.3; 712 -5.2; 783 -5.2; 861 -5.5; 947 -6.1; 1042 -6.8; 1146 -7.2; 1261 -7.2; 1387 -6.9; 1526 -6.8; 1678 -6.2; 1846 -4.9; 2031 -3.4; 2234 -1.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.0; 5267 -5.4; 5793 -6.0; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.7; 13660 -11.7; 15026 -13.4; 16529 -11.6; 18182 -9.6; 20000 -13.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 32 Hz    |  0.28 | -4.0 dB  |
| Peaking | 153 Hz   |  0.78 | -2.6 dB  |
| Peaking | 3343 Hz  |  1.13 | 7.0 dB   |
| Peaking | 12968 Hz |  0.52 | 16.2 dB  |
| Peaking | 14307 Hz |  0.55 | -21.5 dB |
| Peaking | 263 Hz   |  5.4  | -1.8 dB  |
| Peaking | 736 Hz   |  0.95 | 3.6 dB   |
| Peaking | 1319 Hz  |  0.6  | -3.5 dB  |
| Peaking | 2331 Hz  |  2.49 | 3.4 dB   |
| Peaking | 6568 Hz  | 11.44 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -7.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20IE%20800%20S/Sennheiser%20IE%20800%20S.png)