# Sennheiser IE 800 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.1; 25 -10.1; 28 -10.2; 31 -10.3; 34 -10.4; 37 -10.5; 41 -10.5; 45 -10.6; 49 -10.6; 54 -10.7; 60 -10.8; 66 -11.0; 72 -11.1; 79 -11.2; 87 -11.3; 96 -11.5; 106 -11.6; 116 -11.6; 128 -11.7; 141 -11.7; 155 -11.5; 170 -11.1; 187 -10.6; 206 -10.1; 227 -10.6; 249 -11.6; 274 -11.2; 302 -10.5; 332 -9.8; 365 -9.4; 402 -9.1; 442 -8.7; 486 -8.3; 535 -7.9; 588 -7.8; 647 -7.7; 712 -7.5; 783 -7.4; 861 -7.5; 947 -7.9; 1042 -8.6; 1146 -8.9; 1261 -8.8; 1387 -8.4; 1526 -8.1; 1678 -7.4; 1846 -6.1; 2031 -4.4; 2234 -2.4; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -2.7; 5267 -5.7; 5793 -5.6; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.7; 11289 -6.7; 12418 -11.0; 13660 -21.4; 15026 -31.4; 16529 -32.8; 18182 -27.0; 20000 -21.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.16 | -3.1 dB  |
| Peaking | 243 Hz   | 0.31 | -4.0 dB  |
| Peaking | 1330 Hz  | 1.43 | -6.6 dB  |
| Peaking | 8009 Hz  | 0.18 | 21.0 dB  |
| Peaking | 16092 Hz | 0.43 | -43.3 dB |
| Peaking | 3217 Hz  | 1.22 | 2.5 dB   |
| Peaking | 5410 Hz  | 7.06 | -4.8 dB  |
| Peaking | 10433 Hz | 0.1  | -1.2 dB  |
| Peaking | 11698 Hz | 2.64 | 6.9 dB   |
| Peaking | 14464 Hz | 4.9  | -5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 16000 Hz | 1.41 | -33.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20IE%20800%20S/Sennheiser%20IE%20800%20S.png)